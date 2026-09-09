"""Page object for homepage primary calls to action."""

import re

from playwright.sync_api import Locator, Page, expect

from locators.issue_0003_primary_cta_locators import (
    PrimaryCallToActionLocators,
)
from pages.issue_0001_homepage_availability_page import (
    HomepageAvailabilityPage,
)


class PrimaryCallToActionPage(HomepageAvailabilityPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cta_locators = PrimaryCallToActionLocators

    def select_call_to_action(self, name: str) -> None:
        call_to_action = self._call_to_action(name)
        expect(call_to_action).to_be_visible()
        expect(call_to_action).to_be_enabled()
        call_to_action.click()

    def assert_destination(self, path: str, heading: str) -> None:
        expect(self.page).to_have_url(
            re.compile(rf".*{re.escape(path)}(?:[?#].*)?$")
        )
        expect(
            self.page.get_by_role(
                "heading",
                name=heading,
                exact=True,
            )
        ).to_be_visible()

    def _call_to_action(self, name: str) -> Locator:
        main = self.page.get_by_role("main")
        if name == self.cta_locators.HERO:
            return main.get_by_role("link", name=name, exact=True)
        if name == self.cta_locators.ALL_SOLUTIONS:
            return main.get_by_role("link", name=name, exact=True)
        if name == self.cta_locators.CONNECT:
            return self.page.get_by_role("banner").get_by_role(
                "link",
                name=name,
                exact=True,
            )
        raise ValueError(f"Unknown primary call to action: {name}")
