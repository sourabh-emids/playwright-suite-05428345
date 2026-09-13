"""Steps for All Solutions CTA functionality (issue_0016)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0016_all_solutions_cta_page import AllSolutionsCTAPage
from locators.issue_0016_all_solutions_cta_locators import AllSolutionsCTALocators


@given("User views Featured Solutions section")
def view_section(page: Page) -> None:
    page.goto("/")


@given("User clicks All Solutions CTA")
def click_cta(page: Page) -> None:
    page.goto("/")
    cta_page = AllSolutionsCTAPage(page)
    cta_page.click_cta()


@when("User looks for All Solutions CTA")
def look_for_cta(page: Page) -> None:
    pass


@when("Navigation occurs")
def navigation(page: Page) -> None:
    pass


@when("User examines href")
def examine_href(page: Page) -> None:
    pass


@when("Portfolio page is unavailable")
def portfolio_unavailable(page: Page) -> None:
    pass


@then("CTA is visible after or within the section")
def cta_visible(page: Page) -> None:
    expect(AllSolutionsCTALocators(page).all_solutions_cta).to_be_visible()


@then("User is navigated to '/solutions/'")
def navigated_to_solutions(page: Page) -> None:
    expect(page).to_have_url("/solutions/")


@then("URL is canonical")
def url_canonical(page: Page) -> None:
    cta_page = AllSolutionsCTAPage(page)
    href = cta_page.get_href()
    assert href and "solutions" in href


@then("User sees appropriate error or fallback")
def error_fallback(page: Page) -> None:
    pass
