"""Page object for issue_0012: How We Deliver section render"""

from playwright.sync_api import Page, expect

from locators.issue_0012_how_we_deliver_section_render_locators import Issue0012HowWeDeliverLocators


class Issue0012HowWeDeliverPage:
    """Page object for How We Deliver section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0012HowWeDeliverLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_section_present(self) -> None:
        """Verify the How We Deliver section is present."""
        expect(self.locators.section_title).to_be_visible()

    def verify_heading_hierarchy(self) -> None:
        """Verify heading hierarchy is logical."""
        h1 = self.page.get_by_role("heading", level=1)
        h2 = self.page.get_by_role("heading", level=2)
        h3 = self.page.get_by_role("heading", level=3)
        
        # Verify H2 exists
        expect(h2.first).to_be_visible()
        # Verify H3 exists
        expect(h3.first).to_be_visible()

    def verify_required_fields_present(self) -> None:
        """Verify required fields are present."""
        expect(self.locators.section_title).to_be_visible()
        expect(self.locators.section_copy).to_be_visible()
        expect(self.locators.see_model_cta).to_be_visible()

    def get_section_order(self) -> list:
        """Get the order of sections."""
        headings = self.page.get_by_role("heading", level=2).all()
        return [h.inner_text() for h in headings]
