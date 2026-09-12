"""Hero CTA visible above page scroll on desktop."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I am on a desktop viewport")
def set_desktop_viewport(page: Page) -> None:
    """Set desktop viewport."""
    page.set_viewport_size({"width": 1280, "height": 720})


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("Hero CTA is visible above page scroll on desktop")
def hero_cta_visible_desktop(page: Page) -> None:
    """Verify Hero CTA is visible without scrolling on desktop."""
    hero_cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    expect(hero_cta).to_be_in_viewport()
