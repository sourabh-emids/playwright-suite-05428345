"""Page object for Company menu - EMIDS-LP-006"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-006_company_menu_locators import CompanyMenuLocators


class CompanyMenuPage:
    """Page object for Company menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CompanyMenuLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def open_company_menu(self) -> None:
        self.locators.company_trigger.click()

    def verify_menu_groups(self) -> None:
        expect(self.locators.about_us_group).to_be_visible()
        expect(self.locators.connect_with_us_group).to_be_visible()

    def get_company_links(self) -> list[str]:
        links = []
        for i in range(self.locators.company_links.count()):
            link = self.locators.company_links.nth(i)
            href = link.get_attribute("href")
            if href:
                links.append(href)
        return links
