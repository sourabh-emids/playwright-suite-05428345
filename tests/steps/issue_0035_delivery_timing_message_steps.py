"""Step definitions for issue_0035 - Delivery timing message rendering."""
from pytest_bdd import given, then, when

from pages.issue_0035_delivery_timing_message_page import Issue0035DeliveryTimingMessagePage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0035DeliveryTimingMessagePage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the final CTA section")
def view_final_cta_section(page: Issue0035DeliveryTimingMessagePage):
    """View the final CTA section."""
    page.view_final_cta_section()


@then('the timing message "1 Day · 2 Weeks · 3 Months" should be visible')
def timing_message_visible(page: Issue0035DeliveryTimingMessagePage):
    """Verify timing message is visible."""
    page.timing_message_should_be_visible()


@then("the timing description should be present")
def timing_description_present(page: Issue0035DeliveryTimingMessagePage):
    """Verify timing description is present."""
    page.timing_description_should_be_present()
