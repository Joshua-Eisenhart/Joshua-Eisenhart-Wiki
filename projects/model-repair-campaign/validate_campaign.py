#!/usr/bin/env python3
"""Validate the v0.1 external-model repair campaign contract.

This is a process check, not a scientific verdict. It prevents a campaign from
quietly installing a source model, a fixed gate order, or an unfalsifiable
"repair" before source-native adapters and controls have run.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "external-model-repair-campaign/0.1"
REQUIRED_CAMPAIGN_KEYS = {
    "id",
    "source_program",
    "claim_ceiling",
    "source_native_baseline",
    "candidate_axes",
    "demand_families",
    "weakness_hypotheses",
    "controls",
    "kill_criteria",
    "first_experiment",
}
REQUIRED_OUTPUTS = {
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
FORBIDDEN_CEILINGS = {"canon", "canonical", "theorem", "theory_admitted"}


def _duplicates(values: list[str]) -> list[str]:
    return sorted({value for value in values if values.count(value) > 1})


def validate(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION!r}")
    if payload.get("root_primitive") != "constrained_distinguishability":
        errors.append("root_primitive must remain constrained_distinguishability")
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

    campaigns = payload.get("campaigns")
    if not isinstance(campaigns, list) or not campaigns:
        errors.append("campaigns must be a non-empty list")
        return errors

    ids: list[str] = []
    for index, campaign in enumerate(campaigns):
        prefix = f"campaigns[{index}]"
        if not isinstance(campaign, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_CAMPAIGN_KEYS - set(campaign)
        if missing:
            errors.append(f"{prefix} missing {sorted(missing)}")
            continue

        campaign_id = campaign["id"]
        if not isinstance(campaign_id, str) or not campaign_id.strip():
            errors.append(f"{prefix}.id must be a non-empty string")
        else:
            ids.append(campaign_id)

        if campaign["source_native_baseline"] is not True:
            errors.append(f"{prefix} must reproduce a source-native baseline")
        if str(campaign["claim_ceiling"]).lower() in FORBIDDEN_CEILINGS:
            errors.append(f"{prefix}.claim_ceiling overclaims scientific status")

        minimums = {
            "candidate_axes": 2,
            "demand_families": 2,
            "weakness_hypotheses": 2,
            "controls": 4,
            "kill_criteria": 3,
        }
        for field, minimum in minimums.items():
            values = campaign[field]
            if not isinstance(values, list) or len(values) < minimum:
                errors.append(f"{prefix}.{field} requires at least {minimum} entries")
                continue
            if not all(isinstance(value, str) and value.strip() for value in values):
                errors.append(f"{prefix}.{field} entries must be non-empty strings")
            duplicates = _duplicates(values)
            if duplicates:
                errors.append(f"{prefix}.{field} has duplicates {duplicates}")

        experiment = campaign["first_experiment"]
        if not isinstance(experiment, str) or not experiment.strip():
            errors.append(f"{prefix}.first_experiment must be a non-empty string")

    duplicate_ids = _duplicates(ids)
    if duplicate_ids:
        errors.append(f"campaign ids are not unique: {duplicate_ids}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "packet",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("campaigns_v0_1.json"),
    )
    args = parser.parse_args()
    payload = json.loads(args.packet.read_text(encoding="utf-8"))
    errors = validate(payload)
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "packet": str(args.packet),
        "campaign_count": len(payload.get("campaigns", [])),
        "valid": not errors,
        "errors": errors,
        "claim_ceiling": "process_contract_validation_only",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
