"""Test for issue_0049: Capability labels match navigation taxonomy."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_capability_labels_match_taxonomy(page_ready: Page) -> None:
    """Test capability labels match navigation taxonomy."""
    expected_labels = [
        "Data Engineering",
        "Automation",
        "Pacca AI",
        "Digital Engineering",
        "Low-Code",
        "User Experience",
        "Cloud Transformation",
        "Payer Core Platforms",
        "Provider Platforms",
    ]
    
    for label in expected_labels:
        label_elem = page_ready.get_by_role("heading", name=label)
        expect(label_elem).to_be_visible()
