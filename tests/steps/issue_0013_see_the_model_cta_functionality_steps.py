"""Step definitions for issue_0013: See the model CTA functionality"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0013_see_the_model_cta_functionality_page import Issue0013SeeModelCTAPage


@given("The How We Deliver section is rendered")
def section_rendered(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.navigate_to_homepage()


@given("A user navigates using keyboard only")
def user_navigates_keyboard(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.navigate_to_homepage()


@given("The CTA is rendered")
def cta_rendered(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.navigate_to_homepage()


@given("The CTA is configured")
def cta_configured(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.navigate_to_homepage()


@when("A user clicks the See the model CTA")
def user_clicks_see_model_cta(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.click_see_model_cta()


@when("Focus reaches the CTA and Enter is pressed")
def focus_reaches_cta_enter(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.focus_and_press_enter()


@when("Screen reader accesses the element")
def screen_reader_accesses_element(page: Page):
    """Screen reader check happens in assertions."""
    pass


@when("Automated testing checks the destination URL")
def automated_checks_destination(page: Page):
    """Destination check happens in assertions."""
    pass


@then("Navigation routes to the FDCE detail page at /forward-deployed-context-engineering/")
def navigation_routes_to_fdce(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.verify_routes_to_fdce()


@then("Navigation to the FDCE page occurs")
def navigation_occurs(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.verify_routes_to_fdce()


@then("The accessible name describes the action (e.g., 'See the model')")
def accessible_name_descriptive(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.verify_accessible_name()


@then("The URL returns HTTP 200 status")
def url_returns_200(page: Page):
    page_object = Issue0013SeeModelCTAPage(page)
    page_object.verify_destination_returns_200()
