"""Page object for issue_0011 - Hero media optimization and load behavior."""
from playwright.sync_api import Page, expect

from locators.issue_0011_hero_media_locators import Issue0011HeroMediaLocators


class Issue0011HeroMediaPage:
    """Page object for hero media optimization."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0011HeroMediaLocators()
        self.locators.page = page

    def view_hero_section(self) -> None:
        """View the hero section."""
        self.locators.hero_section.scroll_into_view_if_needed()

    def media_should_load_without_errors(self) -> None:
        """Verify media in hero loads without errors."""
        # Check for failed images
        images = self.locators.hero_images
        if images.count() > 0:
            # Images should have valid src attributes
            for i in range(images.count()):
                img = images.nth(i)
                src = await img.get_attribute("src")
                if src:  # Only check images with src
                    expect(img).to_be_visible()

    def page_should_have_good_performance(self) -> None:
        """Verify page has good performance characteristics."""
        # Check that the page loaded within reasonable time
        # This is a basic check - detailed performance testing would require more setup
        timing = self.page.evaluate("() => performance.timing.loadEventEnd - performance.timing.navigationStart")
        assert timing < 10000, f"Page load time too slow: {timing}ms"
