"""Page object for tc_001 - Website homepage loads successfully."""
from playwright.sync_api import Page, expect

from locators.tc_001_homepage_locators import Tc001HomepageLocators


class Tc001HomepagePage:
    """Page object for the homepage."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Tc001HomepageLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def verify_homepage_loaded(self) -> None:
        """Verify the homepage loads completely."""
        expect(self.locators.header).to_be_visible()
        expect(self.locators.hero_section).to_be_visible()
        expect(self.locators.navigation).to_be_visible()
        expect(self.locators.footer).to_be_visible()
        expect(self.locators.logo).to_be_visible()

    def verify_media_assets_load(self) -> None:
        """Verify all images and media assets are visible."""
        images = self.locators.all_images
        expect(images.first).to_be_visible()

    def verify_styles_applied(self) -> None:
        """Verify CSS styles are applied correctly."""
        hero_heading = self.locators.hero_section
        expect(hero_heading).to_have_css("font-size", "48px")

    def dismiss_cookie_banner_if_present(self) -> None:
        """Dismiss the cookie consent banner if present."""
        allow_button = self.page.get_by_role("button", name="Allow all")
        if allow_button.is_visible():
            allow_button.click()
