"""Locators for Footer legal navigation rendering (issue_0045)."""
from playwright.sync_api import Locator, Page


class FooterLegalLocators:
    """Locators for Footer legal navigation elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")

    @property
    def privacy_link(self) -> Locator:
        return self.page.get_by_role("link", name=re.compile("Privacy", re.IGNORECASE)).last

    @property
    def legal_links(self) -> Locator:
        return self.page.locator("footer a")
