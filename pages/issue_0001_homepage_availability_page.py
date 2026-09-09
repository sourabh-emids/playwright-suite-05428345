"""Homepage availability page object."""

from playwright.sync_api import Page, expect

from locators.issue_0001_homepage_availability_locators import (
    HomepageAvailabilityLocators,
)
from pages.base_page import BasePage


class HomepageAvailabilityPage(BasePage):
    """Provides the common homepage loading behavior for public tests."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomepageAvailabilityLocators

    def open(self) -> None:
        response = self.page.goto("/")
        assert response is not None, "The homepage did not return a response."
        assert response.ok, (
            f"The homepage returned HTTP status {response.status}."
        )
        self._dismiss_cookie_banner()

    def assert_loaded(self) -> None:
        expect(self.page).to_have_title(self.locators.PAGE_TITLE)
        expect(self.page.get_by_role("main")).to_be_visible()
        expect(
            self.page.get_by_role(
                "heading",
                name=self.locators.HERO_HEADING,
                level=1,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role("banner").get_by_role(
                "img",
                name=self.locators.LOGO,
            )
        ).to_be_visible()

    def _dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=self.locators.COOKIE_ALLOW_ALL,
        )
        if allow_all.is_visible():
            allow_all.click()
