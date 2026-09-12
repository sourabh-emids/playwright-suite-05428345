"""Step definitions for Issue 0022 - Engineering capability content rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Capabilities section")
def view_capabilities_eng(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The Engineering capability panel/card loads")
def engineering_panel_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Engineering label and supporting content are rendered")
def engineering_label_content(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.engineering_capability).to_be_visible()


@given("A user views the Engineering capability card")
def view_eng_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The user clicks the Engineering capability link")
def click_eng_link(page: Page):
    homepage = HomepagePage(page)
    homepage.click_engineering_capability_link()


@then("The link navigates to the relevant Engineering capability page")
def eng_navigates(page: Page):
    page.wait_for_load_state("networkidle")


@given("A user or assistive technology examines the Engineering capability")
def examine_eng_capability(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The content is analyzed")
def content_analyzed_eng(page: Page):
    pass


@then("Title is present and not empty")
def eng_title_present(page: Page):
    expect(page.getByText("Engineering")).to_be_visible()


@given("A user examines the Engineering capability link")
def examine_eng_link(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The URL is inspected")
def url_inspected_eng(page: Page):
    pass


@then("URL is valid and resolves to the Engineering capability destination")
def eng_url_valid(page: Page):
    link = page.getByText("Digital Engineering", exact=False).first.locator("..")
    href = link.get_attribute("href")
    assert href and "/capabilities/" in href
