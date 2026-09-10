"""Page object for primary homepage calls to action."""

import re

from playwright.sync_api import expect

from locators.issue_0003_primary_actions_locators import (
    PrimaryActionsLocators,
)
from pages.issue_0001_website_homepage_page import WebsiteHomepagePage


class PrimaryActionsPage(WebsiteHomepagePage):
    def select_action(self, action_name: str) -> None:
        action = self.page.locator(
            PrimaryActionsLocators.ACTIONS[action_name]
        )
        expect(action).to_be_visible()
        expect(action).to_have_text(action_name)
        action.click()

    def verify_path(self, expected_path: str) -> None:
        expect(self.page).to_have_url(
            re.compile(rf".*{re.escape(expected_path)}(?:[?#].*)?$")
        )
