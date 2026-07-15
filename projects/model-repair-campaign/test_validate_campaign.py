#!/usr/bin/env python3

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from validate_campaign import validate


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "campaigns_v0_3.json"
REGISTRY = ROOT / "candidate_registry_v0_3.json"
INTAKE = ROOT / "channel_intake_v0_3.json"


class CampaignContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(PACKET.read_text(encoding="utf-8"))
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.intake = json.loads(INTAKE.read_text(encoding="utf-8"))

    def check(
        self,
        payload: dict | None = None,
        registry: dict | None = None,
        intake: dict | None = None,
    ) -> list[str]:
        return validate(
            copy.deepcopy(payload if payload is not None else self.payload),
            base_dir=ROOT,
            registry_payload=copy.deepcopy(registry if registry is not None else self.registry),
            intake_payload=copy.deepcopy(intake if intake is not None else self.intake),
        )

    def test_shipped_packet_is_valid_with_zero_selected_campaigns(self) -> None:
        self.assertEqual(self.check(), [])
        self.assertEqual(self.payload["selected_campaigns"], [])
        self.assertEqual(self.registry["ranking_eligible_count"], 0)

    def test_fixed_gate_order_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["canonical_gate_order"] = True
        self.assertTrue(any("gate order" in error for error in self.check(payload=payload)))

    def test_closed_registry_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["registry_open"] = False
        self.assertTrue(any("registry" in error for error in self.check(registry=registry)))

    def test_finite_intake_cannot_claim_field_completeness(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["completeness_claimed"] = True
        self.assertTrue(any("complete contender field" in error for error in self.check(payload=payload)))

    def test_user_named_provenance_cannot_make_card_eligible(self) -> None:
        registry = copy.deepcopy(self.registry)
        card = next(card for card in registry["candidates"] if card["discovery_provenance"] == "user_named_example")
        card["ranking_eligible"] = True
        registry["ranking_eligible_count"] = 1
        self.assertTrue(any("dossier and baseline receipts" in error for error in self.check(registry=registry)))

    def test_ineligible_card_cannot_enter_frontier(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["candidates"][0]["frontier_receipts"] = ["manual-frontier"]
        self.assertTrue(any("cannot enter a frontier" in error for error in self.check(registry=registry)))

    def test_selected_campaign_requires_full_receipts(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["selected_campaigns"] = [{"id": "manual", "candidate_id": "friston_fep"}]
        self.assertTrue(any("missing" in error for error in self.check(payload=payload)))

    def test_selected_campaign_requires_complete_comparison_pool(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["selected_campaigns"] = [{
            "id": "manual",
            "candidate_id": "friston_fep",
            "dossier_receipt": "d",
            "baseline_receipt": "b",
            "eligibility_receipt": "e",
            "selection_receipt": "s",
            "comparison_pool_ids": [],
            "declared_role": "competitor",
            "question_packet": "q",
            "matched_control": "c",
            "held_out_test": "h",
            "kill_criteria": ["k"],
        }]
        errors = self.check(payload=payload)
        self.assertTrue(any("not ranking-eligible" in error for error in errors))
        self.assertTrue(any("comparison_pool_ids" in error for error in errors))

    def test_manual_priority_labels_are_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["priority_frontiers"] = []
        registry["candidates"][0]["status"] = "priority_dossier"
        errors = self.check(registry=registry)
        self.assertTrue(any("priority_frontiers" in error for error in errors))
        self.assertTrue(any("legacy rank/status" in error for error in errors))

    def test_legacy_seed_fields_are_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["seed_campaigns_only"] = True
        self.assertTrue(any("legacy seed" in error for error in self.check(payload=payload)))

    def test_all_bias_controls_are_required(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["forbidden_ranking_inputs"].remove("user_naming_order")
        self.assertTrue(any("user_naming_order" in error for error in self.check(registry=registry)))


if __name__ == "__main__":
    unittest.main()
