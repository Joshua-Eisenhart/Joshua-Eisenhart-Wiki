#!/usr/bin/env python3

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from validate_campaign import validate


PACKET = Path(__file__).with_name("campaigns_v0_2.json")


class CampaignContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(PACKET.read_text(encoding="utf-8"))

    def test_shipped_packet_is_valid(self) -> None:
        self.assertEqual(validate(copy.deepcopy(self.payload)), [])

    def test_fixed_gate_order_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["canonical_gate_order"] = True
        self.assertTrue(any("gate order" in error for error in validate(payload)))

    def test_closed_registry_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["registry_open"] = False
        self.assertTrue(any("registry" in error for error in validate(payload)))

    def test_seed_list_cannot_claim_completeness(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["completeness_claimed"] = True
        self.assertTrue(any("complete contender field" in error for error in validate(payload)))

    def test_missing_source_baseline_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["campaigns"][0]["source_native_baseline"] = False
        self.assertTrue(any("source-native baseline" in error for error in validate(payload)))

    def test_unfalsifiable_campaign_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["campaigns"][0]["kill_criteria"] = []
        self.assertTrue(any("kill_criteria" in error for error in validate(payload)))

    def test_canonical_claim_ceiling_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["campaigns"][0]["claim_ceiling"] = "canon"
        self.assertTrue(any("overclaims" in error for error in validate(payload)))


if __name__ == "__main__":
    unittest.main()
