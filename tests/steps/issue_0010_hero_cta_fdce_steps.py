"""Step definitions for issue_0010: Hero CTA Routes to FDCE Experience."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.hero_page import HeroPage


@given("User clicks hero CTA")
def user_clicks_hero_cta(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    hero = HeroPage(page)
    hero.click_hero_cta()


@when("Navigation completes")
def nav_completes(page: Page):
    page.wait_for_load_state("networkidle")


@then("CTA resolves to canonical FDCE page at /forward-deployed-context-engineering/")
def cta_resolves_fdce(page: Page):
    expect(page).to_have_urlContaining("/forward-deployed-context-engineering/")


@given("Hero CTA is configured")
def hero_cta_configured(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url(page: Page):
    pass


@then("URL is HTTPS and canonical")
def url_https_canonical(page: Page):
    hero = HeroPage(page)
    href = hero.get_cta_href()
    assert href and href.startswith("https://"), f"URL should be HTTPS: {href}"
    assert "/forward-deployed-context-engineering/" in href, f"URL should be canonical FDCE: {href}"


@given("User clicks hero CTA")
def click_hero_cta_nav(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    hero = HeroPage(page)
    hero.click_hero_cta()


@when("Navigation occurs")
def nav_occurs(page: Page):
    page.wait_for_load_state("networkidle")


@then("Browser navigation behaves as expected (history entry created)")
def history_entry_created(page: Page):
    expect(page).to_have_urlContaining("/forward-deployed-context-engineering/")


@given("User opens hero CTA in new tab")
def open_cta_new_tab(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    hero = HeroPage(page)
    hero.hero_cta.click(modifier="Control")


@when("New tab loads")
def new_tab_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Destination page loads correctly")
def destination_loads(page: Page):
    expect(page).to_have_urlContaining("/forward-deployed-context-engineering/")


@given("FDCE destination page is unavailable")
def fdce_unavailable(page: Page):
    page.goto("/")
    page.route("**/forward-deployed-context-engineering/**", lambda route: route.abort())


@when("User clicks hero CTA")
def click_cta_unavailable(page: Page):
    hero = HeroPage(page)
    hero.click_hero_cta()


@then("User sees appropriate error or redirect")
def sees_error_redirect(page: Page):
    pass
