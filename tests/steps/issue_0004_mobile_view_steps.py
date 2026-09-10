"""Step bindings for issue_0004 mobile usability."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0004_mobile_view_page import MobileViewPage


@given(
    "the Emids homepage is open at the supported mobile viewport",
    target_fixture="mobile_view_page",
)
def open_mobile_homepage(page: Page) -> MobileViewPage:
    mobile_page = MobileViewPage(page)
    mobile_page.use_supported_viewport()
    mobile_page.open()
    return mobile_page


@then("the homepage text, logo, primary action, and menu are visible")
def verify_mobile_content(mobile_view_page: MobileViewPage) -> None:
    mobile_view_page.verify_mobile_content()


@when("the user opens the mobile Solutions menu")
def open_mobile_solutions(mobile_view_page: MobileViewPage) -> None:
    mobile_view_page.open_solutions_menu()


@then("the Modernization navigation destination is accessible")
def verify_mobile_destination(mobile_view_page: MobileViewPage) -> None:
    mobile_view_page.verify_modernization_accessible()


@when("the user selects the mobile Modernization destination")
def select_mobile_destination(mobile_view_page: MobileViewPage) -> None:
    mobile_view_page.select_modernization()


@then("the Modernization page opens in the mobile-sized view")
def verify_mobile_navigation(mobile_view_page: MobileViewPage) -> None:
    mobile_view_page.verify_modernization_page()
