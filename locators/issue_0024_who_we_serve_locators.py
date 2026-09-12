"""Locators for issue_0024 - Five audience entries rendering and Explore actions."""
from playwright.sync_api import Locator


class Issue0024WhoWeServeLocators:
    """Locators for Who We Serve section."""

    @property
    def who_we_serve_section(self) -> Locator:
        """Return the Who We Serve section."""
        return self.page.locator("text=Every part of healthcare has its own anatomy")

    @property
    def payer_button(self) -> Locator:
        """Return the Payer audience button."""
        return self.page.get_by_role("button", name="Payer")

    @property
    def provider_button(self) -> Locator:
        """Return the Provider audience button."""
        return self.page.get_by_role("button", name="Provider")

    @property
    def healthtech_button(self) -> Locator:
        """Return the HealthTech audience button."""
        return self.page.get_by_role("button", name="HealthTech")

    @property
    def life_sciences_button(self) -> Locator:
        """Return the Life Sciences audience button."""
        return self.page.get_by_role("button", name="Life Sciences")

    @property
    def consumer_button(self) -> Locator:
        """Return the Consumer audience button."""
        return self.page.get_by_role("button", name="Consumer")

    @property
    def explore_buttons(self) -> Locator:
        """Return all Explore buttons."""
        return self.page.get_by_role("button", name="Explore")
