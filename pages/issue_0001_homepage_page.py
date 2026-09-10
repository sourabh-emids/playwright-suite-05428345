import re

from playwright.sync_api import Page, Response, expect

from locators.issue_0001_homepage_locators import (
    Issue0001HomepageLocators,
)
from pages.base_page import BasePage


class Issue0001HomepagePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._response: Response | None = None

    @property
    def hero_heading(self):
        return self.page.get_by_role(
            "heading",
            name=Issue0001HomepageLocators.HERO_HEADING,
            exact=True,
        )

    @property
    def header_logo(self):
        return self.page.get_by_role("banner").get_by_role(
            "img",
            name=Issue0001HomepageLocators.LOGO_NAME,
        )

    def open(self) -> None:
        self._response = self.page.goto("/")
        self._dismiss_cookie_banner()

    def assert_loaded_without_obvious_errors(self) -> None:
        assert self._response is not None, "Homepage returned no response"
        assert self._response.ok, (
            f"Homepage returned HTTP {self._response.status}"
        )
        expect(self.page).to_have_title(re.compile(r"\bEmids\b", re.I))
        expect(self.page.locator(Issue0001HomepageLocators.MAIN)).to_be_visible()
        expect(self.header_logo).to_be_visible()
        expect(self.hero_heading).to_be_visible()
        errors = self.page.get_by_text(
            re.compile(
                Issue0001HomepageLocators.ERROR_TEXT_PATTERN,
                re.I,
            )
        )
        expect(errors).to_have_count(0)

    def _dismiss_cookie_banner(self) -> None:
        allow_button = self.page.get_by_role(
            "button",
            name=Issue0001HomepageLocators.COOKIE_ALLOW_BUTTON,
            exact=True,
        )
        if allow_button.is_visible():
            allow_button.click()
