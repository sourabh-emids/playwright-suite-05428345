"""Page object for the Emids homepage."""
from playwright.sync_api import Page, expect, Locator

from locators.homepage_locators import HomePageLocators


class HomePage:
    """Page object for the Emids homepage."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators(page)

    def goto(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    # Header methods
    def click_emids_logo(self) -> None:
        """Click the Emids logo."""
        self.locators.emids_logo.click()

    def open_solutions_menu(self) -> None:
        """Open the Solutions mega-menu."""
        self.locators.solutions_menu_button.click()

    def open_capabilities_menu(self) -> None:
        """Open the Capabilities mega-menu."""
        self.locators.capabilities_menu_button.click()

    def open_industries_menu(self) -> None:
        """Open the Industries menu."""
        self.locators.industries_menu_button.click()

    def open_insights_menu(self) -> None:
        """Open the Insights menu."""
        self.locators.insights_menu_button.click()

    def open_company_menu(self) -> None:
        """Open the Company menu."""
        self.locators.company_menu_button.click()

    def click_header_connect_cta(self) -> None:
        """Click the Connect CTA in the header."""
        self.locators.header_connect_cta.click()

    def navigate_to_solutions_menu_item(self, index: int = 0) -> None:
        """Navigate to a solutions menu item by index."""
        menu_items = self.page.locator("[class*='solutions'] a").all()
        if index < len(menu_items):
            menu_items[index].click()

    # Hero methods
    def click_hero_cta(self) -> None:
        """Click the hero CTA."""
        self.locators.hero_cta.click()

    # How We Deliver methods
    def click_see_the_model_cta(self) -> None:
        """Click the 'See the model' CTA."""
        self.locators.see_the_model_cta.click()

    # Featured Solutions methods
    def click_all_solutions_cta(self) -> None:
        """Click the 'All solutions' CTA."""
        self.locators.all_solutions_cta.click()

    def get_featured_solution_count(self) -> int:
        """Get the number of featured solution cards."""
        return self.page.locator('[href*="/solutions/"]').filter(
            has_text=["01", "02", "03", "04", "05", "06"]
        ).count()

    # Who We Serve methods
    def click_audience_button(self, audience: str) -> None:
        """Click an audience button."""
        self.page.get_by_role("button", name=audience).click()

    # Insights methods
    def navigate_insights_carousel(self) -> None:
        """Navigate the insights carousel."""
        self.locators.insights_next_button.click()

    # Cookie consent methods
    def accept_all_cookies(self) -> None:
        """Accept all cookies."""
        if self.locators.allow_all_cookies_button.is_visible():
            self.locators.allow_all_cookies_button.click()

    def open_cookie_preferences(self) -> None:
        """Open cookie preferences."""
        self.locators.cookie_preferences_button.click()

    # Navigation verification
    def verify_navigation_has_links(self) -> None:
        """Verify all navigation items have valid links."""
        nav_links = self.locators.navigation.get_by_role("link").all()
        for link in nav_links:
            href = link.get_attribute("href")
            assert href is not None and href != "", f"Navigation link has no href: {link}"

    def keyboard_navigate_to_nav_item(self, item_name: str) -> None:
        """Navigate to a nav item using keyboard."""
        self.locators.navigation.get_by_text(item_name).focus()
        self.page.keyboard.press("Enter")

    # Responsive methods
    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 320, "height": 568})

    def resize_to_desktop(self) -> None:
        """Resize to desktop viewport."""
        self.page.set_viewport_size({"width": 1280, "height": 720})

    # Accessibility methods
    def get_focused_element(self) -> Locator:
        """Get the currently focused element."""
        return self.page.evaluate("() => document.activeElement")

    def press_tab(self, times: int = 1) -> None:
        """Press Tab key multiple times."""
        for _ in range(times):
            self.page.keyboard.press("Tab")

    def press_escape(self) -> None:
        """Press Escape key."""
        self.page.keyboard.press("Escape")
