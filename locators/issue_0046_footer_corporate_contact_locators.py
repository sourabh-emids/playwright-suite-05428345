"""Locators for issue_0046 - Footer corporate contact information rendering."""
from playwright.sync_api import Locator


class Issue0046FooterCorporateContactLocators:
    """Locators for footer corporate contact."""

    @property
    def footer_logo(self) -> Locator:
        """Return the footer logo."""
        return self.page.locator("footer").get_by_role("link", name="Emids logo")

    @property
    def footer_connect_link(self) -> Locator:
        """Return the footer Connect link."""
        return self.page.locator("footer").get_by_role("link", name="Connect")
