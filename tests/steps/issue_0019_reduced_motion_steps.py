"""Step definitions for issue_0019 - Reduced motion preference for partner animation."""
from pytest_bdd import given, then, when

from pages.issue_0019_reduced_motion_page import Issue0019ReducedMotionPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0019ReducedMotionPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when('I have "prefers-reduced-motion: reduce" set')
def set_reduced_motion(page: Issue0019ReducedMotionPage):
    """Set reduced motion preference."""
    page.set_reduced_motion_preference()


@when("I view the Partnerships section")
def view_partnerships_section(page: Issue0019ReducedMotionPage):
    """View the Partnerships section."""
    page.view_partnerships_section()


@then("the partner logo animation should be reduced or disabled")
def animation_reduced(page: Issue0019ReducedMotionPage):
    """Verify animation is reduced or disabled."""
    page.animation_should_be_reduced_or_disabled()
