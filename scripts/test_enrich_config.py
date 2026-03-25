#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pytest"]
# ///
"""Tests for enrich_config.py."""

import json
from pathlib import Path

from enrich_config import enrich_config

TESTDATA = Path(__file__).parent / "testdata"


def test_enrich_full_config():
    config = json.loads((TESTDATA / "full.json").read_text())
    expected = json.loads((TESTDATA / "full-expected.json").read_text())
    result = enrich_config(config, app_name="my-app", stack_name="app-example")
    assert result == expected


def test_enrich_only_dev_config():
    config = json.loads((TESTDATA / "only-dev.json").read_text())
    expected = json.loads((TESTDATA / "only-dev-expected.json").read_text())
    result = enrich_config(config, app_name="my-app", stack_name="app-example")
    assert result == expected
