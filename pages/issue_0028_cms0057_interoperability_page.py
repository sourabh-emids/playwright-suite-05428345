"""Page object for issue_0028 - CMS-0057 interoperability resource card display."""
from playwright.sync_api import Page, expect

from locators.issue_0028_cms0057_interoperability_locators import Issue0028CMS0057InteroperabilityLocators


class Issue0028CMS0057InteroperabilityPage:
    """Page object for CMS-0057 interoperability card."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0028CMS0057InteroperabilityLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.cms0057_card.scroll_into_view_if_needed()

    def card_should_be_visible(self) -> None:
        """Verify card is visible."""
        expect(self.locators.cms0057_card).to_be_visible()

    def card_should_have_ebook_indicator(self) -> None:
        """Verify card has eBook type indicator."""
        expect(self.page.locator("text=eBook").first).to_be_visible()
