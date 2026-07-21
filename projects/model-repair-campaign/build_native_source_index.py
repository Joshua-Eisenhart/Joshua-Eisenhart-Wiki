#!/usr/bin/env python3
"""Build a normalized index over independently researched source-native cards.

The source cards deliberately retain heterogeneous, source-appropriate detail.  This
script indexes them without pretending that a common schema makes them comparable
or ranking-eligible.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CROSSWALK = ROOT / "channel_crosswalk_v0_4.json"
OUTPUT = ROOT / "native_source_card_index_v0_1.json"
ROSTER_OUTPUT = ROOT / "CHANNEL_PEOPLE_AND_PROGRAM_STATUS_2026-07-15.md"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def norm_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.casefold().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "", value)


def card_id(card: dict) -> str:
    for key in ("program_id", "id", "card_id", "program_card_id"):
        if card.get(key):
            return str(card[key])
    raise ValueError(f"Card lacks a stable id: {sorted(card)}")


def program_label(card: dict) -> str:
    for key in (
        "canonical_program",
        "program",
        "program_name",
        "title",
        "canonical_version_scope",
    ):
        if card.get(key):
            return str(card[key])
    return card_id(card)


def string_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if isinstance(item, (str, int, float))]
    return []


def contributors(card: dict) -> list[str]:
    values = string_list(card.get("contributors"))
    if not values and isinstance(card.get("native"), dict):
        values = string_list(card["native"].get("contributors"))
    return sorted(set(values), key=str.casefold)


def primary_sources(card: dict) -> list[dict]:
    values = card.get("primary_sources", [])
    if isinstance(values, dict):
        values = [values]
    out = []
    for value in values if isinstance(values, list) else []:
        if isinstance(value, str):
            out.append({"url": value})
        elif isinstance(value, dict):
            url = value.get("url") or value.get("href") or value.get("doi")
            if url:
                item = {"url": str(url)}
                if value.get("title"):
                    item["title"] = str(value["title"])
                out.append(item)
    return out


def surfaces(card: dict) -> list[str]:
    values = string_list(card.get("comparison_surfaces"))
    values.extend(string_list(card.get("comparison_surface_ids")))
    values.extend(string_list(card.get("joshua_surfaces")))
    crosswalk = card.get("joshua_crosswalk")
    if isinstance(crosswalk, dict):
        values.extend(string_list(crosswalk.get("comparison_surface_ids")))
    comparison = card.get("comparison")
    if isinstance(comparison, dict):
        values.extend(string_list(comparison.get("surfaces")))
        values.extend(string_list(comparison.get("comparison_surfaces")))
    return sorted(set(values))


def roles(card: dict) -> list[str]:
    values = string_list(card.get("proposed_roles"))
    values.extend(string_list(card.get("roles")))
    comparison = card.get("comparison")
    if isinstance(comparison, dict):
        values.extend(string_list(comparison.get("roles")))
        values.extend(string_list(comparison.get("proposed_roles")))
    return sorted(set(values))


def batch_paths() -> list[Path]:
    return sorted(ROOT.glob("native_source_cards_batch_*.json"))


def main() -> None:
    crosswalk = load(CROSSWALK)
    people = [
        entity
        for entity in crosswalk["entities"]
        if entity.get("entity_type") == "person"
    ]
    people_by_norm = {norm_name(p["canonical_name"]): p for p in people}

    entries = []
    batches = []
    seen_ids = set()
    all_source_urls = set()
    matched_people_to_cards: dict[str, list[str]] = {}
    matched_people_methods: dict[str, set[str]] = {}
    exact_contributor_person_ids: set[str] = set()
    resolution_records = []
    fully_resolved_administrative_batches = []

    for path in batch_paths():
        packet = load(path)
        cards = packet.get("cards", [])
        if not isinstance(cards, list):
            raise ValueError(f"{path.name}: cards must be a list")
        resolutions = packet.get("resolutions", [])
        if not isinstance(resolutions, list):
            raise ValueError(f"{path.name}: resolutions must be a list when supplied")
        administrative_batch = packet.get("administrative_batch", {})
        if isinstance(administrative_batch, str):
            administrative_batch = {"batch_id": administrative_batch}
        if not isinstance(administrative_batch, dict):
            administrative_batch = {}
        unit_count = administrative_batch.get("unit_count")
        if resolutions and isinstance(unit_count, int) and len(resolutions) == unit_count:
            fully_resolved_administrative_batches.append(administrative_batch.get("batch_id"))
        for record in resolutions:
            if isinstance(record, dict):
                normalized_record = {"source_batch": path.name, **record}
                if not normalized_record.get("administrative_unit") and record.get("unit_id"):
                    normalized_record["administrative_unit"] = record["unit_id"]
                resolution_records.append(normalized_record)
        batches.append(
            {
                "file": path.name,
                "schema_version": packet.get("schema_version"),
                "status": packet.get("status"),
                "card_count": len(cards),
                "administrative_batch_id": administrative_batch.get("batch_id"),
                "administrative_unit_count": unit_count,
                "resolution_record_count": len(resolutions),
            }
        )
        for card in cards:
            cid = card_id(card)
            if cid in seen_ids:
                raise ValueError(f"Duplicate source-card id: {cid}")
            seen_ids.add(cid)
            sources = primary_sources(card)
            all_source_urls.update(source["url"] for source in sources)
            card_people = []
            for contributor in contributors(card):
                person = people_by_norm.get(norm_name(contributor))
                if person:
                    entity_id = person["entity_id"]
                    card_people.append(entity_id)
                    exact_contributor_person_ids.add(entity_id)
                    matched_people_to_cards.setdefault(entity_id, []).append(cid)
                    matched_people_methods.setdefault(entity_id, set()).add(
                        "NORMALIZED_EXACT_CONTRIBUTOR_NAME"
                    )
            entries.append(
                {
                    "card_id": cid,
                    "source_batch": path.name,
                    "program_label": program_label(card),
                    "contributors": contributors(card),
                    "channel_person_entity_ids": sorted(set(card_people)),
                    "primary_source_count": len(sources),
                    "primary_sources": sources,
                    "comparison_surface_ids": surfaces(card),
                    "proposed_roles": roles(card),
                    "dossier_status": card.get("dossier_status", packet.get("status")),
                    "ranking_eligible": bool(card.get("ranking_eligible", False)),
                }
            )

    for record in resolution_records:
        unit = record.get("administrative_unit")
        if not isinstance(unit, str) or not unit.startswith("identity:"):
            continue
        entity_id = unit.removeprefix("identity:")
        linked_ids = string_list(record.get("card_ids"))
        for field in ("cross_reference", "card_reference"):
            reference = record.get(field)
            if isinstance(reference, dict) and reference.get("program_id"):
                linked_ids.append(str(reference["program_id"]))
            elif isinstance(reference, str) and "#" in reference:
                linked_ids.append(reference.rsplit("#", 1)[1])
        linked_ids = [value for value in linked_ids if value in seen_ids]
        if linked_ids:
            matched_people_to_cards.setdefault(entity_id, []).extend(linked_ids)
            matched_people_methods.setdefault(entity_id, set()).add(
                "ADMINISTRATIVE_RESOLUTION_RECORD"
            )

    entries.sort(key=lambda item: item["card_id"])
    matched_ids = set(matched_people_to_cards)
    unmatched = [
        {"entity_id": p["entity_id"], "canonical_name": p["canonical_name"]}
        for p in people
        if p["entity_id"] not in matched_ids
    ]
    matched = [
        {
            "entity_id": p["entity_id"],
            "canonical_name": p["canonical_name"],
            "source_card_ids": sorted(set(matched_people_to_cards[p["entity_id"]])),
            "link_methods": sorted(matched_people_methods.get(p["entity_id"], set())),
        }
        for p in people
        if p["entity_id"] in matched_ids
    ]

    result = {
        "schema_version": "0.1",
        "as_of": "2026-07-15",
        "status": "SOURCE_NATIVE_INDEX_NOT_A_RANKING",
        "claim_ceiling": "This index proves that a source-native starting card exists and links contributors to provisional channel identities by normalized exact name or an explicit administrative resolution record. It does not prove identity, episode topic, dossier completeness, baseline reproduction, comparison eligibility, repair, superiority, or scientific admission.",
        "policies": {
            "people_are_ranked": False,
            "cards_are_ranking_eligible": False,
            "unknown_is_zero": False,
            "source_native_baseline_required_before_repair": True,
            "comparison_unit": "program_version x role x question x evidence_packet",
        },
        "coverage": {
            "source_batch_count": len(batches),
            "source_card_count": len(entries),
            "unique_primary_source_url_count": len(all_source_urls),
            "channel_provisional_person_count": len(people),
            "channel_people_with_normalized_exact_contributor_name_card": len(
                exact_contributor_person_ids
            ),
            "channel_people_with_any_source_card_link": len(matched),
            "channel_people_without_any_source_card_link": len(unmatched),
            "ranking_eligible_card_count": sum(item["ranking_eligible"] for item in entries),
            "administrative_resolution_record_count": len(resolution_records),
            "fully_resolved_administrative_batch_count": len(
                set(value for value in fully_resolved_administrative_batches if value)
            ),
        },
        "source_batches": batches,
        "cards": entries,
        "channel_people_with_source_cards": matched,
        "channel_people_without_source_cards": unmatched,
        "administrative_resolution_records": resolution_records,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    roster_lines = [
        "# Channel people and source-native program status — 2026-07-15",
        "",
        "Status: provisional identity and research crosswalk, not a ranking.",
        "",
        (
            f"The appearance census contains {len(people)} provisional non-host people. "
            f"Normalized exact-name matching or reviewed administrative cross-reference "
            f"currently links {len(matched)} of them to at "
            f"least one of {len(entries)} source-native starting cards. A missing card means "
            "program discovery is open; it does not mean the person or their work was scored weak."
        ),
        "",
        "| Provisional channel identity | Source-native starting card ids | Research state |",
        "|---|---|---|",
    ]
    cards_by_person = {
        item["entity_id"]: item["source_card_ids"] for item in matched
    }
    for person in sorted(people, key=lambda item: item["canonical_name"].casefold()):
        name = person["canonical_name"].replace("|", "\\|")
        ids = cards_by_person.get(person["entity_id"], [])
        linked = ", ".join(f"`{value}`" for value in ids) if ids else "—"
        state = "SOURCE_NATIVE_STARTING_CARD" if ids else "PROGRAM_DISCOVERY_OPEN"
        roster_lines.append(f"| {name} | {linked} | {state} |")
    roster_lines.extend(
        [
            "",
            "Program cards are still split by version, role, question and evidence packet. "
            "A contributor match does not prove that a particular episode discusses that card, "
            "and no card is ranking-eligible before its native baseline is locked.",
        ]
    )
    ROSTER_OUTPUT.write_text("\n".join(roster_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
