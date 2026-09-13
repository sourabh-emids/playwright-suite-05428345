"""Locators for issue_0018: Partner logo rail render"""

from playwright.sync_api import Page, Locator


class Issue0018PartnerLogosLocators:
    """Locators for Partner logo rail."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def partnerships_section(self) -> Locator:
        """Returns the Partnerships section."""
        return self.page.get_by_text("We've assembled the world's most powerful technology platforms").locator("..")

    @property
    def partner_logos(self) -> Locator:
        """Returns partner logo images."""
        return self.page.locator("img[alt*='ServiceNow'], img[alt*='AWS'], img[alt*='Databricks']")
