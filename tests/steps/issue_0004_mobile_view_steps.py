"""Steps for issue_0004: Mobile responsive layout is usable."""
from pytest_bdd import given, when, then

from pages.issue_0004_mobile_view_page import MobileViewPage


@given("A user has access to a web browser with mobile viewport")
def user_has_mobile_viewport(page, mobile_view_page):
    mobile_view_page.set_mobile_viewport(375, 667)


@when("The website is opened in a mobile-sized browser window (e.g., 375x667)")
def open_mobile_viewport(page, mobile_view_page):
    mobile_view_page.set_mobile_viewport(375, 667)
    mobile_view_page.load_homepage()


@then("Text, images, menu, and buttons are visible and usable on the mobile view")
def verify_mobile_elements_visible(page, mobile_view_page):
    mobile_view_page.verify_logo_visible()
    mobile_view_page.verify_main_heading_visible()
    mobile_view_page.verify_footer_visible()
    mobile_view_page.verify_navigation_menu_visible()
    mobile_view_page.verify_buttons_visible()
