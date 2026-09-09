"""Step definitions for issue_0004 mobile usability."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0004_mobile_usability_page import MobileUsabilityPage


@given(
    "the homepage is open in the approved mobile viewport",
    target_fixture="mobile_page",
)
def open_mobile_page(page: Page) -> MobileUsabilityPage:
    mobile_page = MobileUsabilityPage(page)
    mobile_page.open_in_mobile_view()
    return mobile_page


@then("the mobile hero text, logo, and primary call to action are usable")
def verify_mobile_content(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.assert_primary_content_is_usable()


@when("the user opens the mobile menu and selects Contact Us")
def use_mobile_navigation(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.open_contact_from_mobile_navigation()


@then("the contact page opens in the mobile viewport")
def verify_mobile_contact_page(mobile_page: MobileUsabilityPage) -> None:
    mobile_page.assert_contact_page_opened()
