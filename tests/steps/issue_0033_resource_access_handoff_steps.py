"""Step definitions for issue_0033 - Resource access handoff for eBook cards."""
from pytest_bdd import given, then, when

from pages.issue_0033_resource_access_handoff_page import Issue0033ResourceAccessHandoffPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0033ResourceAccessHandoffPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0033ResourceAccessHandoffPage):
    """View the Insights section."""
    page.view_insights_section()


@when("I click an eBook card")
def click_ebook_card(page: Issue0033ResourceAccessHandoffPage):
    """Click an eBook card."""
    page.click_ebook_card()


@then("I should be navigated to the resource page")
def on_resource_page(page: Issue0033ResourceAccessHandoffPage):
    """Verify user is on the resource page."""
    page.should_be_on_resource_page()
