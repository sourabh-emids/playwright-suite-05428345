"""Step definitions for issue_0016: Provide All Solutions CTA."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Featured Solutions section")
def view_featured_solutions_section(page: Page) -> None:
    page.goto("/")


@when("Locating CTA")
def locate_cta(page: Page) -> None:
    pass


@then("All Solutions CTA is visible either after or within the section")
def cta_visible(page: Page) -> None:
    cta = page.get_byRole("link", name="All solutions")
    expect(cta).to_be_visible()


@given("User clicks All Solutions CTA")
def click_all_solutions_cta(page: Page) -> None:
    page.goto("/")
    page.get_byRole("link", name="All solutions").click()


@when("Navigation occurs")
def navigation_occurs(page: Page) -> None:
    pass


@then("User navigates to /solutions/")
def navigate_solutions(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/solutions/")


@given("User inspects CTA URL")
def inspect_cta_url(page: Page) -> None:
    page.goto("/")


@when("Checking URL format")
def check_url_format(page: Page) -> None:
    pass


@then("URL uses canonical /solutions/ path")
def canonical_path(page: Page) -> None:
    cta = page.get_byRole("link", name="All solutions")
    href = cta.get_attribute("href")
    assert "/solutions/" in href


@given("/solutions/ page returns error")
def solutions_error(page: Page) -> None:
    pass


@when("User clicks CTA")
def click_cta_error(page: Page) -> None:
    page.goto("/")
    page.get_byRole("link", name="All solutions").click()


@then("Appropriate error handling occurs")
def error_handling(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com/solutions")
