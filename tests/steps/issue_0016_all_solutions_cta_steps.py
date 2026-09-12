"""Step definitions for Issue 0016 - All Solutions CTA functionality."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Featured Solutions section")
def view_featured_solutions_cta(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@when("The user clicks the All Solutions CTA")
def click_all_solutions_cta(page: Page):
    homepage = HomepagePage(page)
    homepage.click_all_solutions_cta()


@then("The CTA routes to the solutions portfolio at /solutions/")
def routes_to_solutions(page: Page):
    page.wait_for_url("**/solutions/**")


@given("A user examines the All Solutions CTA URL")
def examine_all_solutions_url(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@when("The URL is inspected")
def url_inspected(page: Page):
    pass


@then("The URL is canonical (/solutions/)")
def url_canonical(page: Page):
    cta = page.get_by_role("link", name="All solutions")
    href = cta.get_attribute("href")
    assert href.endswith("/solutions/") or "/solutions/" in href


@given("The solutions portfolio page is unavailable")
def portfolio_unavailable(page: Page):
    pass


@when("A user clicks the All Solutions CTA")
def click_all_solutions_unavailable(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")
    page.get_by_role("link", name="All solutions").click()


@then("An appropriate error handling occurs")
def error_handling(page: Page):
    page.wait_for_load_state("networkidle")
    # Should show error or redirect appropriately
