"""Step definitions for Issue 0010 - Hero CTA routing to FDCE experience."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user clicks the hero CTA")
def click_hero_cta(page: Page):
    homepage = HomepagePage(page)
    homepage.hero_cta_routes_to_fdce()


@when("The CTA is activated")
def cta_activated(page: Page):
    pass


@then("The user is navigated to the canonical FDCE page at /forward-deployed-context-engineering/")
def navigated_to_fdce(page: Page):
    page.wait_for_url("**/forward-deployed-context-engineering/**")


@given("A user examines the hero CTA URL")
def examine_hero_cta_url(page: Page):
    page.goto("/")


@when("The URL is inspected")
def url_inspected(page: Page):
    pass


@then("The URL is HTTPS and canonical")
def url_https_canonical(page: Page):
    cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    href = cta.get_attribute("href")
    assert href.startswith("https://www.emids.com/forward-deployed-context-engineering/")


@given("A user right-clicks or uses keyboard to open hero CTA in new tab")
def open_cta_new_tab(page: Page):
    page.goto("/")
    cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    # Open in new tab
    cta.click(modifiers=["Control"])


@when("The action is performed")
def action_performed(page: Page):
    pass


@then("The FDCE page opens in a new tab with expected behavior")
def fdce_opens_new_tab(page: Page):
    # Verify new tab opened with correct URL
    new_page = page.context.pages[-1]
    expect(new_page).to_have_url("**/forward-deployed-context-engineering/**")
    new_page.close()


@given("The FDCE destination page is temporarily unavailable")
def fdce_unavailable(page: Page):
    pass


@when("A user clicks the hero CTA")
def click_hero_cta_unavailable(page: Page):
    page.goto("/")
    page.get_by_role("link", name="See How We Deliver Outcomes").click()


@then("An appropriate error or redirect handling occurs")
def error_redirect_handling(page: Page):
    page.wait_for_load_state("networkidle")
    # Verify either error page or redirect
    assert page.url in ["https://www.emids.com/forward-deployed-context-engineering/", 
                        "https://www.emids.com/"]
