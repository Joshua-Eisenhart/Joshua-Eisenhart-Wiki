#!/usr/bin/env python3
"""Validate neutral intake, model dossiers, and campaign selection v0.3.

This is a process check, not a scientific verdict. Names, discovery routes,
existing drafts, and prior work may be recorded as provenance but cannot make a
program rankable or activate a repair campaign.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "external-model-repair-campaign/0.3"
REGISTRY_SCHEMA_VERSION = "external-model-candidate-registry/0.3"
INTAKE_SCHEMA_VERSION = "toe-channel-neutral-intake/0.3"
CROSSWALK_SCHEMA_VERSION = "toe-channel-entity-appearance-crosswalk/0.4"
TARGET_DOSSIER_SCHEMA_VERSION = "joshua-model-dossier/0.1"
EXTERNAL_DOSSIER_SCHEMA_VERSION = "external-program-dossier-contract/0.1"
NATIVE_SOURCE_INDEX_SCHEMA_VERSION = "0.1"
FORBIDDEN_CEILINGS = {"canon", "canonical", "theorem", "theory_admitted"}
FORBIDDEN_RANKING_INPUTS = {
    "fame",
    "citation_count_alone",
    "episode_count",
    "institutional_status",
    "joshua_familiarity",
    "user_naming_order",
    "discovery_route",
    "registry_row_order",
    "existing_adapter_draft",
    "deep_read_progress",
    "prior_work_investment",
}
REQUIRED_OUTPUTS = {
    "selection_receipt",
    "source_native_receipt",
    "finite_behavior_surface",
    "behavioral_alias_census",
    "demand_families",
    "weakness_hypotheses",
    "schedule_receipts",
    "packet_relative_mss_frontiers",
    "controls",
    "kill_receipts",
    "provenance",
}
REQUIRED_CARD_KEYS = {
    "id",
    "program",
    "discovery_provenance",
    "known_to_joshua",
    "intake_status",
    "dossier_status",
    "dossier_receipt",
    "baseline_receipt",
    "ranking_eligible",
    "rank_state",
    "frontier_receipts",
    "selection_receipts",
}
REQUIRED_DRAFT_KEYS = {
    "id",
    "candidate_id",
    "origin",
    "selection_status",
    "selection_receipt",
    "dossier_receipt",
    "baseline_receipt",
    "eligibility_receipt",
    "source_native_baseline_required",
    "source_native_baseline_status",
    "selection_confers_priority",
    "claim_ceiling",
}
REQUIRED_SELECTION_KEYS = {
    "id",
    "candidate_id",
    "dossier_receipt",
    "baseline_receipt",
    "eligibility_receipt",
    "selection_receipt",
    "comparison_pool_ids",
    "declared_role",
    "question_packet",
    "matched_control",
    "held_out_test",
    "kill_criteria",
}


def _duplicates(values: list[str]) -> list[str]:
    return sorted({value for value in values if values.count(value) > 1})


def _read_linked_json(
    payload: dict[str, Any],
    field: str,
    base_dir: Path,
    supplied: dict[str, Any] | None,
    errors: list[str],
) -> dict[str, Any] | None:
    if supplied is not None:
        return supplied
    relative = payload.get(field)
    if not isinstance(relative, str) or not relative.strip():
        errors.append(f"{field} must identify a JSON packet")
        return None
    path = base_dir / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read {field} packet {path}: {exc}")
        return None


def _validate_registry(registry: dict[str, Any], errors: list[str]) -> dict[str, dict[str, Any]]:
    if registry.get("schema_version") != REGISTRY_SCHEMA_VERSION:
        errors.append(f"registry schema_version must be {REGISTRY_SCHEMA_VERSION!r}")
    if registry.get("registry_open") is not True:
        errors.append("candidate registry must remain open")
    if registry.get("completeness_claimed") is not False:
        errors.append("candidate registry must not claim field completeness")
    if "priority_frontiers" in registry:
        errors.append("priority_frontiers are forbidden before evidence eligibility")
    missing_forbidden = FORBIDDEN_RANKING_INPUTS - set(registry.get("forbidden_ranking_inputs", []))
    if missing_forbidden:
        errors.append(f"registry forbidden_ranking_inputs missing {sorted(missing_forbidden)}")

    families = registry.get("comparison_question_families")
    if not isinstance(families, list):
        errors.append("comparison_question_families must be a list")
    else:
        for index, family in enumerate(families):
            if family.get("membership_conveys_priority") is not False:
                errors.append(f"comparison_question_families[{index}] membership must convey no priority")
            if family.get("frontier_status") != "NOT_COMPUTED":
                errors.append(f"comparison_question_families[{index}] cannot be a computed frontier")

    cards = registry.get("candidates")
    if not isinstance(cards, list):
        errors.append("registry candidates must be a list")
        return {}
    by_id: dict[str, dict[str, Any]] = {}
    eligible_count = 0
    for index, card in enumerate(cards):
        prefix = f"registry.candidates[{index}]"
        if not isinstance(card, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_CARD_KEYS - set(card)
        if missing:
            errors.append(f"{prefix} missing {sorted(missing)}")
            continue
        card_id = card["id"]
        if card_id in by_id:
            errors.append(f"duplicate candidate id {card_id!r}")
        by_id[card_id] = card
        if "roles" in card or "status" in card or "next_action" in card:
            errors.append(f"{prefix} contains legacy rank/status fields")
        if card.get("ranking_eligible") is True:
            eligible_count += 1
            if not card.get("dossier_receipt") or not card.get("baseline_receipt"):
                errors.append(f"{prefix} cannot be eligible without dossier and baseline receipts")
            if card.get("rank_state") == "UNRANKED":
                errors.append(f"{prefix} eligible card cannot remain UNRANKED")
        elif card.get("rank_state") != "UNRANKED":
            errors.append(f"{prefix} ineligible card must remain UNRANKED")
        if card.get("frontier_receipts") and card.get("ranking_eligible") is not True:
            errors.append(f"{prefix} cannot enter a frontier before eligibility")
        if card.get("selection_receipts") and card.get("ranking_eligible") is not True:
            errors.append(f"{prefix} cannot be selected before eligibility")

    if registry.get("ranking_eligible_count") != eligible_count:
        errors.append("ranking_eligible_count does not match eligible candidate cards")
    computed = registry.get("computed_frontiers")
    if not isinstance(computed, list):
        errors.append("computed_frontiers must be a list")
    elif computed and eligible_count == 0:
        errors.append("frontiers cannot be populated when zero programs are eligible")
    return by_id


def _validate_intake(intake: dict[str, Any], errors: list[str]) -> None:
    if intake.get("schema_version") != INTAKE_SCHEMA_VERSION:
        errors.append(f"channel intake schema_version must be {INTAKE_SCHEMA_VERSION!r}")
    coverage = intake.get("coverage")
    if not isinstance(coverage, dict):
        errors.append("channel intake coverage must be an object")
        return
    if coverage.get("episodes_expected") != coverage.get("episodes_ingested"):
        errors.append("channel episode intake is incomplete")
    if coverage.get("ranking_eligible_programs") != 0:
        errors.append("raw channel intake cannot itself make programs ranking-eligible")
    if not isinstance(intake.get("episodes"), list) or len(intake["episodes"]) != coverage.get("episodes_ingested"):
        errors.append("channel intake episode rows do not reconcile to coverage")


def _validate_crosswalk(crosswalk: dict[str, Any], errors: list[str]) -> None:
    if crosswalk.get("schema_version") != CROSSWALK_SCHEMA_VERSION:
        errors.append(f"channel crosswalk schema_version must be {CROSSWALK_SCHEMA_VERSION!r}")
    coverage = crosswalk.get("coverage")
    if not isinstance(coverage, dict):
        errors.append("channel crosswalk coverage must be an object")
        return
    expected = {
        "episodes": 354,
        "raw_intake_groups": 264,
        "provisional_non_host_people": 218,
        "person_group_edges_total": 294,
        "people_linked": 218,
        "groups_linked": 248,
        "residual_groups": 16,
        "registry_cards": 47,
        "people_linked_to_existing_cards_by_contributor_identity": 39,
        "cards_linked_to_channel_people": 32,
        "people_without_existing_registry_card": 179,
        "program_resolved_groups": 0,
        "ranking_eligible_programs": 0,
    }
    for field, value in expected.items():
        if coverage.get(field) != value:
            errors.append(f"channel crosswalk coverage.{field} must be {value}")
    entities = crosswalk.get("entities")
    edges = crosswalk.get("appearance_edges")
    residual = crosswalk.get("residual_groups")
    contributions = crosswalk.get("program_contributions")
    if not isinstance(entities, list) or len(entities) != 218:
        errors.append("channel crosswalk must contain 218 provisional person entities")
    if not isinstance(edges, list) or len(edges) != 294:
        errors.append("channel crosswalk must contain 294 proposed appearance edges")
    elif len({(edge.get("person_id"), edge.get("intake_group_id")) for edge in edges}) != len(edges):
        errors.append("channel crosswalk appearance edges must be unique")
    if not isinstance(residual, list) or len(residual) != 16:
        errors.append("channel crosswalk must retain 16 residual resolution groups")
    if not isinstance(contributions, list):
        errors.append("channel crosswalk program_contributions must be a list")
    policies = crosswalk.get("policies", {})
    for field in (
        "people_are_models",
        "appearance_implies_program",
        "contributor_presence_implies_episode_program",
        "title_signal_is_source_native_dossier",
        "unknown_means_weak",
    ):
        if policies.get(field) is not False:
            errors.append(f"channel crosswalk policies.{field} must be false")
    batching = crosswalk.get("administrative_batching", {})
    if batching.get("scientific_priority_conveyed") is not False:
        errors.append("channel crosswalk batches must convey no scientific priority")
    batches = batching.get("batches")
    if not isinstance(batches, list) or len(batches) != 16:
        errors.append("channel crosswalk must contain 16 neutral administrative batches")
    elif sorted(batch.get("unit_count") for batch in batches) != [14] * 6 + [15] * 10:
        errors.append("channel crosswalk batch sizes must be six 14-unit and ten 15-unit batches")


def _validate_target_dossier(dossier: dict[str, Any], errors: list[str]) -> None:
    if dossier.get("schema_version") != TARGET_DOSSIER_SCHEMA_VERSION:
        errors.append(f"target model dossier schema_version must be {TARGET_DOSSIER_SCHEMA_VERSION!r}")
    comparison = dossier.get("comparison_use", {})
    if comparison.get("people_are_ranked") is not False:
        errors.append("target model dossier must not rank people")
    if comparison.get("joshua_is_automatic_baseline_winner") is not False:
        errors.append("Joshua cannot be an automatic baseline winner")
    root = dossier.get("operational_root_and_open_ontology", {})
    if root.get("unique_ontological_root_earned") is not False:
        errors.append("target model dossier must not claim a unique ontological root")
    execution = dossier.get("campaign_execution_state", {})
    if execution.get("scientific_campaign_has_run") is not False:
        errors.append("target dossier cannot claim the proposed scientific campaign has run")
    modules = dossier.get("joshua_program_modules")
    if not isinstance(modules, list) or len(modules) != 9:
        errors.append("target dossier must preserve nine separately scoped Joshua program modules")
    elif len({module.get("program_id") for module in modules}) != len(modules):
        errors.append("target dossier program module ids must be unique")
    surfaces = dossier.get("comparison_surfaces")
    if not isinstance(surfaces, list) or not surfaces:
        errors.append("target dossier comparison_surfaces must be a nonempty list")
    elif len({surface.get("surface_id") for surface in surfaces}) != len(surfaces):
        errors.append("target dossier comparison surface ids must be unique")
    evidence = dossier.get("evidence_registry")
    if not isinstance(evidence, list) or not evidence:
        errors.append("target dossier evidence_registry must be a nonempty list")
    elif any("does_not_support" not in receipt for receipt in evidence):
        errors.append("every target evidence entry must state what it does not support")


def _validate_external_dossier_contract(contract: dict[str, Any], errors: list[str]) -> None:
    if contract.get("schema_version") != EXTERNAL_DOSSIER_SCHEMA_VERSION:
        errors.append(f"external dossier schema_version must be {EXTERNAL_DOSSIER_SCHEMA_VERSION!r}")
    if contract.get("people_are_ranked") is not False:
        errors.append("external dossier contract must not rank people")
    if contract.get("ranked_unit") != "program_version_x_role_x_question_x_evidence_packet":
        errors.append("external dossier contract ranked unit is incorrect")
    gates = set(contract.get("eligibility_gates", []))
    required = {
        "primary_source_packet_complete",
        "native_model_reconstructed_without_joshua_vocabulary",
        "native_baseline_reproduction_passed_or_documented_nonexecutable",
        "missing_evidence_not_imputed_as_zero",
        "no_fame_familiarity_episode_count_or_prior_work_input",
        "comparison_pool_receipt_complete",
    }
    if missing := required - gates:
        errors.append(f"external dossier contract eligibility_gates missing {sorted(missing)}")
    unknown = contract.get("unknown_policy", {})
    if unknown.get("unprocessed") != "UNRANKED":
        errors.append("external dossier contract must keep unprocessed programs UNRANKED")


def _validate_native_source_index(
    index: dict[str, Any], base_dir: Path, errors: list[str]
) -> None:
    if index.get("schema_version") != NATIVE_SOURCE_INDEX_SCHEMA_VERSION:
        errors.append(
            f"native source index schema_version must be {NATIVE_SOURCE_INDEX_SCHEMA_VERSION!r}"
        )
    if index.get("status") != "SOURCE_NATIVE_INDEX_NOT_A_RANKING":
        errors.append("native source index must remain explicitly non-ranking")
    policies = index.get("policies", {})
    if policies.get("people_are_ranked") is not False:
        errors.append("native source index must not rank people")
    if policies.get("unknown_is_zero") is not False:
        errors.append("native source index cannot score unknown evidence as zero")
    if policies.get("source_native_baseline_required_before_repair") is not True:
        errors.append("native source index must require a source-native baseline before repair")

    cards = index.get("cards")
    if not isinstance(cards, list) or not cards:
        errors.append("native source index cards must be a nonempty list")
        return
    card_ids = [card.get("card_id") for card in cards]
    if None in card_ids or len(set(card_ids)) != len(card_ids):
        errors.append("native source index card ids must be present and unique")
    if any(card.get("ranking_eligible") is not False for card in cards):
        errors.append("native source cards cannot be ranking-eligible before baseline reproduction")
    if any(not card.get("primary_sources") for card in cards):
        errors.append("every indexed source-native card must retain a primary-source lead")
    for card in cards:
        if card.get("primary_source_count") != len(card.get("primary_sources", [])):
            errors.append(f"native source card {card.get('card_id')!r} source count mismatch")
        for source in card.get("primary_sources", []):
            if not str(source.get("url", "")).startswith(("https://", "http://")):
                errors.append(f"native source card {card.get('card_id')!r} has invalid source URL")

    batches = index.get("source_batches")
    if not isinstance(batches, list) or not batches:
        errors.append("native source index must identify source batches")
        return
    indexed_batch_files = {batch.get("file") for batch in batches}
    actual_batch_files = {path.name for path in base_dir.glob("native_source_cards_batch_*.json")}
    if indexed_batch_files != actual_batch_files:
        errors.append("native source index batch file set is stale")
    batch_card_total = 0
    raw_ids: list[str] = []
    resolution_total = 0
    fully_resolved_batch_ids: set[str] = set()
    resolution_units: list[str] = []
    for batch in batches:
        filename = batch.get("file")
        path = base_dir / str(filename)
        try:
            packet = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"cannot read native source batch {path}: {exc}")
            continue
        raw_cards = packet.get("cards")
        if not isinstance(raw_cards, list):
            errors.append(f"native source batch {filename} cards must be a list")
            continue
        if batch.get("card_count") != len(raw_cards):
            errors.append(f"native source batch {filename} card count mismatch")
        batch_card_total += len(raw_cards)
        raw_resolutions = packet.get("resolutions", [])
        if not isinstance(raw_resolutions, list):
            errors.append(f"native source batch {filename} resolutions must be a list")
            raw_resolutions = []
        if batch.get("resolution_record_count") != len(raw_resolutions):
            errors.append(f"native source batch {filename} resolution count mismatch")
        resolution_total += len(raw_resolutions)
        administrative = packet.get("administrative_batch", {})
        if isinstance(administrative, str):
            administrative = {"batch_id": administrative}
        if not isinstance(administrative, dict):
            administrative = {}
        unit_count = administrative.get("unit_count")
        batch_id = administrative.get("batch_id")
        if raw_resolutions and isinstance(unit_count, int):
            if len(raw_resolutions) != unit_count:
                errors.append(f"native source batch {filename} administrative census is incomplete")
            elif batch_id:
                fully_resolved_batch_ids.add(batch_id)
        for record in raw_resolutions:
            unit = (
                record.get("administrative_unit") or record.get("unit_id")
                if isinstance(record, dict)
                else None
            )
            if not unit:
                errors.append(f"native source batch {filename} has an invalid resolution record")
            else:
                resolution_units.append(unit)
        for raw in raw_cards:
            raw_id = raw.get("program_id") or raw.get("id") or raw.get("card_id")
            if not raw_id:
                errors.append(f"native source batch {filename} contains a card without an id")
            else:
                raw_ids.append(raw_id)
            if raw.get("ranking_eligible") is not False:
                errors.append(f"native source batch {filename} contains a rank-eligible card")
    if len(set(raw_ids)) != len(raw_ids):
        errors.append("native source batch card ids must be globally unique")
    if len(set(resolution_units)) != len(resolution_units):
        errors.append("native source administrative units must not be resolved twice")

    coverage = index.get("coverage", {})
    if coverage.get("source_batch_count") != len(batches):
        errors.append("native source index source_batch_count mismatch")
    if coverage.get("source_card_count") != len(cards) or len(cards) != batch_card_total:
        errors.append("native source index source_card_count mismatch")
    if coverage.get("channel_provisional_person_count") != 218:
        errors.append("native source index must reconcile to 218 provisional channel people")
    matched = coverage.get("channel_people_with_any_source_card_link")
    unmatched = coverage.get("channel_people_without_any_source_card_link")
    if not isinstance(matched, int) or not isinstance(unmatched, int) or matched + unmatched != 218:
        errors.append("native source index person coverage must sum to 218")
    if coverage.get("ranking_eligible_card_count") != 0:
        errors.append("native source index cannot report ranking-eligible cards")
    if coverage.get("administrative_resolution_record_count") != resolution_total:
        errors.append("native source index administrative resolution count mismatch")
    if coverage.get("fully_resolved_administrative_batch_count") != len(
        fully_resolved_batch_ids
    ):
        errors.append("native source index fully resolved batch count mismatch")


def validate(
    payload: dict[str, Any],
    *,
    base_dir: Path | None = None,
    registry_payload: dict[str, Any] | None = None,
    intake_payload: dict[str, Any] | None = None,
    crosswalk_payload: dict[str, Any] | None = None,
    target_dossier_payload: dict[str, Any] | None = None,
    external_dossier_payload: dict[str, Any] | None = None,
    native_source_index_payload: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    base_dir = base_dir or Path(__file__).resolve().parent
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION!r}")
    if payload.get("root_primitive") != "constrained_distinguishability":
        errors.append("root_primitive must remain constrained_distinguishability")
    if payload.get("root_primitive_scope") != "CURRENT_OPERATIONAL_ASSUMPTION":
        errors.append("root_primitive must be scoped as a current operational assumption")
    if payload.get("root_primitive_is_unique_ontology") is not False:
        errors.append("root_primitive must not be promoted to a unique ontology")
    if payload.get("target_model_is_split_and_defeasible") is not True:
        errors.append("target model must remain split into defeasible program modules")
    if payload.get("scientific_campaign_has_run") is not False:
        errors.append("v0.3 cannot claim that the proposed scientific campaign has run")
    if payload.get("comparison_cohort_closed") is not False:
        errors.append("v0.3 comparison cohort remains open")
    if payload.get("registry_open") is not True:
        errors.append("candidate registry must remain open")
    if payload.get("completeness_claimed") is not False:
        errors.append("finite intake must not claim a complete contender field")
    if payload.get("scientific_authority") is not False:
        errors.append("campaign packet must not claim scientific authority")
    if payload.get("canonical_gate_order") is not False:
        errors.append("gate order must remain a proposal population")
    if payload.get("canonical_gate_decomposition") is not False:
        errors.append("gate decomposition must remain a proposal population")
    if payload.get("receipts_append_only") is not True:
        errors.append("evidence receipts must be append-only")
    if payload.get("conclusions_defeasible") is not True:
        errors.append("conclusions must remain defeasible")
    if payload.get("familiarity_is_provenance_only") is not True:
        errors.append("familiarity must be provenance only")
    if payload.get("adapter_drafts_are_ranked") is not False:
        errors.append("adapter drafts must not be ranked or selected")
    if "seed_campaigns_only" in payload or "campaigns" in payload:
        errors.append("legacy seed/active campaign fields are forbidden")

    outputs = payload.get("shared_adapter_output")
    if not isinstance(outputs, list):
        errors.append("shared_adapter_output must be a list")
    else:
        missing_outputs = REQUIRED_OUTPUTS - set(outputs)
        if missing_outputs:
            errors.append(f"shared_adapter_output missing {sorted(missing_outputs)}")
        duplicates = _duplicates(outputs)
        if duplicates:
            errors.append(f"shared_adapter_output has duplicates {duplicates}")

    registry = _read_linked_json(payload, "candidate_registry", base_dir, registry_payload, errors)
    intake = _read_linked_json(payload, "channel_intake", base_dir, intake_payload, errors)
    crosswalk = _read_linked_json(payload, "channel_crosswalk", base_dir, crosswalk_payload, errors)
    target_dossier = _read_linked_json(payload, "target_model_dossier", base_dir, target_dossier_payload, errors)
    external_dossier = _read_linked_json(
        payload, "external_program_dossier_contract", base_dir, external_dossier_payload, errors
    )
    native_source_index = _read_linked_json(
        payload, "native_source_card_index", base_dir, native_source_index_payload, errors
    )
    cards = _validate_registry(registry, errors) if registry is not None else {}
    if intake is not None:
        _validate_intake(intake, errors)
    if crosswalk is not None:
        _validate_crosswalk(crosswalk, errors)
    if target_dossier is not None:
        _validate_target_dossier(target_dossier, errors)
    if external_dossier is not None:
        _validate_external_dossier_contract(external_dossier, errors)
    if native_source_index is not None:
        _validate_native_source_index(native_source_index, base_dir, errors)

    drafts = payload.get("adapter_drafts")
    if not isinstance(drafts, list):
        errors.append("adapter_drafts must be a list")
    else:
        seen_ids: list[str] = []
        for index, draft in enumerate(drafts):
            prefix = f"adapter_drafts[{index}]"
            if not isinstance(draft, dict):
                errors.append(f"{prefix} must be an object")
                continue
            missing = REQUIRED_DRAFT_KEYS - set(draft)
            if missing:
                errors.append(f"{prefix} missing {sorted(missing)}")
                continue
            seen_ids.append(draft["id"])
            if draft["candidate_id"] not in cards:
                errors.append(f"{prefix}.candidate_id is absent from registry")
            if draft.get("selection_status") != "UNSELECTED":
                errors.append(f"{prefix} must remain UNSELECTED without a selection receipt")
            for field in ("selection_receipt", "dossier_receipt", "baseline_receipt", "eligibility_receipt"):
                if draft.get(field) is not None:
                    errors.append(f"{prefix}.{field} must be null while unselected")
            if draft.get("source_native_baseline_required") is not True:
                errors.append(f"{prefix} must require a source-native baseline")
            if draft.get("selection_confers_priority") is not False:
                errors.append(f"{prefix} draft existence must convey no priority")
            if str(draft.get("claim_ceiling", "")).lower() in FORBIDDEN_CEILINGS:
                errors.append(f"{prefix}.claim_ceiling overclaims scientific status")
        duplicates = _duplicates(seen_ids)
        if duplicates:
            errors.append(f"adapter draft ids are not unique: {duplicates}")

    selected = payload.get("selected_campaigns")
    if not isinstance(selected, list):
        errors.append("selected_campaigns must be a list")
    else:
        for index, campaign in enumerate(selected):
            prefix = f"selected_campaigns[{index}]"
            if not isinstance(campaign, dict):
                errors.append(f"{prefix} must be an object")
                continue
            missing = REQUIRED_SELECTION_KEYS - set(campaign)
            if missing:
                errors.append(f"{prefix} missing {sorted(missing)}")
                continue
            card = cards.get(campaign["candidate_id"])
            if card is None:
                errors.append(f"{prefix}.candidate_id is absent from registry")
                continue
            if card.get("ranking_eligible") is not True:
                errors.append(f"{prefix} candidate is not ranking-eligible")
            for field in ("dossier_receipt", "baseline_receipt", "eligibility_receipt", "selection_receipt"):
                if not campaign.get(field):
                    errors.append(f"{prefix}.{field} is required")
            pool = campaign.get("comparison_pool_ids")
            if not isinstance(pool, list) or not pool or campaign["candidate_id"] not in pool:
                errors.append(f"{prefix}.comparison_pool_ids must include the selected candidate")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "packet",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("campaigns_v0_3.json"),
    )
    args = parser.parse_args()
    payload = json.loads(args.packet.read_text(encoding="utf-8"))
    errors = validate(payload, base_dir=args.packet.resolve().parent)
    registry_path = args.packet.resolve().parent / payload.get("candidate_registry", "")
    ranking_eligible_count = 0
    if registry_path.is_file():
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        ranking_eligible_count = registry.get("ranking_eligible_count", 0)
    native_index_path = args.packet.resolve().parent / payload.get(
        "native_source_card_index", ""
    )
    native_coverage: dict[str, Any] = {}
    if native_index_path.is_file():
        native_index = json.loads(native_index_path.read_text(encoding="utf-8"))
        native_coverage = native_index.get("coverage", {})
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "packet": str(args.packet),
        "adapter_draft_count": len(payload.get("adapter_drafts", [])),
        "selected_campaign_count": len(payload.get("selected_campaigns", [])),
        "ranking_eligible_count": ranking_eligible_count,
        "source_native_starting_card_count": native_coverage.get("source_card_count", 0),
        "channel_people_with_source_card_link": native_coverage.get(
            "channel_people_with_any_source_card_link", 0
        ),
        "fully_resolved_administrative_batch_count": native_coverage.get(
            "fully_resolved_administrative_batch_count", 0
        ),
        "valid": not errors,
        "errors": errors,
        "claim_ceiling": "process_contract_validation_only",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
