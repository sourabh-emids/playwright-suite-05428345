"""Test for AI, Engineering, and Platforms capability cards."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_ai_capability_valid_destination(page_ready: Page) -> None:
    """Test AI capability card has valid destination."""
    pacca_link = page_ready.get_by_role("link", name="Pacca AI")
    href = pacca_link.get_attribute("href")
    assert href is not None and "/pacca-ai/" in href, "Pacca AI should link to /pacca-ai/"


def test_engineering_capability_valid_destination(page_ready: Page) -> None:
    """Test Engineering capability card has valid destination."""
    digital_eng_link = page_ready.get_by_role("link", name="Digital Engineering")
    href = digital_eng_link.get_attribute("href")
    assert href is not None and "/capabilities/digital-engineering/" in href, "Should link to digital engineering"


def test_platforms_capability_valid_destination(page_ready: Page) -> None:
    """Test Platforms capability card has valid destination."""
    payer_core_link = page_ready.get_by_role("link", name="Payer Core Platforms")
    href = payer_core_link.get_attribute("href")
    assert href is not None and "/capabilities/payer-core-platforms/" in href, "Should link to payer core platforms"
