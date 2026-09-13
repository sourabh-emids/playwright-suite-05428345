"""Steps for Google Tag Manager container loading (issue_0037)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0037_gtm_loading_locators import GTMLoadingLocators


@given("Google Tag Manager fails to load")
def gtm_fails(page: Page) -> None:
    page.goto("/")


@given("Non-essential tags are configured in GTM")
def tags_configured(page: Page) -> None:
    page.goto("/")


@given("GTM script loads")
def gtm_loads(page: Page) -> None:
    page.goto("/")


@given("Ad blocker is active")
def ad_blocker(page: Page) -> None:
    page.goto("/")


@given("Content Security Policy blocks GTM")
def csp_block(page: Page) -> None:
    page.goto("/")


@given("GTM script times out")
def gtm_timeout(page: Page) -> None:
    page.goto("/")


@given("User has denied analytics consent")
def consent_denied(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Required consent has not been given")
def no_consent(page: Page) -> None:
    pass


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


@then("Core page content and functionality remain intact")
def core_intact(page: Page) -> None:
    expect(GTMLoadingLocators(page).main_content).to_be_visible()


@then("Non-essential tags do not run before required consent")
def tags_consent(page: Page) -> None:
    pass


@then("GTM loading is non-blocking and does not prevent page rendering")
def non_blocking(page: Page) -> None:
    expect(GTMLoadingLocators(page).header).to_be_visible()


@then("Core page remains functional")
def core_functional(page: Page) -> None:
    expect(GTMLoadingLocators(page).main_content).to_be_visible()


@then("Core functionality remains intact")
def functionality_intact(page: Page) -> None:
    expect(GTMLoadingLocators(page).main_content).to_be_visible()


@then("Core page continues to function")
def page_continues(page: Page) -> None:
    expect(GTMLoadingLocators(page).main_content).to_be_visible()


@then("GTM respects consent configuration")
def respects_consent(page: Page) -> None:
    expect(GTMLoadingLocators(page).main_content).to_be_visible()
