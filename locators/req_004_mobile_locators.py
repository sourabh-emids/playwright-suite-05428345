"""Locators for REQ-004: Website displays correctly on mobile viewport."""

from playwright.sync_api import Page, Locator


class Req004MobileLocators:
    """Locators for mobile viewport elements."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def mobile_menu_toggle(self) -> Locator:
        """Mobile menu toggle button."""
        return self._page.get_by_role("button", name="Toggle mobile menu")

    @property
    def emids_logo(self) -> Locator:
        """Emids logo."""
        return self._page.get_by_role("link", name="Emids logo").first

    @property
    def main_heading(self) -> Locator:
        """Main heading on homepage."""
        return self._page.get_by_role("heading", level=1).first

    @property
    def contact_heading(self) -> Locator:
        """Contact heading on contact page."""
        return self._page.get_by_role("heading", name="Let's Connect")

    @property
    def cookie_banner(self) -> Locator:
        """Cookie consent banner."""
        return self._page.get_by_role("region", name="This website uses cookies")

    @property
    def allow_all_cookies_button(self) -> Locator:
        """Allow all cookies button."""
        return self._page.get_by_role("button", name="Allow all")

    @property
    def connect_nav_link(self) -> Locator:
        """Connect navigation link."""
        return self._page.get_by_role("link", name="Connect").first

    @property
    def mobile_menu(self) -> Locator:
        """Mobile navigation menu container."""
        return self._page.locator(".mobile-nav, .mobile-menu, nav.mobile, [class*='mobile-nav']").first

    @property
    def solutions_mobile_button(self) -> Locator:
        """Solutions button in mobile menu."""
        return self._page.locator("button:has-text('Solutions')").first

    @property
    def capabilities_mobile_button(self) -> Locator:
        """Capabilities button in mobile menu."""
        return self._page.locator("button:has-text('Capabilities')").first

    @property
    def industries_mobile_button(self) -> Locator:
        """Industries button in mobile menu."""
        return self._page.locator("button:has-text('Industries')").first

    @property
    def insights_mobile_button(self) -> Locator:
        """Insights button in mobile menu."""
        return self._page.locator("button:has-text('Insights')").first

    @property
    def company_mobile_button(self) -> Locator:
        """Company button in mobile menu."""
        return self._page.locator("button:has-text('Company')").first

    @property
    def footer(self) -> Locator:
        """Footer section."""
        return self._page.get_by_role("contentinfo")
