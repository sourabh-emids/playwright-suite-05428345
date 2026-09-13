"""Page object for issue_0004: Industries mega-menu implementation"""

from playwright.sync_api import Page, expect

from locators.issue_0004_industries_mega_menu_implementation_locators import Issue0004IndustriesMenuLocators


class Issue0004IndustriesMenuPage:
    """Page object for Industries mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0004IndustriesMenuLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def open_industries_menu(self) -> None:
        """Open the Industries menu."""
        self.locators.industries_nav_button.click()

    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})

    def verify_all_industries_visible(self) -> None:
        """Verify all five industry links are visible."""
        expect(self.locators.payer_link).to_be_visible()
        expect(self.locators.provider_link).to_be_visible()
        expect(self.locators.healthtech_link).to_be_visible()
        expect(self.locators.life_sciences_link).to_be_visible()
        expect(self.locators.consumer_link).to_be_visible()

    def get_industry_links_count(self) -> int:
        """Get the count of industry links."""
        return self.locators.get_all_industry_links().count()

    def validate_canonical_urls(self) -> bool:
        """Validate that URLs follow canonical patterns."""
        expected_patterns = [
            "/segments/payer/",
            "/segments/provider/",
            "/segments/healthtech/",
            "/segments/life-sciences/",
            "/segments/consumer/"
        ]
        links = self.locators.get_all_industry_links().all()
        hrefs = [link.get_attribute("href") for link in links]
        for pattern in expected_patterns:
            found = any(pattern in href for href in hrefs if href)
            if not found:
                return False
        return True
