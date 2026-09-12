"""Step definitions for Issue 0013 - See the model CTA functionality."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user is viewing the How We Deliver section")
def viewing_how_we_deliver(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")


@when("The user clicks the See the model CTA")
def click_see_model_cta(page: Page):
    homepage = HomepagePage(page)
    homepage.click_see_the_model_cta()


@then("The user is navigated to /forward-deployed-context-engineering/")
def navigated_to_fdce(page: Page):
    page.wait_for_url("**/forward-deployed-context-engineering/**")


@given("A user is navigating with keyboard")
def navigating_keyboard(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")


@when("The user focuses on and activates the See the model CTA")
def focus_activate_see_model(page: Page):
    page.get_by_role("link", name="See the model").focus()
    page.keyboard.press("Enter")


@then("The action is triggered successfully")
def action_triggered(page: Page):
    page.wait_for_url("**/forward-deployed-context-engineering/**")


@given("A user or assistive technology examines the CTA")
def examine_cta(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")


@when("The CTA is present")
def cta_present(page: Page):
    pass


@then("The accessible name describes the action")
def accessible_name_describes_action(page: Page):
    cta = page.get_by_role("link", name="See the model")
    expect(cta).to_be_visible()
    name = cta.get_attribute("aria-label") or cta.text_content()
    assert "model" in name.lower()


@given("The FDCE detail page returns 404")
def fdce_404(page: Page):
    pass


@when("A user clicks the See the model CTA")
def click_see_model_404(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")
    page.get_by_role("link", name="See the model").click()


@then("An appropriate error page is displayed")
def error_page_displayed(page: Page):
    page.wait_for_load_state("networkidle")
    title = page.title()
    assert "404" in title or "Page not found" in title or "Error" in title
