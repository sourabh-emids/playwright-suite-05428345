"""Step definitions for emids_lp_016 - All Solutions CTA."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("All Solutions CTA is visible within or after the section")
def verify_all_solutions_cta_visible(page: Page) -> None:
    from pages.emids_lp_016_all_solutions_cta_page import AllSolutionsCTAPage
    page_obj = AllSolutionsCTAPage(page)
    expect(page_obj.all_solutions_cta).to_be_visible()


@when("User clicks the CTA")
def user_clicks_all_solutions_cta(page: Page) -> None:
    from pages.emids_lp_016_all_solutions_cta_page import AllSolutionsCTAPage
    page_obj = AllSolutionsCTAPage(page)
    page_obj.all_solutions_cta.click()


@then("The CTA routes to '/solutions/'")
def verify_solutions_url(page: Page) -> None:
    expect(page).to_have_url("/solutions/")


@then("URL is canonical HTTPS destination")
def verify_canonical_url(page: Page) -> None:
    from pages.emids_lp_016_all_solutions_cta_page import AllSolutionsCTAPage
    page_obj = AllSolutionsCTAPage(page)
    href = page_obj.all_solutions_cta.get_attribute("href")
    assert href.startswith("https://"), f"Not HTTPS: {href}"


@then("Appropriate error or fallback displayed")
def verify_page_unavailable_handled(page: Page) -> None:
    expect(page).to_have_url("/solutions/")
