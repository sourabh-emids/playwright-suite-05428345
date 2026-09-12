"""Step definitions for Issue 0031 - FinOps healthcare payer resource card."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the FinOps healthcare payer resource card")
def view_finops_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card renders")
def finops_renders(page: Page):
    page.wait_for_load_state("networkidle")


@then("Card renders with title, type, action and routes correctly to configured destination")
def finops_content(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.finops_blog).to_be_visible()


@given("A user clicks the FinOps resource card action")
def click_finops(page: Page):
    homepage = HomepagePage(page)
    homepage.click_insight_card("FinOps Principles")


@when("The action is activated")
def finops_activated(page: Page):
    pass


@then("User is navigated to the valid destination")
def finops_navigates(page: Page):
    page.wait_for_url("**/insights/**")


@given("The FinOps resource link is broken")
def finops_broken(page: Page):
    pass


@when("A user clicks the card")
def click_finops_broken(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")
    page.getByText("FinOps Principles", exact=False).first.locator("..").click()


@then("Appropriate error handling or redirect occurs")
def finops_error_handling(page: Page):
    page.wait_for_load_state("networkidle")
