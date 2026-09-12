"""Locators for issue_0018 - Partner logo rail rendering and accessibility."""
from playwright.sync_api import Locator


class Issue0018PartnerLogoRailLocators:
    """Locators for Partner logo rail."""

    @property
    def partnerships_section(self) -> Locator:
        """Return the Partnerships section."""
        return self.page.locator("text=We've assembled the world's most powerful technology platforms")

    @property
    def partner_logos(self) -> Locator:
        """Return the partner logos."""
        return self.partnerships_section.locator("..").locator("img")
