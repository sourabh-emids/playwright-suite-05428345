import re
from urllib.parse import urljoin

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

from locators.tc_01_tc_02_tc_03_tc_04_tc_05_emids_locators import (
    EmidsLocators,
)


class EmidsPage:
    MOBILE_WIDTH = 390
    MOBILE_HEIGHT = 844

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open_home(self) -> None:
        self._open("/")

    def open_contact(self) -> None:
        self._open("/contact/")
        expect(self.page.locator(EmidsLocators.CONTACT_FORM)).to_be_visible(
            timeout=15_000
        )

    def _open(self, path: str) -> None:
        response = self.page.goto(
            urljoin(f"{self.base_url}/", path.lstrip("/")),
            wait_until="domcontentloaded",
        )
        assert response is not None and response.ok, (
            f"Expected a successful response for {path}"
        )
        self._accept_cookie_consent_if_present()

    def _accept_cookie_consent_if_present(self) -> None:
        allow_all = self.page.get_by_role(
            "button", name="Allow all", exact=True
        )
        try:
            allow_all.wait_for(state="visible", timeout=3_000)
        except PlaywrightTimeoutError:
            return
        allow_all.click()

    def assert_homepage_loaded(self) -> None:
        expect(self.page).to_have_title(re.compile(r"Emids", re.IGNORECASE))
        expect(self.page).to_have_url(self._url_pattern("/"))
        expect(self.page.locator(EmidsLocators.MAIN)).to_be_visible()
        expect(
            self.page.get_by_role(
                "heading", name=EmidsLocators.HOME_HEADING, exact=True
            )
        ).to_be_visible()
        logo = self.page.locator(EmidsLocators.HEADER_LOGO).first
        expect(logo).to_be_visible()
        assert logo.evaluate("element => element.naturalWidth > 0")
        expect(
            self.page.get_by_role(
                "link", name=EmidsLocators.HERO_CTA, exact=True
            )
        ).to_be_visible()
        error_heading = self.page.get_by_role(
            "heading",
            name=re.compile(
                EmidsLocators.ERROR_HEADING_PATTERN,
                re.IGNORECASE,
            ),
        )
        expect(error_heading).to_have_count(0)
        assert not self._has_horizontal_overflow()

    def assert_main_navigation_available(self) -> None:
        navigation = self.page.locator(EmidsLocators.MAIN_NAVIGATION)
        expect(navigation).to_be_visible()

    def select_navigation_destination(
        self, menu_name: str, destination: str
    ) -> None:
        menu_key = menu_name.lower()
        trigger = self.page.locator(
            EmidsLocators.NAV_TRIGGER.format(menu=menu_key)
        )
        expect(trigger).to_be_visible()
        trigger.click()
        expect(trigger).to_have_attribute("aria-expanded", "true")

        menu = self.page.locator(
            EmidsLocators.NAV_MENU.format(menu=menu_key)
        )
        expect(menu).to_be_visible()
        destination_name = re.compile(
            EmidsLocators.NAV_DESTINATION_NAME.format(
                label=re.escape(destination)
            )
        )
        link = menu.get_by_role("link", name=destination_name)
        expect(link).to_be_visible()
        link.click()

    def select_primary_cta(self, action: str) -> None:
        if action == "Connect":
            cta = self.page.locator(EmidsLocators.HEADER_CONNECT)
        else:
            cta = self.page.get_by_role("link", name=action, exact=True)
        expect(cta).to_be_visible()
        expect(cta).to_be_enabled()
        cta.click()

    def assert_destination(self, path: str, heading: str) -> None:
        expect(self.page).to_have_url(self._url_pattern(path))
        expect(self.page.locator(EmidsLocators.MAIN)).to_be_visible()
        expect(
            self.page.get_by_role("heading", name=heading, exact=True)
        ).to_be_visible()

    def use_mobile_viewport(self) -> None:
        self.page.set_viewport_size(
            {"width": self.MOBILE_WIDTH, "height": self.MOBILE_HEIGHT}
        )

    def open_mobile_menu(self) -> None:
        button = self.page.locator(EmidsLocators.MOBILE_MENU_BUTTON)
        expect(button).to_be_visible()
        expect(button).to_be_enabled()
        button.click()

    def assert_mobile_homepage_and_menu_usable(self) -> None:
        expect(
            self.page.get_by_role(
                "heading", name=EmidsLocators.HOME_HEADING, exact=True
            )
        ).to_be_visible()
        logo = self.page.locator(EmidsLocators.HEADER_LOGO).first
        expect(logo).to_be_visible()
        assert logo.evaluate("element => element.naturalWidth > 0")
        expect(
            self.page.get_by_role(
                "link", name=EmidsLocators.HERO_CTA, exact=True
            )
        ).to_be_visible()
        expect(self.page.locator(EmidsLocators.MOBILE_MENU)).to_be_visible()
        expect(
            self.page.locator(EmidsLocators.MOBILE_CONNECT)
        ).to_be_visible()
        assert not self._has_horizontal_overflow()

    def select_mobile_connect(self) -> None:
        connect = self.page.locator(EmidsLocators.MOBILE_CONNECT)
        expect(connect).to_be_enabled()
        connect.click()

    def assert_mobile_contact_page_usable(self) -> None:
        self.assert_destination("/contact/", "Let's Connect")
        assert not self._has_horizontal_overflow()

    def assert_required_fields_empty(self) -> None:
        fields = self.page.locator(EmidsLocators.REQUIRED_FIELDS)
        expect(fields).to_have_count(8)
        for index in range(fields.count()):
            expect(fields.nth(index)).to_have_value("")

    def submit_contact_form(self) -> None:
        submit = self.page.locator(EmidsLocators.CONTACT_SUBMIT)
        expect(submit).to_be_enabled()
        submit.click()

    def assert_all_required_validation_messages(self) -> None:
        expect(self.page).to_have_url(self._url_pattern("/contact/"))
        expect(self.page.locator(EmidsLocators.CONTACT_FORM)).to_be_visible()

        fields = self.page.locator(EmidsLocators.REQUIRED_FIELDS)
        for index in range(fields.count()):
            field = fields.nth(index)
            expect(field).to_have_attribute("aria-invalid", "true")
            message_id = field.get_attribute("aria-describedby")
            assert message_id, "Required field has no validation message"
            message = self.page.locator(f"#{message_id}")
            expect(message).to_be_visible()
            expect(message).to_have_text(EmidsLocators.REQUIRED_MESSAGE)

    def _has_horizontal_overflow(self) -> bool:
        return self.page.evaluate(
            "document.documentElement.scrollWidth "
            "> document.documentElement.clientWidth"
        )

    def _url_pattern(self, path: str) -> re.Pattern[str]:
        expected = f"{self.base_url}{path}"
        return re.compile(rf"^{re.escape(expected)}(?:[?#].*)?$")
