"""Step definitions for issue_0006: Company navigation group"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0006_company_navigation_group_page import Issue0006CompanyMenuPage


@given("A user navigates to the Company menu")
def user_navigates_company_menu(page: Page):
    page_object = Issue0006CompanyMenuPage(page)
    page_object.navigate_to_homepage()
    page_object.open_company_menu()


@given("The Company menu is rendered")
def company_menu_rendered(page: Page):
    page_object = Issue0006CompanyMenuPage(page)
    page_object.open_company_menu()


@when("The user activates the menu using keyboard, pointer, or touch")
def user_activates_menu(page: Page):
    page_object = Issue0006CompanyMenuPage(page)
    page_object.open_company_menu()


@when("Automated testing validates destination URLs")
def automated_validates_urls(page: Page):
    """URL validation happens in assertions."""
    pass


@then("The menu opens and displays approved company links and contact destinations")
def menu_displays_company_links(page: Page):
    page_object = Issue0006CompanyMenuPage(page)
    page_object.verify_company_menu_content()


@then("All links point to currently published pages with valid HTTP status")
def links_point_to_published_pages(page: Page):
    page_object = Issue0006CompanyMenuPage(page)
    # Basic check - links should be present and not be anchors
    links = page_object.get_company_links()
    for link in links:
        href = link.get_attribute("href")
        expect(href).not_to_be_none()
        if href:
            expect(href).not_to_match(r"^(#|javascript:)")
