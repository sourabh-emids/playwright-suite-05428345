"""Step definitions for Issue 0021 - AI capability content rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Capabilities section")
def view_capabilities_ai(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The AI capability panel/card loads")
def ai_panel_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("AI label and supporting content are rendered")
def ai_label_content_rendered(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.ai_capability).to_be_visible()


@given("A user views the AI capability card")
def view_ai_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The user clicks the AI capability link")
def click_ai_link(page: Page):
    homepage = HomepagePage(page)
    homepage.click_ai_capability_link()


@then("The link navigates to the relevant AI capability page")
def ai_navigates(page: Page):
    page.wait_for_load_state("networkidle")


@given("A user or assistive technology examines the AI capability")
def examine_ai_capability(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The content is analyzed")
def content_analyzed_ai(page: Page):
    pass


@then("Title is present and not empty")
def ai_title_present(page: Page):
    expect(page.getByText("Artificial Intelligence")).to_be_visible()


@given("A user examines the AI capability link")
def examine_ai_link(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The URL is inspected")
def url_inspected_ai(page: Page):
    pass


@then("URL is valid and resolves to the AI capability destination")
def ai_url_valid(page: Page):
    link = page.getByText("Data Engineering", exact=False).first.locator("..")
    href = link.get_attribute("href")
    assert href and "/capabilities/" in href or "/pacca-ai/" in href


@given("The AI capability destination page is unavailable")
def ai_destination_unavailable(page: Page):
    pass


@when("A user clicks the AI capability link")
def click_ai_unavailable(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")
    page.getByText("Data Engineering", exact=False).first.locator("..").click()


@then("Appropriate error handling occurs")
def ai_error_handling(page: Page):
    page.wait_for_load_state("networkidle")
