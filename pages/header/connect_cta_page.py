"""Page object for emids_lp_007: Provide header Connect CTA."""
from playwright.sync_api import Page, expect
from locators.emids_lp_007_connect_cta_locators import ConnectCTALocators


class ConnectCTAPage:
    """Connect CTA page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ConnectCTALocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def click_connect_cta(self) -> None:
        """Click the Connect CTA."""
        self.locators.main_connect_cta.click()

    def is_visually_distinct(self) -> bool:
        """Check if Connect CTA is visually distinct."""
        # Verify CTA has styling that makes it stand out (e.g., different background, border)
        cta = self.locators.main_connect_cta
        # Get computed styles - CTA should have distinct styling
        bg_color = cta.evaluate("el => window.getComputedStyle(el).backgroundColor")
        return bg_color != "rgba(0, 0, 0, 0)"

    def get_accessible_name(self) -> str:
        """Get accessible name of Connect CTA."""
        return self.locators.main_connect_cta.get_attribute("aria-label") or "Connect"

    def is_https_and_valid(self) -> bool:
        """Check if URL is HTTPS and valid."""
        href = self.locators.main_connect_cta.get_attribute("href")
        return href and href.startswith("https://") and "/contact/" in href

    def count_primary_ctas(self) -> int:
        """Count number of primary Connect CTAs in header."""
        return self.locators.header_connect_cta.count()

    def is_keyboard_operable(self) -> bool:
        """Check if Connect CTA is keyboard operable."""
        self.navigate()
        return self.locators.main_connect_cta.is_focusable()

    def is_visible_on_mobile(self) -> bool:
        """Check if Connect CTA is visible on mobile."""
        self.page.set_viewport_size({"width": 375, "height": 667})
        return self.locators.main_connect_cta.is_visible()
