"""Capability labels match navigation taxonomy."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("capability labels match navigation taxonomy")
def capability_labels_match_taxonomy(page: Page) -> None:
    """Verify capability labels match navigation taxonomy."""
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
        label_elem = page.get_by_role("heading", name=label)
        expect(label_elem).to_be_visible()
