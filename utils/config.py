"""Read runtime configuration for the public Emids test target."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


BASE_URL = os.environ.get("BASE_URL", "https://www.emids.com")
TEST_USERNAME = os.environ.get("TEST_USERNAME") or None
TEST_PASSWORD = os.environ.get("TEST_PASSWORD") or None


def has_credentials() -> bool:
    return bool(TEST_USERNAME and TEST_PASSWORD)
