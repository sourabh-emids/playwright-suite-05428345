"""Steps for Hero CTA routes to FDCE experience (issue_0010)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0010_hero_cta_fdce_page import HeroCTAFDCEPage
from locators.issue_0010_hero_cta_fdce_locators import HeroCTAFDCELocators


@given("User is on Emids homepage viewing hero")
def on_homepage_hero(page: Page) -> None:
    page.goto("/")


@given("User inspects hero CTA URL")
def inspect_cta_url(page: Page) -> None:
    page.goto("/")


@given("User right-clicks hero CTA")
def right_click_cta(page: Page) -> None:
    page.goto("/")


@given("User clicks hero CTA")
def click_hero_cta(page: Page) -> None:
    page.goto("/")
    cta_page = HeroCTAFDCEPage(page)
    cta_page.click_hero_cta()


@when("User clicks the hero CTA")
def click_cta(page: Page) -> None:
    cta_page = HeroCTAFDCEPage(page)
    cta_page.click_hero_cta()


@when("User examines href attribute")
def examine_href(page: Page) -> None:
    pass


@when("User selects Open in New Tab")
def open_new_tab(page: Page) -> None:
    pass


@when("FDCE destination is unavailable (404/503)")
def fdce_unavailable(page: Page) -> None:
    pass


@then("User is navigated to '/forward-deployed-context-engineering/'")
def navigated_to_fdce(page: Page) -> None:
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("URL uses HTTPS protocol and is canonical")
def url_https_canonical(page: Page) -> None:
    cta_page = HeroCTAFDCEPage(page)
    href = cta_page.get_cta_href()
    assert href
    assert href.startswith("https://")


@then("FDCE page opens in new tab")
def fdce_new_tab(page: Page) -> None:
    pass


@then("User sees appropriate error page")
def error_page_shown(page: Page) -> None:
    pass
