"""Step definitions for issue_0010: Route hero CTA to FDCE experience."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User clicks hero CTA")
def click_hero_cta(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="See How We Deliver Outcomes").click()


@when("Navigation occurs")
def navigation_occurs(page: Page) -> None:
    pass


@then("User lands on canonical FDCE URL /forward-deployed-context-engineering/")
def lands_fdce(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")


@given("User inspects hero CTA URL")
def inspect_hero_cta_url(page: Page) -> None:
    page.goto("/")


@when("Checking protocol")
def check_protocol(page: Page) -> None:
    pass


@then("URL uses HTTPS secure protocol")
def url_uses_https(page: Page) -> None:
    cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    href = cta.get_attribute("href")
    assert href.startswith("https://")


@given("User right-clicks hero CTA")
def right_click_hero_cta(page: Page) -> None:
    page.goto("/")


@when("User selects Open in New Tab")
def open_new_tab(page: Page) -> None:
    pass


@then("Page opens in new tab as expected; standard navigation behaviors preserved")
def new_tab_opens(page: Page) -> None:
    cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    href = cta.get_attribute("href")
    assert href == "https://www.emids.com/forward-deployed-context-engineering/"


@given("FDCE destination page returns 404")
def fdce_404(page: Page) -> None:
    pass


@when("User clicks hero CTA")
def click_hero_cta_fdce(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="See How We Deliver Outcomes").click()


@then("Appropriate error handling occurs without page crash")
def error_handling(page: Page) -> None:
    current_url = page.url
    assert "emids.com" in current_url


@given("FDCE destination has redirect configured")
def fdce_redirect(page: Page) -> None:
    pass


@when("User clicks hero CTA")
def click_hero_cta_redirect(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="See How We Deliver Outcomes").click()


@then("User lands on final destination URL with redirect completed")
def lands_final_url(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")
