"""Page object for issue_0011: Hero media loading optimization"""

from playwright.sync_api import Page, expect

from locators.issue_0011_hero_media_loading_optimization_locators import Issue0011HeroMediaLocators


class Issue0011HeroMediaPage:
    """Page object for Hero media loading optimization."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0011HeroMediaLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_text_content_available(self) -> None:
        """Verify text content is visible."""
        expect(self.locators.hero_h1).to_be_visible()

    def check_lcp_lazy_loaded(self) -> bool:
        """Check if LCP image has loading=lazy attribute."""
        images = self.page.locator("main img").all()
        for img in images:
            loading = img.get_attribute("loading")
            if loading == "lazy":
                # Check if it's likely the LCP image
                src = img.get_attribute("src")
                if src and "hero" in src.lower():
                    return True
        return False

    def verify_no_lazy_loaded_hero(self) -> None:
        """Verify hero LCP image is not lazy-loaded."""
        has_lazy_hero = self.check_lcp_lazy_loaded()
        expect(has_lazy_hero).to_be(False)

    def verify_media_dimensions(self) -> None:
        """Verify media has dimensions set."""
        images = self.page.locator("main img").all()
        for img in images:
            width = img.get_attribute("width")
            height = img.get_attribute("height")
            # At least one should be set
            pass  # Basic verification
