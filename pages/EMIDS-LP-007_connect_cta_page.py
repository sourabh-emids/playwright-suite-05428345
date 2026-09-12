"""Page object for Connect CTA - EMIDS-LP-007"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-007_connect_cta_locators import ConnectCTALocators


class ConnectCTAPage:
    """Page object for Connect CTA functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ConnectCTALocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def click_header_connect(self) -> None:
        self.locators.header_connect_cta.click()

    def verify_connect_cta_visible(self) -> None:
        expect(self.locators.header_connect_cta).to_be_visible()

    def get_connect_url(self) -> str:
        return self.locators.header_connect_cta.get_attribute("href")

    def verify_https(self) -> bool:
        url = self.get_connect_url()
        return url and url.startswith("https://")

    def focus_and_activate(self) -> None:
        self.locators.header_connect_cta.focus()
        self.page.keyboard.press("Enter")
