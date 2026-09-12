"""Page object for TC-03 homepage calls to action."""

from playwright.sync_api import expect

from locators.tc_03_important_buttons_locators import (
    COMPANY_CONTACT_LINK,
    COMPANY_MENU_TRIGGER,
    CONNECT_LINK,
    CONTACT_PAGE_HEADING,
    HERO_OUTCOMES_CTA,
)
from pages.base_page import BasePage


class ImportantButtonsPage(BasePage):
    """Exercises the site's real high-value homepage calls to action."""

    def load_homepage(self) -> None:
        self.page.set_viewport_size({"width": 1280, "height": 900})
        self.goto("/")
        self.dismiss_cookie_banner()

    def open_contact_from_header(self) -> None:
        self.page.locator(CONNECT_LINK).click()
        expect(self.page).to_have_url("**/contact/")
        expect(self.page.locator(CONTACT_PAGE_HEADING)).to_be_visible()

    def open_contact_from_company_menu(self) -> None:
        self.page.locator(COMPANY_MENU_TRIGGER).click()
        contact_link = self.page.locator(COMPANY_CONTACT_LINK)
        expect(contact_link).to_be_visible()
        contact_link.click()
        self.assert_contact_page_open()

    def open_outcomes_cta(self) -> None:
        self.page.locator(HERO_OUTCOMES_CTA).first.click()
        self.assert_outcomes_page_open()

    def assert_contact_page_open(self) -> None:
        expect(self.page).to_have_url("**/contact/")
        expect(self.page.locator(CONTACT_PAGE_HEADING)).to_be_visible()

    def assert_outcomes_page_open(self) -> None:
        expect(self.page).to_have_url("**/forward-deployed-context-engineering/")
        expect(self.page.locator("main")).to_be_visible()
