#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# ///
"""Enrich a GP CI/CD config file with computed values (stackDir, concurrencyGroup, appName)."""

import json
import os
import sys


def enrich_config(config: dict, app_name: str, stack_name: str) -> dict:
    if app_name:
        config["appName"] = app_name

    for env in ("dev", "prod"):
        if env not in config:
            continue

        if stack_name:
            config[env]["stackDir"] = f"{config[env]['infrastructureRoot']}/{stack_name}"

        if config.get("monorepo"):
            config[env]["concurrencyGroup"] = f"{config[env]['name']}-{app_name}"
        else:
            config[env]["concurrencyGroup"] = config[env]["name"]

    return config


def main() -> None:
    config_file = os.environ.get("CONFIG_FILE", "")
    app_name = os.environ.get("APP_NAME", "")
    stack_name = os.environ.get("STACK_NAME", "")

    if not config_file:
        print("::error::CONFIG_FILE environment variable is not set", file=sys.stderr)
        sys.exit(1)

    with open(config_file) as f:
        config = json.load(f)

    result = enrich_config(config, app_name, stack_name)
    print(json.dumps(result, separators=(",", ":")))


if __name__ == "__main__":
    main()
