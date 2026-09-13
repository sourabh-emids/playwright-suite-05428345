"""Step definitions for issue_0007: Header Connect CTA functionality"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0007_header_connect_cta_functionality_page import Issue0007ConnectCTAPage


@given("A user views the global header")
def user_views_header(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.navigate_to_homepage()


@given("A user or assistive technology accesses the Connect CTA")
def user_accesses_connect_cta(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.navigate_to_homepage()


@given("A user clicks the Connect CTA")
def user_clicks_connect_cta(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.navigate_to_homepage()


@given("A user navigates using keyboard only")
def user_navigates_keyboard(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.navigate_to_homepage()


@given("The Connect CTA is rendered")
def connect_cta_rendered(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.navigate_to_homepage()


@when("The user visually scans the header")
def user_scans_header(page: Page):
    """Visual scan happens in assertions."""
    pass


@when("Screen reader or accessibility tool reads the element")
def screen_reader_reads_element(page: Page):
    """Accessibility check happens in assertions."""
    pass


@when("The navigation action completes")
def navigation_completes(page: Page):
    """Navigation check happens in assertions."""
    pass


@when("Focus reaches the Connect CTA and user presses Enter")
def focus_reaches_cta_enter_pressed(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    # Focus on the CTA
    page_object.locators.connect_cta.focus()
    page.keyboard.press("Enter")


@when("Automated testing validates the URL")
def automated_validates_url(page: Page):
    """URL validation happens in assertions."""
    pass


@then("The Connect CTA is visually distinct from other navigation items")
def cta_visually_distinct(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.verify_cta_visually_distinct()


@then("The CTA has an accessible name that describes its action")
def cta_has_accessible_name(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.verify_accessible_name()


@then("The user lands on the contact page at /contact/")
def user_lands_on_contact(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.verify_routes_to_contact()


@then("Navigation to the contact page occurs")
def navigation_to_contact_occurs(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.verify_routes_to_contact()


@then("The URL is valid and uses the HTTPS protocol")
def url_valid_https(page: Page):
    page_object = Issue0007ConnectCTAPage(page)
    page_object.verify_https_protocol()
