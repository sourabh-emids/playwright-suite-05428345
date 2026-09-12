"""Step definitions for issue_0008 - Responsive navigation behavior."""
from pytest_bdd import given, then, when

from pages.issue_0008_responsive_nav_page import Issue0008ResponsiveNavPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0008ResponsiveNavPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I set the viewport to desktop size")
def set_viewport_desktop(page: Issue0008ResponsiveNavPage):
    """Set viewport to desktop size."""
    page.set_viewport_to_desktop()


@when("I set the viewport to mobile size")
def set_viewport_mobile(page: Issue0008ResponsiveNavPage):
    """Set viewport to mobile size."""
    page.set_viewport_to_mobile()


@then("the full navigation menu should be visible")
def full_navigation_visible(page: Issue0008ResponsiveNavPage):
    """Verify full navigation menu is visible."""
    page.full_navigation_should_be_visible()


@then("the Connect CTA should be visible")
def connect_cta_visible(page: Issue0008ResponsiveNavPage):
    """Verify Connect CTA is visible."""
    page.connect_cta_should_be_visible()


@then("the mobile menu toggle should be visible")
def mobile_menu_toggle_visible(page: Issue0008ResponsiveNavPage):
    """Verify mobile menu toggle is visible."""
    page.mobile_menu_toggle_should_be_visible()


@then("tapping the menu toggle should reveal navigation options")
def tapping_menu_reveals_navigation(page: Issue0008ResponsiveNavPage):
    """Verify tapping menu toggle reveals navigation."""
    page.tapping_menu_toggle_should_reveal_navigation()
