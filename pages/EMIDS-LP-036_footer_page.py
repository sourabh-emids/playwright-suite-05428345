"""Page object for Footer section - EMIDS-LP-036, EMIDS-LP-045, EMIDS-LP-046"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-036_footer_locators import FooterLocators


class FooterPage:
    """Page object for Footer section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FooterLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_footer_visible(self) -> None:
        expect(self.locators.footer).to_be_visible()

    def verify_cookie_preferences(self) -> None:
        expect(self.locators.cookie_preferences).to_be_visible()

    def click_cookie_preferences(self) -> None:
        self.locators.cookie_preferences.click()

    def verify_legal_links(self) -> None:
        expect(self.locators.privacy_policy_link).to_be_visible()
        expect(self.locators.code_of_conduct_link).to_be_visible()

    def count_legal_links(self) -> int:
        return self.locators.legal_links.count()

    def get_legal_link_urls(self) -> list[str]:
        urls = []
        for i in range(self.locators.legal_links.count()):
            href = self.locators.legal_links.nth(i).get_attribute("href")
            if href:
                urls.append(href)
        return urls

    def verify_https_links(self) -> list[bool]:
        results = []
        for i in range(self.locators.legal_links.count()):
            href = self.locators.legal_links.nth(i).get_attribute("href")
            results.append(href and href.startswith("https://"))
        return results
