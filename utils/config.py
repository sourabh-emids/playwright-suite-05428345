"""Reads the environment this suite runs against.

Fails loudly and immediately when BASE_URL is unset -- a suite that silently
ran against an empty base URL would fail every test with a confusing
low-level connection error instead of one clear one, here, at collection
time.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def _require(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"{name} is not set. Copy .env.example to .env and fill it in, "
            "or export it in your shell/CI before running pytest."
        )
    return value


BASE_URL = _require("BASE_URL")
TEST_USERNAME = os.environ.get("TEST_USERNAME") or None
TEST_PASSWORD = os.environ.get("TEST_PASSWORD") or None


def has_credentials() -> bool:
    return bool(TEST_USERNAME and TEST_PASSWORD)
