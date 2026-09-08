import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_04_mobile_view_page import Tc04MobileViewPage


@pytest.fixture
def tc_04_mobile_page(page: Page) -> Tc04MobileViewPage:
    return Tc04MobileViewPage(page)


@given("the browser uses a 390 by 844 mobile viewport")
def set_mobile_viewport(tc_04_mobile_page: Tc04MobileViewPage) -> None:
    tc_04_mobile_page.use_mobile_viewport()


@when("the Emids homepage is opened in mobile view")
def open_mobile_homepage(tc_04_mobile_page: Tc04MobileViewPage) -> None:
    tc_04_mobile_page.open()


@then("the mobile logo, primary text, image, and call-to-action are visible")
def verify_mobile_content(tc_04_mobile_page: Tc04MobileViewPage) -> None:
    tc_04_mobile_page.assert_primary_content_visible()


@when("the mobile navigation menu and Solutions section are opened")
def open_mobile_navigation(tc_04_mobile_page: Tc04MobileViewPage) -> None:
    tc_04_mobile_page.open_navigation_and_solutions()


@then("the mobile navigation controls are visible and operable")
def verify_mobile_navigation(tc_04_mobile_page: Tc04MobileViewPage) -> None:
    tc_04_mobile_page.assert_navigation_operable()


@then("the page has no horizontal content overflow")
def verify_no_horizontal_overflow(
    tc_04_mobile_page: Tc04MobileViewPage,
) -> None:
    tc_04_mobile_page.assert_no_horizontal_overflow()
