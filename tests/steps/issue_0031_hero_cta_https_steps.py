"""Step definitions for issue_0031: Hero CTA uses HTTPS canonical URL."""
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


@then("Hero CTA uses HTTPS canonical URL")
def hero_cta_uses_https(page: Page) -> None:
    """Verify Hero CTA uses HTTPS canonical URL."""
    hero_cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    href = hero_cta.get_attribute("href")
    assert href is not None, "Hero CTA should have href"
    assert href.startswith("https://"), f"Hero CTA should use HTTPS: {href}"
