"""Step definitions for issue_0054 - Graceful handling of script failures."""
from pytest_bdd import given, then, when

from pages.issue_0054_script_failure_handling_page import Issue0054ScriptFailureHandlingPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0054ScriptFailureHandlingPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I simulate a script failure")
def simulate_script_failure(page: Issue0054ScriptFailureHandlingPage):
    """Simulate a script failure."""
    page.simulate_script_failure()


@then("the page should still be functional")
def page_functional(page: Issue0054ScriptFailureHandlingPage):
    """Verify page still works."""
    page.page_should_still_be_functional()


@then("critical functionality should remain accessible")
def critical_functionality_accessible(page: Issue0054ScriptFailureHandlingPage):
    """Verify critical functionality remains accessible."""
    page.critical_functionality_should_remain_accessible()
