"""Step bindings for TC-04 responsive mobile usability."""

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_04_mobile_usability_page import MobileUsabilityPage


@pytest.fixture
def mobile_page(page: Page) -> MobileUsabilityPage:
    return MobileUsabilityPage(page)


@given("the Emids homepage is open at the agreed mobile viewport")
def open_mobile_homepage(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.open_in_mobile_view()


@then("the primary mobile content and controls are visible and usable")
def verify_mobile_content(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.assert_primary_content_is_usable()


@when("the user navigates to Solutions with the mobile menu")
def use_mobile_menu(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.navigate_with_mobile_menu()


@then("the Solutions page is displayed in mobile view")
def verify_mobile_destination(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.assert_mobile_navigation_destination()
