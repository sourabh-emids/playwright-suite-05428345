"""Page object for issue_0049 - Contact form submission feedback and retry."""
from playwright.sync_api import Page, expect

from locators.issue_0049_contact_form_submission_locators import Issue0049ContactFormSubmissionLocators


class Issue0049ContactFormSubmissionPage:
    """Page object for contact form submission."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0049ContactFormSubmissionLocators()
        self.locators.page = page

    def navigate_to_contact(self) -> None:
        """Navigate to the contact page."""
        self.page.goto("/contact/")

    def submit_form(self) -> None:
        """Submit the form."""
        self.locators.submit_button.click()

    def should_receive_feedback(self) -> None:
        """Verify user receives feedback on submission."""
        # Either success message or error message should appear
        feedback = self.locators.form_feedback
        expect(feedback.first).to_be_visible(timeout=10000)

    def should_be_able_to_retry(self) -> None:
        """Verify user can retry if submission fails."""
        # Form should remain accessible for retry
        expect(self.locators.submit_button).to_be_enabled()
