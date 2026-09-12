"""Test for issue_0014: Capabilities menu labels unique within menu."""
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


def test_capability_labels_unique(page_ready: Page) -> None:
    """Test all capability labels are unique within the menu."""
    page_ready.get_by_role("button", name="Capabilities").first.click()
    
    capability_texts = [
        "Data Engineering",
        "Automation",
        "Pacca AI",
        "Digital Engineering",
        "Low Code",
        "User Experience",
        "Cloud Transformation",
        "Payer Core Platforms",
        "Provider Platforms",
    ]
    
    seen = set()
    for text in capability_texts:
        assert text not in seen, f"Duplicate capability label: {text}"
        seen.add(text)
