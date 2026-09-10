import re

from playwright.sync_api import Page, expect

from locators.issue_0004_mobile_locators import Issue0004MobileLocators
from pages.base_page import BasePage


class Issue0004MobilePage(BasePage):
    @property
    def mobile_menu_toggle(self):
        return self.page.get_by_role(
            "button",
            name=Issue0004MobileLocators.MOBILE_MENU_TOGGLE,
            exact=True,
        )

    @property
    def mobile_menu(self):
        return self.page.locator(Issue0004MobileLocators.MOBILE_MENU)

    def open_at_mobile_size(self, width: int, height: int) -> None:
        self.page.set_viewport_size({"width": width, "height": height})
        self.page.goto("/")
        self._dismiss_cookie_banner()

    def assert_core_content_visible(self) -> None:
        header = self.page.get_by_role("banner")
        expect(
            header.get_by_role(
                "img",
                name=Issue0004MobileLocators.LOGO_NAME,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role(
                "heading",
                name=Issue0004MobileLocators.HERO_HEADING,
                exact=True,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role("main").get_by_role(
                "link",
                name=Issue0004MobileLocators.HERO_CTA,
                exact=True,
            )
        ).to_be_visible()
        expect(self.mobile_menu_toggle).to_be_visible()

    def open_mobile_menu(self) -> None:
        self.mobile_menu_toggle.click()

    def assert_mobile_navigation_usable(self) -> None:
        expect(
            self.mobile_menu.get_by_role(
                "button",
                name=Issue0004MobileLocators.SOLUTIONS_MENU_ITEM,
                exact=True,
            )
        ).to_be_visible()
        expect(
            self.mobile_menu.get_by_role(
                "link",
                name=Issue0004MobileLocators.CONTACT_CTA,
                exact=True,
            )
        ).to_be_visible()

    def close_menu_and_select_hero_cta(self) -> None:
        self.mobile_menu_toggle.click()
        self.page.get_by_role("main").get_by_role(
            "link",
            name=Issue0004MobileLocators.HERO_CTA,
            exact=True,
        ).click()

    def assert_hero_destination_opened(self) -> None:
        expect(self.page).to_have_url(
            re.compile(
                rf".*{re.escape(Issue0004MobileLocators.HERO_DESTINATION)}"
                r"(?:[?#].*)?$"
            )
        )
        expect(self.page.locator("main")).to_be_visible()

    def _dismiss_cookie_banner(self) -> None:
        allow_button = self.page.get_by_role(
            "button",
            name=Issue0004MobileLocators.COOKIE_ALLOW_BUTTON,
            exact=True,
        )
        if allow_button.is_visible():
            allow_button.click()
