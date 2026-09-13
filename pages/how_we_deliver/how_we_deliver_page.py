"""Page object for emids_lp_012: Render How We Deliver section."""
from playwright.sync_api import Page, expect
from locators.emids_lp_012_how_we_deliver_locators import HowWeDeliverLocators


class HowWeDeliverPage:
    """How We Deliver section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HowWeDeliverLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        """Scroll to How We Deliver section."""
        self.locators.section_heading.scroll_into_view_if_needed()

    def get_heading_hierarchy(self) -> dict:
        """Get heading hierarchy on page."""
        h2s = self.locators.all_h2s.all()
        h3s = self.locators.all_h3s.all()
        return {
            "h2_count": len(h2s),
            "h3_count": len(h3s),
        }

    def click_see_model_cta(self) -> None:
        """Click the See the model CTA."""
        self.locators.see_model_cta.click()

    def is_heading_logical(self) -> bool:
        """Check if heading hierarchy is logical."""
        hierarchy = self.get_heading_hierarchy()
        # Should have H2 before H3
        return hierarchy["h2_count"] > 0

    def is_section_content_visible(self) -> bool:
        """Check if all section content is visible."""
        return (
            self.locators.main_heading.is_visible()
            and self.locators.body_copy.is_visible()
        )
