"""Step definitions for REQ-004: Website displays correctly on mobile viewport."""

from pytest_bdd import given, when, then  # noqa: F401

from pages.req_001_homepage_page import Req001HomepagePage
from utils.config import BASE_URL


@given("User accesses the website using a mobile-sized browser window or device")
def user_accesses_mobile_site(req004_mobile_page) -> None:
    """Set viewport to mobile and navigate to homepage."""
    req004_mobile_page.set_mobile_viewport()
    homepage_page = Req001HomepagePage(req004_mobile_page.page)
    homepage_page.goto_homepage(BASE_URL)


@when("The homepage loads in mobile viewport")
def homepage_loads_mobile(req004_mobile_page) -> None:
    """Verify homepage loads in mobile viewport."""
    req004_mobile_page.dismiss_cookie_banner_if_present()


@then("Text, images, menu and buttons are visible and usable without horizontal scrolling for core content")
def content_visible_without_horizontal_scroll(req004_mobile_page) -> None:
    """Verify all content is visible without horizontal scrolling."""
    req004_mobile_page.verify_main_heading_visible()
    req004_mobile_page.verify_logo_visible()
    req004_mobile_page.verify_no_horizontal_scroll()


@then("A mobile menu toggle button should be visible")
def mobile_menu_toggle_visible(req004_mobile_page) -> None:
    """Verify mobile menu toggle is visible."""
    req004_mobile_page.verify_mobile_menu_toggle_visible()


@then("The main heading should be visible")
def main_heading_mobile(req004_mobile_page) -> None:
    """Verify main heading is visible on mobile."""
    req004_mobile_page.verify_main_heading_visible()


@then("The logo should be visible")
def logo_mobile(req004_mobile_page) -> None:
    """Verify logo is visible on mobile."""
    req004_mobile_page.verify_logo_visible()


@then("The page title should be correct")
def page_title_mobile(req004_mobile_page) -> None:
    """Verify page title is correct on mobile."""
    req004_mobile_page.verify_page_title("Emids - Digital Engineering, Core Platforms, and AI Solutions")
