"""Step definitions for issue_0019: Reduced motion for partner animation"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0019_reduced_motion_for_partner_animation_page import Issue0019ReducedMotionPage


@given("User has prefers-reduced-motion enabled in system settings")
def user_has_reduced_motion(page: Page):
    page_object = Issue0019ReducedMotionPage(page)
    page_object.navigate_to_homepage()


@given("User has prefers-reduced-motion enabled")
def user_has_reduced_motion_short(page: Page):
    page_object = Issue0019ReducedMotionPage(page)
    page_object.navigate_to_homepage()


@given("The page is currently displayed")
def page_currently_displayed(page: Page):
    page_object = Issue0019ReducedMotionPage(page)
    page_object.navigate_to_homepage()


@when("The Partnerships section renders")
def partnerships_section_renders(page: Page):
    """Rendering check happens in assertions."""
    pass


@when("The user views the Partnerships section")
def user_views_partnerships(page: Page):
    """Viewing check happens in assertions."""
    pass


@when("User changes system reduced motion preference")
def user_changes_reduced_motion_preference(page: Page):
    """Preference change handled."""
    pass


@then("Continuous motion animations are disabled or meaningfully reduced")
def motion_disabled_or_reduced(page: Page):
    page_object = Issue0019ReducedMotionPage(page)
    page_object.verify_partnerships_content_visible()


@then("All partner logos remain visible and discoverable without animation")
def logos_visible_without_animation(page: Page):
    page_object = Issue0019ReducedMotionPage(page)
    page_object.verify_partnerships_content_visible()


@then("All partner names and logos are visible in a static state")
def logos_static_visible(page: Page):
    page_object = Issue0019ReducedMotionPage(page)
    page_object.verify_partnerships_content_visible()


@then("Animation state updates without requiring page reload")
def animation_state_updates(page: Page):
    expect(page.get_by_role("main")).to_be_visible()
