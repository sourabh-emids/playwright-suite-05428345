"""AI, Engineering, and Platforms capability cards with valid destinations."""
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


@then("AI capability card has valid destination")
def ai_capability_valid_destination(page: Page) -> None:
    """Verify AI capability card has valid destination."""
    pacca_link = page.get_by_role("link", name="Pacca AI")
    href = pacca_link.get_attribute("href")
    assert href is not None and "/pacca-ai/" in href, "Pacca AI should link to /pacca-ai/"


@then("Engineering capability card has valid destination")
def engineering_capability_valid_destination(page: Page) -> None:
    """Verify Engineering capability card has valid destination."""
    digital_eng_link = page.get_by_role("link", name="Digital Engineering")
    href = digital_eng_link.get_attribute("href")
    assert href is not None and "/capabilities/digital-engineering/" in href, "Should link to digital engineering"


@then("Platforms capability card has valid destination")
def platforms_capability_valid_destination(page: Page) -> None:
    """Verify Platforms capability card has valid destination."""
    payer_core_link = page.get_by_role("link", name="Payer Core Platforms")
    href = payer_core_link.get_attribute("href")
    assert href is not None and "/capabilities/payer-core-platforms/" in href, "Should link to payer core platforms"
