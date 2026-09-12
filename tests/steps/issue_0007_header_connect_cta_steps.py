"""Step definitions for issue_0007 - Header Connect CTA visibility and routing."""
from pytest_bdd import given, then, when

from pages.issue_0007_connect_cta_page import Issue0007ConnectCTAPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0007ConnectCTAPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the header")
def view_header(page: Issue0007ConnectCTAPage):
    """View the header."""
    pass


@then("the Connect CTA should be visible")
def connect_cta_visible(page: Issue0007ConnectCTAPage):
    """Verify Connect CTA is visible."""
    page.connect_cta_should_be_visible()


@then("the Connect CTA should link to the contact page")
def connect_cta_links_to_contact(page: Issue0007ConnectCTAPage):
    """Verify Connect CTA links to the contact page."""
    page.connect_cta_should_link_to_contact_page()


@when("I click the Connect CTA in the header")
def click_connect_cta(page: Issue0007ConnectCTAPage):
    """Click the Connect CTA in the header."""
    page.click_connect_cta()


@then("I should be navigated to the contact page")
def on_contact_page(page: Issue0007ConnectCTAPage):
    """Verify user is on the contact page."""
    page.should_be_on_contact_page()
