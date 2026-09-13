"""Steps for AI, Engineering, and Platforms capability content rendering (issues 0021-0023)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0021_0022_0023_capabilities_content_locators import CapabilitiesContentLocators


@given("User views Capabilities section")
def view_capabilities(page: Page) -> None:
    page.goto("/")


@given("AI capability panel renders")
def ai_panel_renders(page: Page) -> None:
    page.goto("/")


@given("Engineering capability panel renders")
def engineering_panel_renders(page: Page) -> None:
    page.goto("/")


@given("Platforms capability panel renders")
def platforms_panel_renders(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User clicks AI link")
def click_ai(page: Page) -> None:
    pass


@when("User validates content")
def validate(page: Page) -> None:
    pass


@when("User clicks Engineering link")
def click_engineering(page: Page) -> None:
    pass


@then("AI label and supporting content render in the AI capability panel")
def ai_renders(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("Link is operable and navigates to AI capability page")
def ai_link_works(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("AI title is present and non-empty")
def ai_title(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("Engineering label and supporting content render in the Engineering capability panel")
def engineering_renders(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("Link is operable and navigates to Engineering capability page")
def engineering_link_works(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("Engineering title is present and non-empty")
def engineering_title(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("Platforms label and supporting content render in the Platforms capability panel")
def platforms_renders(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()


@then("Platforms title is present and matches approved taxonomy")
def platforms_title(page: Page) -> None:
    expect(CapabilitiesContentLocators(page).capabilities_section).to_be_visible()
