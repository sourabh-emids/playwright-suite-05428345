"""Page object for Header Connect CTA functionality (issue_0007)."""
from playwright.sync_api import Page

from locators.issue_0007_header_connect_cta_locators import HeaderConnectCTALocators


class HeaderConnectCTAPage:
    """Page object for Header Connect CTA functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeaderConnectCTALocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def click_connect(self) -> None:
        self.locators.connect_cta.click()

    def focus_connect(self) -> None:
        self.locators.connect_cta.focus()

    def get_cta_count(self) -> int:
        return len(self.locators.connect_ctas)
