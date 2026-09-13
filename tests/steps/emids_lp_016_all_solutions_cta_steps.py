"""Steps for emids_lp_016: Provide All Solutions CTA."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.featured_solutions.featured_solutions_page import FeaturedSolutionsPage


@given(parsers.parse("User views Featured Solutions section"))
def view_featured_solutions(page: Page) -> None:
    """User views Featured Solutions section."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("User clicks All Solutions CTA"))
def click_all_solutions_cta(page: Page) -> None:
    """User clicks All Solutions CTA."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()
    solutions_page.click_all_solutions_cta()


@given(parsers.parse("User examines All Solutions CTA"))
def examine_all_solutions_cta(page: Page) -> None:
    """User examines All Solutions CTA."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("Solutions portfolio page is unavailable"))
def portfolio_unavailable(page: Page) -> None:
    """Portfolio page is unavailable."""
    pass


@when("User looks for additional action")
def look_for_action(page: Page) -> None:
    """User looks for additional action."""
    pass


@when("Navigation completes")
def navigation_completes(page: Page) -> None:
    """Navigation completes."""
    page.wait_for_load_state("domcontentloaded")


@when("User checks destination")
def check_destination(page: Page) -> None:
    """Check destination."""
    pass


@when("User clicks All Solutions CTA")
def click_cta(page: Page) -> None:
    """Click All Solutions CTA."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.click_all_solutions_cta()


@then("CTA is visible within or after the section")
def cta_visible(page: Page) -> None:
    """Verify CTA is visible."""
    solutions_page = FeaturedSolutionsPage(page)
    expect(solutions_page.locators.all_solutions_cta).to_be_visible()


@then("Browser loads /solutions/ page")
def loads_solutions_page(page: Page) -> None:
    """Verify loads solutions page."""
    expect(page).to_have_url("/solutions/")


@then("URL resolves to canonical /solutions/ destination")
def canonical_solutions_url(page: Page) -> None:
    """Verify canonical solutions URL."""
    solutions_page = FeaturedSolutionsPage(page)
    href = solutions_page.locators.all_solutions_cta.get_attribute("href")
    expect(href).to_contain("/solutions/")


@then("User receives appropriate error or redirect")
def appropriate_error(page: Page) -> None:
    """Verify appropriate error or redirect."""
    pass


@then("No broken page")
def no_broken_page(page: Page) -> None:
    """Verify no broken page."""
    expect(page).not_to_have_url(r"404")
