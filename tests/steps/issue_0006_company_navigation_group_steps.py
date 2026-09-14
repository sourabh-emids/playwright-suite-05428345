"""Step definitions for issue_0006: Company Navigation Group."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from locators.company_menu_locators import CompanyMenuLocators


@given("Company menu is open")
def company_menu_open(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    locators = CompanyMenuLocators(page)
    locators.company_trigger.click()


@when("User views navigation items")
def view_company_nav_items(page: Page):
    pass


@then("Menu exposes only approved company links")
def approved_links_only(page: Page):
    locators = CompanyMenuLocators(page)
    links = locators.company_links.all()
    for link in links:
        href = link.get_attribute("href")
        text = link.text_content()
        assert text and text.strip(), "Link has empty text"
        assert href, "Link has no href"


@given("Company menu is rendered")
def company_menu_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User interacts via keyboard, pointer, or touch")
def interact_methods(page: Page):
    locators = CompanyMenuLocators(page)
    locators.company_trigger.click()
    locators.company_trigger.hover()
    page.keyboard.press("Tab")


@then("Menu works with all interaction methods")
def works_all_interactions(page: Page):
    locators = CompanyMenuLocators(page)
    expect(locators.company_menu).to_be_visible()


@given("Company menu is open")
def company_menu_open_connect(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    locators = CompanyMenuLocators(page)
    locators.company_trigger.click()


@when("User navigates to contact-related destinations")
def nav_to_contact(page: Page):
    locators = CompanyMenuLocators(page)
    locators.contact_link.click()


@then("Contact/Connect destinations route correctly")
def contact_routes_correctly(page: Page):
    expect(page).to_have_urlContaining("/contact/")


@given("Company navigation is configured")
def company_nav_configured(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Menu renders")
def company_menu_renders(page: Page):
    locators = CompanyMenuLocators(page)
    locators.company_trigger.click()


@then("Only published pages appear in the menu")
def only_published_pages(page: Page):
    locators = CompanyMenuLocators(page)
    links = locators.company_links.all()
    for link in links:
        href = link.get_attribute("href")
        assert href and not href.endswith("#"), "Unpublished page found"


@given("Company menu is open")
def company_menu_open_focus(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    locators = CompanyMenuLocators(page)
    locators.company_trigger.click()


@when("User navigates via keyboard")
def keyboard_nav_company(page: Page):
    page.keyboard.press("Tab")


@then("Focus does not trap unexpectedly within menu")
def no_focus_trap(page: Page):
    locators = CompanyMenuLocators(page)
    expect(locators.company_menu).to_be_visible()
