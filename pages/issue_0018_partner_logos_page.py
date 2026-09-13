"""Page object for Partner logo rail/marquee rendering (issue_0018)."""
from playwright.sync_api import Page

from locators.issue_0018_partner_logos_locators import PartnerLogosLocators


class PartnerLogosPage:
    """Page object for Partner logos functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = PartnerLogosLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def get_partner_count(self) -> int:
        return self.locators.partner_logos.count()
