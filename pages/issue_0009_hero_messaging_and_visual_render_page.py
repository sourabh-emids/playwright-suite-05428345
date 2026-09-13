"""Page object for issue_0009: Hero messaging and visual render"""

from playwright.sync_api import Page, expect

from locators.issue_0009_hero_messaging_and_visual_render_locators import Issue0009HeroLocators


class Issue0009HeroPage:
    """Page object for Hero messaging and visual render."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0009HeroLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def resize_to_desktop(self) -> None:
        """Resize to desktop viewport."""
        self.page.set_viewport_size({"width": 1280, "height": 720})

    def verify_h1_present(self) -> None:
        """Verify H1 is present and contains expected text."""
        expect(self.locators.h1).to_be_visible()
        expect(self.locators.h1).to_contain_text("In Healthcare, Only Outcomes Matter")

    def count_h1_elements(self) -> int:
        """Count the number of H1 elements."""
        return self.page.get_by_role("heading", level=1).count()

    def verify_h1_is_unique(self) -> None:
        """Verify only one H1 exists."""
        count = self.count_h1_elements()
        expect(count).to_be(1)

    def verify_cta_visible(self) -> None:
        """Verify hero CTA is visible."""
        expect(self.locators.hero_cta).to_be_visible()

    def get_h1_content(self) -> str:
        """Get H1 text content."""
        return self.locators.h1.inner_text()
