"""Locators for REQ-001: Homepage loads successfully."""

from playwright.sync_api import Page, Locator


class Req001HomepageLocators:
    """Locators for homepage elements."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def cookie_banner(self) -> Locator:
        """Cookie consent banner."""
        return self._page.get_by_role("region", name="This website uses cookies")

    @property
    def allow_all_cookies_button(self) -> Locator:
        """Allow all cookies button."""
        return self._page.get_by_role("button", name="Allow all")

    @property
    def main_heading(self) -> Locator:
        """Main heading on homepage."""
        return self._page.get_by_role("heading", level=1).first

    @property
    def emids_logo(self) -> Locator:
        """Emids logo in header."""
        return self._page.get_by_role("link", name="Emids logo").first

    @property
    def main_navigation(self) -> Locator:
        """Main navigation menu."""
        return self._page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_nav_button(self) -> Locator:
        """Solutions navigation button."""
        return self._page.get_by_role("navigation", name="Main Navigation").get_by_role(
            "button", name="Solutions"
        )

    @property
    def capabilities_nav_button(self) -> Locator:
        """Capabilities navigation button."""
        return self._page.get_by_role("navigation", name="Main Navigation").get_by_role(
            "button", name="Capabilities"
        )

    @property
    def industries_nav_button(self) -> Locator:
        """Industries navigation button."""
        return self._page.get_by_role("navigation", name="Main Navigation").get_by_role(
            "button", name="Industries"
        )

    @property
    def insights_nav_button(self) -> Locator:
        """Insights navigation button."""
        return self._page.get_by_role("navigation", name="Main Navigation").get_by_role(
            "button", name="Insights"
        )

    @property
    def company_nav_button(self) -> Locator:
        """Company navigation button."""
        return self._page.get_by_role("navigation", name="Main Navigation").get_by_role(
            "button", name="Company"
        )

    @property
    def connect_nav_link(self) -> Locator:
        """Connect link in navigation."""
        return self._page.get_by_role("navigation", name="Main Navigation").get_by_role(
            "link", name="Connect"
        )
