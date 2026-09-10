from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0004_mobile_page import Issue0004MobilePage


@given(
    "the Emids homepage is open in a 390 by 844 mobile viewport",
    target_fixture="mobile_page",
)
def mobile_homepage(page: Page) -> Issue0004MobilePage:
    mobile_page = Issue0004MobilePage(page)
    mobile_page.open_at_mobile_size(390, 844)
    return mobile_page


@then(
    "the core text, brand image, menu control, and primary action are visible"
)
def verify_mobile_content(mobile_page: Issue0004MobilePage) -> None:
    mobile_page.assert_core_content_visible()


@when("the user opens the mobile menu")
def open_mobile_menu(mobile_page: Issue0004MobilePage) -> None:
    mobile_page.open_mobile_menu()


@then("the mobile navigation and contact action are visible and usable")
def verify_mobile_navigation(mobile_page: Issue0004MobilePage) -> None:
    mobile_page.assert_mobile_navigation_usable()


@when("the user closes the menu and selects the primary homepage action")
def select_mobile_primary_action(mobile_page: Issue0004MobilePage) -> None:
    mobile_page.close_menu_and_select_hero_cta()


@then("the primary action destination opens in the mobile viewport")
def verify_mobile_destination(mobile_page: Issue0004MobilePage) -> None:
    mobile_page.assert_hero_destination_opened()
