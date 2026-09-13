"""Locators for issue_0004: Industries mega-menu implementation"""

from playwright.sync_api import Page, Locator


class Issue0004IndustriesMenuLocators:
    """Locators for the Industries mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def industries_nav_button(self) -> Locator:
        """Returns the Industries navigation button."""
        return self.page.get_by_role("button", name="Industries")

    @property
    def payer_link(self) -> Locator:
        """Returns the Payer link."""
        return self.page.get_by_role("link", name="Payer")

    @property
    def provider_link(self) -> Locator:
        """Returns the Provider link."""
        return self.page.get_by_role("link", name="Provider")

    @property
    def healthtech_link(self) -> Locator:
        """Returns the HealthTech link."""
        return self.page.get_by_role("link", name="HealthTech")

    @property
    def life_sciences_link(self) -> Locator:
        """Returns the Life Sciences link."""
        return self.page.get_by_role("link", name="Life Sciences")

    @property
    def consumer_link(self) -> Locator:
        """Returns the Consumer link."""
        return self.page.get_by_role("link", name="Consumer")

    def get_all_industry_links(self) -> Locator:
        """Returns all industry links."""
        return self.page.locator("a[href*='/segments/']")
