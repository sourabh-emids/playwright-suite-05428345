"""Page object for issue_0033 - Resource access handoff for eBook cards."""
from playwright.sync_api import Page, expect

from locators.issue_0033_resource_access_handoff_locators import Issue0033ResourceAccessHandoffLocators


class Issue0033ResourceAccessHandoffPage:
    """Page object for resource access handoff."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0033ResourceAccessHandoffLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.ebook_card.scroll_into_view_if_needed()

    def click_ebook_card(self) -> None:
        """Click an eBook card."""
        self.locators.ebook_card.click()

    def should_be_on_resource_page(self) -> None:
        """Verify user is on the resource page."""
        expect(self.page).to_have_url("**/insights/**")
