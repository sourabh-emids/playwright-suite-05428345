"""Page object for issue_0004: Mobile responsive layout is usable."""
from playwright.sync_api import Page, expect

from locators.issue_0004_mobile_view_locators import MobileViewLocators


class MobileViewPage:
    """Page object for mobile view verification."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = MobileViewLocators(page)

    def set_mobile_viewport(self, width: int = 375, height: int = 667) -> None:
        self.page.set_viewport_size({"width": width, "height": height})

    def load_homepage(self) -> None:
        self.page.goto("/")
        self.dismiss_cookie_consent()

    def dismiss_cookie_consent(self) -> None:
        allow_all_button = self.page.get_by_role("button", name="Allow all")
        if allow_all_button.is_visible():
            allow_all_button.click()

    def verify_logo_visible(self) -> None:
        expect(self.locators.emids_logo).to_be_visible()

    def verify_main_heading_visible(self) -> None:
        expect(self.locators.main_heading).to_be_visible()

    def verify_footer_visible(self) -> None:
        expect(self.locators.footer_content).to_be_visible()

    def verify_cta_button_visible(self) -> None:
        expect(self.locators.hero_cta).to_be_visible()

    def verify_navigation_visible(self) -> None:
        expect(self.locators.nav_menu_button).to_be_visible()

    def verify_navigation_menu_visible(self) -> None:
        expect(self.locators.nav_menu_button).to_be_visible()

    def verify_buttons_visible(self) -> None:
        expect(self.locators.hero_cta).to_be_visible()
