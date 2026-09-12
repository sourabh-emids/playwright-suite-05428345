"""Step definitions for issue_0052 - Responsive layout across common viewports."""
from pytest_bdd import given, parsers, then, when

from pages.issue_0052_responsive_layout_page import Issue0052ResponsiveLayoutPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0052ResponsiveLayoutPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when(parsers.parse("I set the viewport to {width}x{height}"))
def set_viewport(page: Issue0052ResponsiveLayoutPage, width: int, height: int):
    """Set the viewport size."""
    page.set_viewport(int(width), int(height))


@then("the page should render without horizontal overflow")
def no_horizontal_overflow(page: Issue0052ResponsiveLayoutPage):
    """Verify page renders without horizontal overflow."""
    page.page_should_render_without_horizontal_overflow()
