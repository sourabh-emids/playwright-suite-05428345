"""Runtime configuration for the Emids public website test suite."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# This public-site suite has a safe, non-secret default while retaining an
# environment override for deployment or staging environments.
BASE_URL = os.environ.get("BASE_URL", "https://www.emids.com").rstrip("/")
TEST_USERNAME = os.environ.get("TEST_USERNAME") or None
TEST_PASSWORD = os.environ.get("TEST_PASSWORD") or None


def has_credentials() -> bool:
    """Return whether a complete optional authenticated test account exists."""
    return bool(TEST_USERNAME and TEST_PASSWORD)
