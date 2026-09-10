import re

from playwright.sync_api import Page, expect

from locators.issue_0003_cta_locators import Issue0003CtaLocators
from pages.base_page import BasePage


class Issue0003CtaPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.expected_path = "/"

    def open(self) -> None:
        self.page.goto("/")
        self._dismiss_cookie_banner()

    def select_contact_cta(self) -> None:
        self.page.get_by_role("banner").get_by_role(
            "link",
            name=Issue0003CtaLocators.CONTACT_CTA,
            exact=True,
        ).click()
        self.expected_path = Issue0003CtaLocators.CONTACT_PATH

    def select_learn_more_cta(self) -> None:
        self.page.get_by_role("main").get_by_role(
            "link",
            name=Issue0003CtaLocators.LEARN_MORE_CTA,
            exact=True,
        ).click()
        self.expected_path = Issue0003CtaLocators.LEARN_MORE_PATH

    def assert_expected_destination_opened(self) -> None:
        expect(self.page).to_have_url(
            re.compile(
                rf".*{re.escape(self.expected_path)}(?:[?#].*)?$"
            )
        )
        expect(self.page.locator("main")).to_be_visible()

    def _dismiss_cookie_banner(self) -> None:
        allow_button = self.page.get_by_role(
            "button",
            name=Issue0003CtaLocators.COOKIE_ALLOW_BUTTON,
            exact=True,
        )
        if allow_button.is_visible():
            allow_button.click()
