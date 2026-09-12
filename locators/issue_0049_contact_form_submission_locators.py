"""Locators for issue_0049 - Contact form submission feedback and retry."""
from playwright.sync_api import Locator


class Issue0049ContactFormSubmissionLocators:
    """Locators for contact form submission."""

    @property
    def submit_button(self) -> Locator:
        """Return the form submit button."""
        return self.page.get_by_role("button", name="Submit")

    @property
    def form_feedback(self) -> Locator:
        """Return the form feedback element."""
        return self.page.locator("[class*='message'], [class*='alert'], [class*='success'], [class*='error']")
