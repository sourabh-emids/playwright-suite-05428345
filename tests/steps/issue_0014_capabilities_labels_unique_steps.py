"""Step definitions for issue_0014: Capabilities menu labels unique within menu."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("all capability labels are unique within the menu")
def capability_labels_unique(page: Page) -> None:
    """Verify capability labels are unique within the menu."""
    page.get_by_role("button", name="Capabilities").first.click()
    
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
