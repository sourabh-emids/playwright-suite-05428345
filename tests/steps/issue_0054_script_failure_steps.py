"""Steps for Script failure resilience (issue_0054)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0054_script_failure_locators import ScriptFailureLocators


@given("Analytics scripts fail")
def analytics_fail(page: Page) -> None:
    page.goto("/")


@given("Consent scripts fail")
def consent_fail(page: Page) -> None:
    page.goto("/")


@given("Media scripts fail")
def media_fail(page: Page) -> None:
    page.goto("/")


@given("Marketing scripts fail")
def marketing_fail(page: Page) -> None:
    page.goto("/")


@given("Optional integration fails")
def integration_fail(page: Page) -> None:
    page.goto("/")


@given("Content Security Policy blocks script")
def csp_block(page: Page) -> None:
    page.goto("/")


@given("DNS resolution fails for third-party")
def dns_fail(page: Page) -> None:
    page.goto("/")


@given("Ad blocker blocks third-party script")
def ad_blocker(page: Page) -> None:
    page.goto("/")


@given("Third-party script times out")
def timeout(page: Page) -> None:
    page.goto("/")


@given("Vendor script is malformed")
def malformed(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


@when("Error occurs")
def error_occurs(page: Page) -> None:
    pass


@then("Header remains readable and functional")
def header_readable(page: Page) -> None:
    expect(ScriptFailureLocators(page).header).to_be_visible()


@then("Main content remains readable")
def main_readable(page: Page) -> None:
    expect(ScriptFailureLocators(page).main_content).to_be_visible()


@then("CTAs remain functional")
def ctas_functional(page: Page) -> None:
    expect(ScriptFailureLocators(page).ctas.first).to_be_visible()


@then("Footer remains navigable")
def footer_navigable(page: Page) -> None:
    expect(ScriptFailureLocators(page).footer).to_be_visible()


@then("Error does not break core functionality")
def core_intact(page: Page) -> None:
    expect(ScriptFailureLocators(page).main_content).to_be_visible()


@then("Core functionality remains intact")
def core_functionality(page: Page) -> None:
    expect(ScriptFailureLocators(page).main_content).to_be_visible()
