"""Page object for public Emids website journeys."""
import re
from typing import Optional

from playwright.sync_api import ConsoleMessage, Error, Page, Response, expect

from locators.emids_locators import EmidsLocators as L
from pages.base_page import BasePage


class EmidsPage(BasePage):
    """All UI operations and web-first assertions for the covered journeys."""

    def __init__(self, page: Page):
        super().__init__(page)
        self._console_errors: list[str] = []
        self._page_errors: list[str] = []
        self._monitoring_errors = False
        self._last_response: Optional[Response] = None

    def _start_error_monitoring(self) -> None:
        if self._monitoring_errors:
            return
        self._monitoring_errors = True
        self.page.on("console", self._record_console_error)
        self.page.on("pageerror", self._record_page_error)

    def _record_console_error(self, message: ConsoleMessage) -> None:
        if message.type == "error":
            self._console_errors.append(message.text)

    def _record_page_error(self, error: Error) -> None:
        self._page_errors.append(str(error))

    def open_home(self) -> None:
        self._start_error_monitoring()
        self._last_response = self.page.goto("/")

    def assert_homepage_loaded_without_obvious_errors(self) -> None:
        assert self._last_response is not None, "The homepage navigation did not return a response"
        assert self._last_response.ok, (
            f"Homepage returned HTTP {self._last_response.status} "
            f"{self._last_response.status_text}"
        )
        expect(self.page).to_have_title(re.compile(L.HOME_TITLE_PATTERN, re.IGNORECASE))
        expect(self.page.locator(L.MAIN)).to_be_visible()
        expect(self.page.get_by_role("heading", name=L.HOME_HEADING, exact=True)).to_be_visible()
        assert not self._console_errors, f"Browser console errors: {self._console_errors}"
        assert not self._page_errors, f"Uncaught page errors: {self._page_errors}"

    def open_navigation_destination(self, menu_name: str, item_name: str) -> None:
        navigation = self.page.get_by_role("navigation", name=L.MAIN_NAVIGATION_NAME)
        navigation.get_by_role("link", name=menu_name, exact=True).click()
        open_menu = self.page.locator(L.ACTIVE_MEGA_MENU)
        expect(open_menu).to_be_visible()
        open_menu.locator(L.NAVIGATION_DESTINATIONS[item_name]).click()

    def assert_path_opened(self, expected_path: str) -> None:
        normalized = expected_path.rstrip("/")
        expect(self.page).to_have_url(
            re.compile(rf"^https?://[^/]+{re.escape(normalized)}/?(?:[?#].*)?$")
        )
        expect(self.page.locator(L.MAIN)).to_be_visible()

    def open_contact_from_company_menu(self) -> None:
        navigation = self.page.get_by_role("navigation", name=L.MAIN_NAVIGATION_NAME)
        navigation.get_by_role("link", name=L.COMPANY_MENU_NAME, exact=True).click()
        open_menu = self.page.locator(L.ACTIVE_MEGA_MENU)
        expect(open_menu).to_be_visible()
        open_menu.locator(L.CONTACT_DESTINATION).click()

    def assert_contact_page_opened(self) -> None:
        self.assert_path_opened(L.CONTACT_PATH)
        expect(self.page.get_by_role("heading", name=L.CONTACT_HEADING, exact=True)).to_be_visible()

    def open_partners_page(self) -> None:
        self.page.goto(L.PARTNERS_PATH)
        expect(self.page.get_by_role("heading", name=L.PARTNERS_HEADING, exact=True)).to_be_visible()

    def open_snowflake_with_learn_more(self) -> None:
        snowflake_card = self.page.locator(L.PARTNER_CARD).filter(
            has=self.page.get_by_role("heading", name=L.SNOWFLAKE_HEADING, exact=True)
        )
        expect(snowflake_card).to_be_visible()
        snowflake_card.get_by_role("link", name=L.LEARN_MORE_NAME, exact=True).click()

    def assert_snowflake_partner_page_opened(self) -> None:
        self.assert_path_opened(L.SNOWFLAKE_PATH)
        expect(
            self.page.get_by_role("heading", name=re.compile("Snowflake", re.IGNORECASE)).first
        ).to_be_visible()

    def use_mobile_viewport(self) -> None:
        self.page.set_viewport_size(L.MOBILE_VIEWPORT)

    def assert_mobile_home_content_visible(self) -> None:
        expect(self.page.get_by_role("link", name=L.HEADER_LOGO_NAME).first).to_be_visible()
        expect(self.page.get_by_role("img", name=L.HEADER_LOGO_NAME).first).to_be_visible()
        expect(self.page.get_by_role("heading", name=L.HOME_HEADING, exact=True)).to_be_visible()
        expect(self.page.get_by_role("link", name=L.HERO_CTA_NAME, exact=True)).to_be_visible()
        expect(self.page.locator(L.MOBILE_MENU_TOGGLE)).to_be_visible()

    def open_mobile_menu(self) -> None:
        self.page.locator(L.MOBILE_MENU_TOGGLE).click()
        mobile_menu = self.page.locator(L.ACTIVE_MOBILE_MENU)
        expect(mobile_menu).to_be_visible()
        for item_name in L.MOBILE_MENU_ITEMS:
            expect(mobile_menu.get_by_role("button", name=item_name, exact=True)).to_be_visible()
        expect(mobile_menu.get_by_role("link", name=L.CONNECT_NAME, exact=True)).to_be_visible()

    def use_mobile_connect_link(self) -> None:
        mobile_menu = self.page.locator(L.ACTIVE_MOBILE_MENU)
        mobile_menu.get_by_role("link", name=L.CONNECT_NAME, exact=True).click()

    def open_contact_form(self) -> None:
        self.page.goto(L.CONTACT_PATH)
        expect(self.page.locator(L.CONTACT_FORM)).to_be_visible()

    def assert_required_fields_are_empty(self) -> None:
        required_fields = self.page.locator(L.CONTACT_FORM).locator(L.REQUIRED_FIELDS)
        expect(required_fields).to_have_count(8)
        for index in range(required_fields.count()):
            expect(required_fields.nth(index)).to_have_value("")

    def submit_contact_form(self) -> None:
        self.page.locator(L.CONTACT_FORM).locator(L.SUBMIT_BUTTON).click()

    def assert_required_validation_is_clear(self) -> None:
        alert = self.page.locator(L.CONTACT_FORM).locator(L.VALIDATION_ALERT)
        expect(alert).to_be_visible()
        expect(alert).to_have_text(L.REQUIRED_MESSAGE)
        expect(self.page).to_have_url(re.compile(r"/contact/?(?:[?#].*)?$"))
