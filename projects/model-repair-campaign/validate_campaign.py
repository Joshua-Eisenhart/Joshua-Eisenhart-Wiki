#!/usr/bin/env python3
"""Validate neutral intake, evidence eligibility, and campaign selection v0.3.

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


def validate(
    payload: dict[str, Any],
    *,
    base_dir: Path | None = None,
    registry_payload: dict[str, Any] | None = None,
    intake_payload: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    base_dir = base_dir or Path(__file__).resolve().parent
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION!r}")
    if payload.get("root_primitive") != "constrained_distinguishability":
        errors.append("root_primitive must remain constrained_distinguishability")
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
    cards = _validate_registry(registry, errors) if registry is not None else {}
    if intake is not None:
        _validate_intake(intake, errors)

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
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "packet": str(args.packet),
        "adapter_draft_count": len(payload.get("adapter_drafts", [])),
        "selected_campaign_count": len(payload.get("selected_campaigns", [])),
        "ranking_eligible_count": ranking_eligible_count,
        "valid": not errors,
        "errors": errors,
        "claim_ceiling": "process_contract_validation_only",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
