"""Primary call-to-action interactions and destination checks."""

import re

from playwright.sync_api import Page, expect

from locators.tc_03_primary_cta_locators import PrimaryCtaLocators
from pages.base_page import BasePage


class PrimaryCtaPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = PrimaryCtaLocators()

    def open_homepage(self) -> None:
        self.page.goto("/")

    def select_contact_us(self) -> None:
        navigation = self.page.get_by_role(
            "navigation", name=self.locators.NAVIGATION_NAME
        )
        company = navigation.get_by_role(
            "link", name=self.locators.COMPANY_MENU, exact=True
        )
        company.click()
        contact = company.locator(
            self.locators.COMPANY_MENU_ANCESTOR
        ).locator(self.locators.CONTACT_LINK)
        expect(contact).to_be_visible()
        contact.click()

    def assert_contact_destination(self) -> None:
        expect(self.page).to_have_url(re.compile(r"/contact/(?:[?#].*)?$"))
        expect(
            self.page.get_by_role(
                "heading", name=self.locators.CONTACT_HEADING, level=2
            )
        ).to_be_visible()

    def open_partners_page(self) -> None:
        self.page.goto(self.locators.PARTNERS_PATH)

    def select_snowflake_learn_more(self) -> None:
        partner_heading = self.page.get_by_role(
            "heading", name=self.locators.SNOWFLAKE_HEADING, level=4
        )
        partner_card = partner_heading.locator(self.locators.PARTNER_CARD)
        learn_more = partner_card.get_by_role(
            "link", name=self.locators.LEARN_MORE, exact=True
        )
        expect(learn_more).to_be_visible()
        learn_more.click()

    def assert_snowflake_destination(self) -> None:
        expected_url = re.compile(
            rf"{re.escape(self.locators.SNOWFLAKE_PATH)}(?:[?#].*)?$"
        )
        expect(self.page).to_have_url(expected_url)
        heading = self.page.get_by_role("heading", level=1)
        expect(heading).to_contain_text(
            self.locators.SNOWFLAKE_DESTINATION_HEADING
        )
