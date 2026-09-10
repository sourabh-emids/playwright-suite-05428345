"""Page object for the Emids public website and homepage."""

import re

from playwright.sync_api import Page, Response, expect

from locators.issue_0001_website_homepage_locators import (
    WebsiteHomepageLocators,
)
from pages.base_page import BasePage


class WebsiteHomepagePage(BasePage):
    """Shared public-site behavior plus homepage availability checks."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.response: Response | None = None

    def open(self, path: str = "/") -> None:
        self.response = self.page.goto(path)
        self.dismiss_cookie_banner()

    def dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=WebsiteHomepageLocators.COOKIE_ALLOW_ALL_NAME,
            exact=True,
        )
        if allow_all.is_visible():
            allow_all.click()

    def verify_homepage_loaded(self) -> None:
        assert self.response is not None, "The homepage returned no response."
        assert self.response.ok, (
            f"The homepage returned HTTP {self.response.status}."
        )
        expect(self.page).to_have_title(re.compile(r"^Emids -"))
        expect(
            self.page.locator(WebsiteHomepageLocators.MAIN)
        ).to_be_visible()
        expect(
            self.page.get_by_role(
                "heading",
                name=WebsiteHomepageLocators.HERO_HEADING_NAME,
                exact=True,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role(
                "img",
                name=WebsiteHomepageLocators.LOGO_NAME,
            ).first
        ).to_be_visible()
