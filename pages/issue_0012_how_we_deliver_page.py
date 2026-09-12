"""Page object for issue_0012 - How We Deliver section content rendering."""
from playwright.sync_api import Page, expect

from locators.issue_0012_how_we_deliver_locators import Issue0012HowWeDeliverLocators


class Issue0012HowWeDeliverPage:
    """Page object for How We Deliver section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0012HowWeDeliverLocators()
        self.locators.page = page

    def view_how_we_deliver_section(self) -> None:
        """Scroll to the How We Deliver section."""
        self.locators.how_we_deliver_section.scroll_into_view_if_needed()

    def section_heading_should_be_visible(self) -> None:
        """Verify section heading is visible."""
        expect(self.locators.fdce_heading).to_be_visible()

    def fdce_description_should_be_present(self) -> None:
        """Verify FDCE description is present."""
        expect(self.locators.fdce_description).to_be_visible()

    def feature_list_should_be_rendered(self) -> None:
        """Verify feature list is rendered."""
        expect(self.locators.feature_list).to_be_visible()
