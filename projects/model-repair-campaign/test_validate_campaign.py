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
CROSSWALK = ROOT / "channel_crosswalk_v0_4.json"
TARGET_DOSSIER = ROOT / "joshua_model_dossier_v0_1.json"
EXTERNAL_DOSSIER = ROOT / "external_program_dossier_contract_v0_1.json"
NATIVE_SOURCE_INDEX = ROOT / "native_source_card_index_v0_1.json"


class CampaignContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(PACKET.read_text(encoding="utf-8"))
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.intake = json.loads(INTAKE.read_text(encoding="utf-8"))
        cls.crosswalk = json.loads(CROSSWALK.read_text(encoding="utf-8"))
        cls.target_dossier = json.loads(TARGET_DOSSIER.read_text(encoding="utf-8"))
        cls.external_dossier = json.loads(EXTERNAL_DOSSIER.read_text(encoding="utf-8"))
        cls.native_source_index = json.loads(NATIVE_SOURCE_INDEX.read_text(encoding="utf-8"))

    def check(
        self,
        payload: dict | None = None,
        registry: dict | None = None,
        intake: dict | None = None,
        crosswalk: dict | None = None,
        target_dossier: dict | None = None,
        external_dossier: dict | None = None,
        native_source_index: dict | None = None,
    ) -> list[str]:
        return validate(
            copy.deepcopy(payload if payload is not None else self.payload),
            base_dir=ROOT,
            registry_payload=copy.deepcopy(registry if registry is not None else self.registry),
            intake_payload=copy.deepcopy(intake if intake is not None else self.intake),
            crosswalk_payload=copy.deepcopy(crosswalk if crosswalk is not None else self.crosswalk),
            target_dossier_payload=copy.deepcopy(
                target_dossier if target_dossier is not None else self.target_dossier
            ),
            external_dossier_payload=copy.deepcopy(
                external_dossier if external_dossier is not None else self.external_dossier
            ),
            native_source_index_payload=copy.deepcopy(
                native_source_index
                if native_source_index is not None
                else self.native_source_index
            ),
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

    def test_operational_root_cannot_be_promoted_to_unique_ontology(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["root_primitive_is_unique_ontology"] = True
        self.assertTrue(any("unique ontology" in error for error in self.check(payload=payload)))

    def test_target_dossier_cannot_claim_completed_scientific_campaign(self) -> None:
        dossier = copy.deepcopy(self.target_dossier)
        dossier["campaign_execution_state"]["scientific_campaign_has_run"] = True
        self.assertTrue(any("scientific campaign" in error for error in self.check(target_dossier=dossier)))

    def test_target_evidence_requires_negative_claim_ceiling(self) -> None:
        dossier = copy.deepcopy(self.target_dossier)
        dossier["evidence_registry"][0].pop("does_not_support")
        self.assertTrue(any("does not support" in error for error in self.check(target_dossier=dossier)))

    def test_crosswalk_cannot_turn_title_signal_into_program(self) -> None:
        crosswalk = copy.deepcopy(self.crosswalk)
        crosswalk["policies"]["title_signal_is_source_native_dossier"] = True
        self.assertTrue(any("title_signal" in error for error in self.check(crosswalk=crosswalk)))

    def test_external_dossier_keeps_unprocessed_programs_unranked(self) -> None:
        contract = copy.deepcopy(self.external_dossier)
        contract["unknown_policy"]["unprocessed"] = "WEAK"
        self.assertTrue(any("UNRANKED" in error for error in self.check(external_dossier=contract)))

    def test_source_native_card_cannot_be_made_rankable_by_research_alone(self) -> None:
        index = copy.deepcopy(self.native_source_index)
        index["cards"][0]["ranking_eligible"] = True
        index["coverage"]["ranking_eligible_card_count"] = 1
        errors = self.check(native_source_index=index)
        self.assertTrue(any("cannot be ranking-eligible" in error for error in errors))

    def test_source_native_index_requires_primary_source_leads(self) -> None:
        index = copy.deepcopy(self.native_source_index)
        index["cards"][0]["primary_sources"] = []
        index["cards"][0]["primary_source_count"] = 0
        self.assertTrue(
            any("primary-source lead" in error for error in self.check(native_source_index=index))
        )

    def test_source_native_person_coverage_must_reconcile(self) -> None:
        index = copy.deepcopy(self.native_source_index)
        index["coverage"]["channel_people_without_any_source_card_link"] -= 1
        self.assertTrue(any("sum to 218" in error for error in self.check(native_source_index=index)))


if __name__ == "__main__":
    unittest.main()
