"""Page object for shared Emids website and homepage behavior."""

import re

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect

from locators.emids_locators import EmidsSiteLocators
from pages.base_page import BasePage


class EmidsSitePage(BasePage):
    MOBILE_WIDTH = 390
    MOBILE_HEIGHT = 844

    def __init__(self, page: Page):
        super().__init__(page)
        self.last_response = None

    def _dismiss_cookie_banner_if_present(self) -> None:
        allow_all = self.page.get_by_role(
            "button", name=EmidsSiteLocators.COOKIE_ALLOW_ALL_NAME, exact=True
        )
        try:
            allow_all.wait_for(state="visible", timeout=1500)
        except PlaywrightTimeoutError:
            return
        allow_all.click()

    def open_home(self) -> None:
        self.last_response = self.page.goto("/", wait_until="domcontentloaded")
        self._dismiss_cookie_banner_if_present()

    def use_mobile_viewport(self) -> None:
        self.page.set_viewport_size(
            {"width": self.MOBILE_WIDTH, "height": self.MOBILE_HEIGHT}
        )

    def verify_home_loaded(self) -> None:
        assert self.last_response is not None, "The homepage returned no HTTP response"
        assert self.last_response.ok, (
            f"Homepage request failed with HTTP {self.last_response.status}"
        )
        expect(self.page).to_have_title(re.compile(r"^Emids\b", re.IGNORECASE))
        expect(
            self.page.get_by_role(
                "heading", name=EmidsSiteLocators.HOME_HERO_HEADING, exact=True
            )
        ).to_be_visible()

    def verify_no_obvious_error(self) -> None:
        expect(self.page.locator("main")).to_be_visible()
        obvious_error_heading = self.page.get_by_role(
            "heading",
            name=re.compile(
                r"(?:404|page not found|internal server error|service unavailable)",
                re.IGNORECASE,
            ),
        )
        expect(obvious_error_heading).to_have_count(0)

    def open_defined_navigation_destination(
        self, navigation_item: str, expected_path: str
    ) -> None:
        actual_path = EmidsSiteLocators.NAVIGATION_INVENTORY.get(navigation_item)
        assert actual_path == expected_path, (
            f"No matching destination inventory entry for {navigation_item!r}"
        )
        navigation = self.page.get_by_role(
            "navigation", name=EmidsSiteLocators.MAIN_NAVIGATION_NAME
        )
        navigation.get_by_role(
            "link", name=navigation_item, exact=True
        ).click()
        destination = self.page.locator(
            EmidsSiteLocators.NAV_DESTINATION_SELECTOR.format(path=expected_path)
        ).first
        expect(destination).to_be_visible()
        destination.click()

    def verify_destination_opened(self, expected_path: str) -> None:
        expect(self.page).to_have_url(
            re.compile(rf"https?://[^/]+{re.escape(expected_path)}(?:[?#].*)?$")
        )
        expect(self.page.locator("main")).to_be_visible()

    def select_contact_us(self) -> None:
        navigation = self.page.get_by_role(
            "navigation", name=EmidsSiteLocators.MAIN_NAVIGATION_NAME
        )
        navigation.get_by_role("link", name="Company", exact=True).click()
        contact_us = self.page.locator(
            EmidsSiteLocators.NAV_DESTINATION_SELECTOR.format(
                path=EmidsSiteLocators.CONTACT_US_PATH
            )
        ).first
        expect(contact_us).to_be_visible()
        contact_us.click()

    def verify_contact_page_opened(self) -> None:
        self.verify_destination_opened(EmidsSiteLocators.CONTACT_US_PATH)
        expect(
            self.page.get_by_role(
                "heading", name=EmidsSiteLocators.CONTACT_HEADING, exact=True
            )
        ).to_be_visible()

    def select_primary_home_cta(self) -> None:
        primary_cta = self.page.get_by_role(
            "link", name=EmidsSiteLocators.PRIMARY_HOME_CTA_NAME, exact=True
        )
        expect(primary_cta).to_be_visible()
        primary_cta.click()

    def verify_primary_cta_destination(self) -> None:
        self.verify_destination_opened(EmidsSiteLocators.PRIMARY_HOME_CTA_PATH)
        expect(
            self.page.get_by_role(
                "heading",
                name=EmidsSiteLocators.PRIMARY_HOME_CTA_HEADING,
                exact=True,
            )
        ).to_be_visible()

    def verify_mobile_content(self) -> None:
        expect(
            self.page.get_by_role(
                "heading", name=EmidsSiteLocators.HOME_HERO_HEADING, exact=True
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role("banner").get_by_role(
                "img", name=EmidsSiteLocators.HOME_LOGO_NAME, exact=True
            )
        ).to_be_visible()
        has_no_horizontal_overflow = self.page.evaluate(
            "() => document.documentElement.scrollWidth <= window.innerWidth"
        )
        assert has_no_horizontal_overflow, "The mobile page has horizontal overflow"

    def open_mobile_solutions_menu(self) -> None:
        mobile_menu = self.page.get_by_role(
            "button", name=EmidsSiteLocators.MOBILE_MENU_BUTTON_NAME, exact=True
        )
        expect(mobile_menu).to_be_visible()
        mobile_menu.click()

        solutions = self.page.get_by_role("button", name="Solutions", exact=True)
        expect(solutions).to_be_visible()
        solutions.click()

    def verify_mobile_solutions_menu(self) -> None:
        modernization = self.page.locator(
            EmidsSiteLocators.VISIBLE_DESTINATION_SELECTOR.format(
                path=EmidsSiteLocators.NAVIGATION_INVENTORY["Solutions"]
            )
        ).first
        expect(modernization).to_be_visible()
        expect(modernization).to_be_enabled()
