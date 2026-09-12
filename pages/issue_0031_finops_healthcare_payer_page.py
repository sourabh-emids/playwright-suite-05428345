"""Page object for issue_0031 - FinOps healthcare payer resource card display."""
from playwright.sync_api import Page, expect

from locators.issue_0031_finops_healthcare_payer_locators import Issue0031FinopsHealthcarePayerLocators


class Issue0031FinopsHealthcarePayerPage:
    """Page object for FinOps healthcare payer card."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0031FinopsHealthcarePayerLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.finops_card.scroll_into_view_if_needed()

    def card_should_be_visible(self) -> None:
        """Verify card is visible."""
        expect(self.locators.finops_card).to_be_visible()

    def card_should_have_read_more_action(self) -> None:
        """Verify card has a Read More action."""
        expect(self.page.get_by_text("Read More").first).to_be_visible()
