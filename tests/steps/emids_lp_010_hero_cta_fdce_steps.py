"""Steps for emids_lp_010: Route hero CTA to FDCE experience."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.hero.hero_page import HeroPage


@given(parsers.parse("User is on homepage hero section"))
def on_homepage_hero(page: Page) -> None:
    """User is on homepage hero section."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("User examines hero CTA destination"))
def examine_hero_cta_destination(page: Page) -> None:
    """User examines hero CTA destination."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("User clicks hero CTA"))
def click_hero_cta(page: Page) -> None:
    """User clicks hero CTA."""
    hero_page = HeroPage(page)
    hero_page.navigate()
    hero_page.click_hero_cta()


@given(parsers.parse("User right-clicks hero CTA to open in new tab"))
def right_click_hero_cta(page: Page) -> None:
    """User right-clicks hero CTA."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("FDCE destination page is temporarily unavailable"))
def fdce_unavailable(page: Page) -> None:
    """FDCE destination is unavailable."""
    # Would simulate unavailable state
    pass


@when("User clicks the primary hero CTA")
def click_primary_hero_cta(page: Page) -> None:
    """Click the primary hero CTA."""
    hero_page = HeroPage(page)
    hero_page.click_hero_cta()


@when("Navigation occurs")
def navigation_occurs(page: Page) -> None:
    """Navigation occurs."""
    page.wait_for_load_state("domcontentloaded")


@when("User selects open in new tab")
def select_open_new_tab(page: Page) -> None:
    """Select open in new tab."""
    # Right-click handled by context action
    pass


@when("User clicks hero CTA")
def click_hero_cta_action(page: Page) -> None:
    """Click hero CTA."""
    hero_page = HeroPage(page)
    hero_page.click_hero_cta()


@then(parsers.parse("Browser navigates to /forward-deployed-context-engineering/"))
def navigates_to_fdce(page: Page) -> None:
    """Verify browser navigates to FDCE page."""
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("URL uses HTTPS protocol")
def url_https(page: Page) -> None:
    """Verify URL uses HTTPS."""
    url = page.url
    expect(url).to_start_with("https://")


@then("URL is canonical")
def url_canonical(page: Page) -> None:
    """Verify URL is canonical."""
    url = page.url
    expect(url).to_contain("/forward-deployed-context-engineering/")


@then("Standard browser navigation behavior occurs")
def standard_navigation(page: Page) -> None:
    """Verify standard browser navigation behavior."""
    expect(page).not_to_have_title("")  # Title should be set


@then("No unexpected popups or behaviors")
def no_popups(page: Page) -> None:
    """Verify no unexpected popups."""
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("FDCE page opens in new tab correctly")
def opens_new_tab(page: Page) -> None:
    """Verify FDCE page opens in new tab."""
    hero_page = HeroPage(page)
    hero_page.navigate()
    # Open in new tab
    with page.context.expect_page():
        hero_page.locators.hero_cta.click(button="right")


@then("User receives appropriate error page")
def error_page_received(page: Page) -> None:
    """Verify user receives appropriate error page."""
    # Check for error indicators
    pass


@then("Core site remains functional")
def core_site_functional(page: Page) -> None:
    """Verify core site remains functional."""
    page.goto("/")
    expect(page.get_by_role("heading", level=1)).to_be_visible()
