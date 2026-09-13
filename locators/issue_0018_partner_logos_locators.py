"""Locators for Partner logo rail/marquee rendering (issue_0018)."""
from playwright.sync_api import Locator, Page


class PartnerLogosLocators:
    """Locators for Partner logos section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def partnerships_section(self) -> Locator:
        return self.page.get_by_text("the world's most powerful technology platforms")

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator(".partner-logo, [data-partner], img[alt*='partner']")
