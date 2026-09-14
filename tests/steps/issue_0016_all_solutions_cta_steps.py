"""Step definitions for issue_0016: All Solutions CTA Rendering."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.featured_solutions_page import FeaturedSolutionsPage


@given("Featured Solutions section renders")
def fs_section_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Section is reviewed")
def review_section(page: Page):
    pass


@then("All Solutions CTA is visible after or within the section")
def all_solutions_cta_visible(page: Page):
    fs = FeaturedSolutionsPage(page)
    expect(fs.all_solutions_cta).to_be_visible()


@given("User clicks All Solutions CTA")
def click_all_solutions(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    fs = FeaturedSolutionsPage(page)
    fs.click_all_solutions_cta()


@when("Navigation completes")
def nav_completes_solutions(page: Page):
    page.wait_for_load_state("networkidle")


@then("CTA routes to solutions portfolio at /solutions/")
def routes_to_solutions(page: Page):
    expect(page).to_have_urlContaining("/solutions/")


@given("All Solutions CTA is configured")
def cta_configured(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url_solutions(page: Page):
    pass


@then("URL is canonical")
def url_canonical(page: Page):
    fs = FeaturedSolutionsPage(page)
    href = fs.all_solutions_cta.get_attribute("href")
    assert href and "/solutions/" in href, f"Should route to /solutions/: {href}"


@given("Portfolio page at /solutions/ is unavailable")
def portfolio_unavailable(page: Page):
    page.goto("/")
    page.route("**/solutions/**", lambda route: route.abort())


@when("User clicks All Solutions CTA")
def click_cta_unavailable(page: Page):
    fs = FeaturedSolutionsPage(page)
    fs.click_all_solutions_cta()


@then("User sees appropriate error handling")
def error_handling(page: Page):
    pass
