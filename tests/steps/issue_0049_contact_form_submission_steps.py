"""Step definitions for issue_0049 - Contact form submission feedback and retry."""
from pytest_bdd import given, then, when

from pages.issue_0049_contact_form_submission_page import Issue0049ContactFormSubmissionPage


@given("I navigate to the contact page")
def navigate_to_contact(page: Issue0049ContactFormSubmissionPage):
    """Navigate to the contact page."""
    page.navigate_to_contact()


@when("I submit the contact form")
def submit_form(page: Issue0049ContactFormSubmissionPage):
    """Submit the contact form."""
    page.submit_form()


@then("I should receive feedback on submission")
def receive_feedback(page: Issue0049ContactFormSubmissionPage):
    """Verify user receives feedback."""
    page.should_receive_feedback()


@then("I should be able to retry if submission fails")
def can_retry(page: Issue0049ContactFormSubmissionPage):
    """Verify user can retry."""
    page.should_be_able_to_retry()
