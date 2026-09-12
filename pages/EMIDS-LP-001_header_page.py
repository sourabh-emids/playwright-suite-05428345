"""Page object for Header section - EMIDS-LP-001"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-001_header_locators import HeaderLocators


class HeaderPage:
    """Page object for header functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeaderLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def click_logo(self) -> None:
        self.locators.emids_logo.click()

    def click_nav_item(self, name: str) -> None:
        nav_map = {
            "Solutions": self.locators.solutions_nav,
            "Capabilities": self.locators.capabilities_nav,
            "Industries": self.locators.industries_nav,
            "Insights": self.locators.insights_nav,
            "Company": self.locators.company_nav,
        }
        if name in nav_map:
            nav_map[name].click()

    def click_connect_cta(self) -> None:
        self.locators.header_connect_cta.click()

    def get_nav_item_count(self) -> int:
        return self.locators.all_nav_items.count()

    def verify_header_visible(self) -> None:
        expect(self.locators.header_element).to_be_visible()

    def verify_nav_item_visible(self, name: str) -> None:
        self.click_nav_item(name)

    def tab_through_navigation(self) -> list[str]:
        focused_elements = []
        self.page.keyboard.press("Tab")
        for _ in range(20):
            focused = self.page.evaluate("document.activeElement.tagName + ':' + document.activeElement.textContent.trim()")
            focused_elements.append(focused)
            self.page.keyboard.press("Tab")
        return focused_elements
