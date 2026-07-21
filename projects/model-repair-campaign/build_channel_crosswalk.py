#!/usr/bin/env python3
"""Build a neutral person/appearance/program-lead crosswalk from the v0.3 intake.

This script does not resolve identities or programs.  It records only recoverable
title-surface links, explicit alias proposals, and contributor-presence links.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INTAKE_PATH = ROOT / "channel_intake_v0_3.json"
REGISTRY_PATH = ROOT / "candidate_registry_v0_3.json"
OUTPUT_PATH = ROOT / "channel_crosswalk_v0_4.json"

CENSUS_EPOCH = "channel_2026_07_13"
CROSSWALK_VERSION = "crosswalk_v1"


def tokens(value: str) -> list[str]:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    return re.findall(r"[a-z0-9]+", value)


def normalized(value: str) -> str:
    return " ".join(tokens(value))


def surface_contains_name(surface: str, name: str) -> bool:
    surface_tokens = tokens(surface)
    name_tokens = tokens(name)
    if not surface_tokens or not name_tokens or len(name_tokens) > len(surface_tokens):
        return False
    width = len(name_tokens)
    return any(surface_tokens[i : i + width] == name_tokens for i in range(len(surface_tokens) - width + 1))


# These are title-surface proposals, not source-verified identities.
EXPLICIT_LINKS = [
    ("person_elan_barenholtz", "prefix_barenholtz_hahn_jaimungal", "surname_panel", "Barenholtz"),
    ("person_william_hahn", "prefix_barenholtz_hahn_jaimungal", "surname_panel", "Hahn"),
    ("person_bernardo_kastrup", "prefix_kastrup_hoffman_and_schneider", "surname_panel", "Kastrup"),
    ("person_donald_hoffman", "prefix_kastrup_hoffman_and_schneider", "surname_panel", "Hoffman"),
    ("person_susan_schneider", "prefix_kastrup_hoffman_and_schneider", "surname_panel", "Schneider"),
    ("person_bernardo_kastrup", "prefix_kastrup_vs_vervaeke", "surname_panel", "Kastrup"),
    ("person_john_vervaeke", "prefix_kastrup_vs_vervaeke", "surname_panel", "Vervaeke"),
    ("person_george_knapp", "prefix_live", "surname_panel", "Knapp"),
    ("person_jeremy_corbell", "prefix_live", "surname_panel", "Corbell"),
    ("person_donald_hoffman", "prefix_live", "surname_panel", "Hoffman"),
    ("person_john_vervaeke", "prefix_live", "surname_panel", "Vervaeke"),
    ("person_michael_levin", "prefix_live", "surname_panel", "Levin"),
    ("person_luis_elizondo", "prefix_lue_elizondo", "verified_alias", "Lue Elizondo"),
    ("person_luis_elizondo", "prefix_lue_elizondo_and_sean_cahill", "verified_alias", "Lue Elizondo"),
    ("person_luis_elizondo", "prefix_the_best_of_lue_elizondo", "verified_alias", "Lue Elizondo"),
    ("person_claudia_passos", "prefix_passos_montemayor_mindt", "surname_panel", "Passos"),
    ("person_carlos_montemayor", "prefix_passos_montemayor_mindt", "surname_panel", "Montemayor"),
    ("person_garrett_mindt", "prefix_passos_montemayor_mindt", "surname_panel", "Mindt"),
    ("person_salvatore_pais", "prefix_sal_pais_and_stephon_alexander", "verified_alias", "Sal Pais"),
]

CONTRIBUTOR_ALIASES = {
    "robert spekkens": "rob spekkens",
    "j b manchak": "jb manchak",
}


def main() -> None:
    intake = json.loads(INTAKE_PATH.read_text())
    registry = json.loads(REGISTRY_PATH.read_text())
    people = {p["person_id"]: p for p in intake["person_identity_candidates"]}
    groups = {g["intake_group_id"]: g for g in intake["intake_groups"]}

    edges: dict[tuple[str, str], dict] = {}
    for person_id, person in people.items():
        name = person["display_name"]
        for group_id, group in groups.items():
            raw_prefix = group.get("raw_title_prefix") or ""
            if raw_prefix:
                matched = surface_contains_name(raw_prefix, name)
                method = "exact_prefix"
                surface = raw_prefix
            else:
                title_surface = " || ".join(group.get("titles") or [])
                matched = surface_contains_name(title_surface, name)
                method = "unparsed_title"
                surface = title_surface
            if matched:
                edges[(person_id, group_id)] = {
                    "person_id": person_id,
                    "intake_group_id": group_id,
                    "match_method": method,
                    "matched_surface": surface,
                    "evidence_episode_ids": group.get("rss_indices", []),
                    "verification_state": "PROPOSED_FROM_FEED_SURFACE"
                }

    direct_edge_count = len(edges)
    direct_person_count = len({person_id for person_id, _ in edges})
    direct_group_count = len({group_id for _, group_id in edges})

    for person_id, group_id, method, surface in EXPLICIT_LINKS:
        if person_id not in people:
            raise ValueError(f"Missing explicit-link person: {person_id}")
        if group_id not in groups:
            raise ValueError(f"Missing explicit-link group: {group_id}")
        edges[(person_id, group_id)] = {
            "person_id": person_id,
            "intake_group_id": group_id,
            "match_method": method,
            "matched_surface": surface,
            "evidence_episode_ids": groups[group_id].get("rss_indices", []),
            "verification_state": "PROPOSED_ALIAS_OR_SURNAME_LINK"
        }

    appearance_edges = sorted(edges.values(), key=lambda item: (item["person_id"], item["intake_group_id"]))
    linked_people = {edge["person_id"] for edge in appearance_edges}
    linked_groups = {edge["intake_group_id"] for edge in appearance_edges}
    residual_groups = [
        {
            "intake_group_id": group_id,
            "raw_title_prefix": group.get("raw_title_prefix", ""),
            "titles": group.get("titles", []),
            "resolution_state": "HOST_ENTITY_FORMAT_OR_IDENTITY_RESOLUTION_REQUIRED",
            "ranking_state": "NOT_RANKABLE"
        }
        for group_id, group in sorted(groups.items())
        if group_id not in linked_groups
    ]

    people_by_name = {normalized(person["display_name"]): person_id for person_id, person in people.items()}
    program_contributions = []
    for candidate in registry["candidates"]:
        for contributor in candidate.get("contributors", []):
            contributor_name = normalized(contributor)
            contributor_name = CONTRIBUTOR_ALIASES.get(contributor_name, contributor_name)
            person_id = people_by_name.get(contributor_name)
            if person_id:
                program_contributions.append({
                    "person_id": person_id,
                    "program_id": candidate["id"],
                    "contribution_role": "CONTRIBUTOR_IDENTITY_MATCH_ONLY",
                    "evidence_refs": [f"candidate_registry_v0_3.json#{candidate['id']}"],
                    "verification_state": "PROVISIONAL_NORMALIZED_NAME_MATCH",
                    "episode_ownership_inference_prohibited": True
                })
    program_contributions.sort(key=lambda item: (item["person_id"], item["program_id"]))

    contribution_people = {item["person_id"] for item in program_contributions}
    contribution_programs = {item["program_id"] for item in program_contributions}
    contributor_groups = {
        edge["intake_group_id"]
        for edge in appearance_edges
        if edge["person_id"] in contribution_people
    }
    contributor_episodes = {
        rss_index
        for group_id in contributor_groups
        for rss_index in groups[group_id].get("rss_indices", [])
    }

    person_units = [f"identity:{person_id}" for person_id in sorted(people)]
    residual_units = [f"residual:{item['intake_group_id']}" for item in residual_groups]

    def shuffle_key(unit_id: str) -> str:
        raw = f"{CENSUS_EPOCH}|{CROSSWALK_VERSION}|{unit_id}".encode()
        return hashlib.sha256(raw).hexdigest()

    person_units.sort(key=shuffle_key)
    residual_units.sort(key=shuffle_key)
    batches = [
        {
            "batch_id": f"batch_{index + 1:02d}",
            "scientific_priority": None,
            "administrative_units": [residual_units[index]],
        }
        for index in range(16)
    ]
    for index, unit_id in enumerate(person_units):
        batches[index % 16]["administrative_units"].append(unit_id)
    for batch in batches:
        batch["administrative_units"].sort(key=shuffle_key)
        batch["unit_count"] = len(batch["administrative_units"])

    output = {
        "schema_version": "toe-channel-entity-appearance-crosswalk/0.4",
        "census_epoch": CENSUS_EPOCH,
        "source_intake": "channel_intake_v0_3.json",
        "source_registry": "candidate_registry_v0_3.json",
        "status": "STRUCTURAL_APPEARANCE_CROSSWALK_COMPLETE_PROGRAM_RESOLUTION_OPEN",
        "claim_ceiling": "Feed-title surfaces support provisional person-to-appearance and contributor-to-card links only. They do not establish identity, guest role, program ownership, episode content, source-native model scope, relevance, merit, or rank.",
        "coverage": {
            "episodes": len(intake["episodes"]),
            "raw_intake_groups": len(groups),
            "provisional_non_host_people": len(people),
            "direct_person_group_edges": direct_edge_count,
            "direct_people_linked": direct_person_count,
            "direct_groups_linked": direct_group_count,
            "explicit_alias_or_surname_edges": len(EXPLICIT_LINKS),
            "person_group_edges_total": len(appearance_edges),
            "people_linked": len(linked_people),
            "groups_linked": len(linked_groups),
            "residual_groups": len(residual_groups),
            "registry_cards": len(registry["candidates"]),
            "people_linked_to_existing_cards_by_contributor_identity": len(contribution_people),
            "cards_linked_to_channel_people": len(contribution_programs),
            "groups_containing_linked_contributors": len(contributor_groups),
            "episodes_containing_linked_contributors": len(contributor_episodes),
            "people_without_existing_registry_card": len(people) - len(contribution_people),
            "program_resolved_groups": 0,
            "ranking_eligible_programs": 0
        },
        "policies": {
            "people_are_models": False,
            "appearance_implies_program": False,
            "contributor_presence_implies_episode_program": False,
            "title_signal_is_source_native_dossier": False,
            "unknown_means_weak": False,
            "unknown_means": "UNRESOLVED_OR_UNRANKED",
            "target_model_reference": "joshua_model_dossier_v0_1.json",
            "target_model_must_be_content_addressed_before_comparison": True
        },
        "entities": [
            {
                "entity_id": person_id,
                "entity_type": "person",
                "canonical_name": person["display_name"],
                "identity_state": person["identity_verification_status"],
                "program_resolution_state": person["program_resolution_status"],
                "ranking_state": "NOT_A_RANKABLE_OBJECT"
            }
            for person_id, person in sorted(people.items())
        ],
        "appearance_edges": appearance_edges,
        "residual_groups": residual_groups,
        "program_contributions": program_contributions,
        "administrative_batching": {
            "method": "PUBLIC_HASH_ORDER_ROUND_ROBIN_WITH_ONE_RESIDUAL_UNIT_PER_BATCH",
            "hash_preimage_template": f"{CENSUS_EPOCH}|{CROSSWALK_VERSION}|<unit_id>",
            "scientific_priority_conveyed": False,
            "cohort_must_close_before_ranking": True,
            "batches": batches
        },
        "known_identity_risks": [
            "All identities remain provisional pending source verification.",
            "Claudia Passos requires a verified full surname form.",
            "Mononyms and handles such as Atlas, Parker, Marwa, Tevin, Fidias, Gen Zed, and Artisan Tony require identity resolution.",
            "Title mentions may describe a subject rather than an appearance.",
            "The Live episode leaves approximately forty participants unnamed.",
            "DemystifySci hosts, the QBism guest, and the Egyptologist interviewer remain unresolved."
        ]
    }

    if direct_edge_count != 275 or direct_person_count != 214 or direct_group_count != 241:
        raise ValueError(
            f"Direct mapping drift: edges={direct_edge_count}, people={direct_person_count}, groups={direct_group_count}"
        )
    if len(appearance_edges) != 294 or len(linked_people) != 218 or len(linked_groups) != 248:
        raise ValueError(
            f"Final mapping drift: edges={len(appearance_edges)}, people={len(linked_people)}, groups={len(linked_groups)}"
        )
    if len(residual_groups) != 16:
        raise ValueError(f"Residual group drift: {len(residual_groups)}")
    if len(contribution_people) != 39 or len(contribution_programs) != 32:
        raise ValueError(
            f"Contributor mapping drift: people={len(contribution_people)}, programs={len(contribution_programs)}"
        )
    if len(contributor_groups) != 58 or len(contributor_episodes) != 77:
        raise ValueError(
            f"Contributor appearance drift: groups={len(contributor_groups)}, episodes={len(contributor_episodes)}"
        )
    if sorted(batch["unit_count"] for batch in batches) != [14] * 6 + [15] * 10:
        raise ValueError("Unexpected administrative batch sizes")

    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
