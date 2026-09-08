from playwright.sync_api import Page, expect

from locators.tc_04_mobile_view_locators import Tc04MobileViewLocators
from pages.base_page import BasePage


class Tc04MobileViewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Tc04MobileViewLocators

    def use_mobile_viewport(self) -> None:
        self.page.set_viewport_size(self.locators.VIEWPORT)

    def open(self) -> None:
        self.goto("/")
        self._dismiss_cookie_banner()

    def assert_primary_content_visible(self) -> None:
        expect(
            self.page.get_by_role("banner").get_by_role(
                "img",
                name=self.locators.LOGO_NAME,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role(
                "heading",
                name=self.locators.HOME_HEADING,
                exact=True,
            )
        ).to_be_visible()
        expect(self.page.locator(self.locators.HERO_IMAGE)).to_be_visible()
        expect(
            self.page.get_by_role(
                "link",
                name=self.locators.PRIMARY_CTA_NAME,
                exact=True,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role(
                "button",
                name=self.locators.MENU_TOGGLE_NAME,
                exact=True,
            )
        ).to_be_enabled()

    def open_navigation_and_solutions(self) -> None:
        toggle = self.page.get_by_role(
            "button",
            name=self.locators.MENU_TOGGLE_NAME,
            exact=True,
        )
        toggle.click()
        mobile_menu = self.page.locator(self.locators.MOBILE_MENU)
        expect(mobile_menu).to_be_visible()

        for name in self.locators.MOBILE_MENU_ITEMS:
            expect(
                mobile_menu.get_by_role("button", name=name, exact=True)
            ).to_be_visible()

        solutions = mobile_menu.get_by_role(
            "button",
            name=self.locators.MOBILE_MENU_ITEMS[0],
            exact=True,
        )
        solutions.click()
        expect(solutions).to_have_attribute("aria-expanded", "true")

    def assert_navigation_operable(self) -> None:
        mobile_menu = self.page.locator(self.locators.MOBILE_MENU)
        expect(
            mobile_menu.get_by_text(
                self.locators.SOLUTIONS_DESTINATION_NAME,
                exact=True,
            ).first
        ).to_be_visible()

    def assert_no_horizontal_overflow(self) -> None:
        dimensions = self.page.locator(self.locators.DOCUMENT).evaluate(
            "element => ({"
            "clientWidth: element.clientWidth, "
            "scrollWidth: element.scrollWidth"
            "})"
        )
        assert dimensions["scrollWidth"] <= dimensions["clientWidth"], (
            "Mobile content extends beyond the viewport: "
            f"{dimensions['scrollWidth']}px > {dimensions['clientWidth']}px"
        )

    def _dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=self.locators.COOKIE_ALLOW_NAME,
            exact=True,
        )
        if allow_all.count() and allow_all.is_visible():
            allow_all.click()
