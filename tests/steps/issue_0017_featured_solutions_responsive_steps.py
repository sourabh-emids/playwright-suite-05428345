"""Step definitions for issue_0017 - Featured solutions responsive interaction."""
from pytest_bdd import given, then, when

from pages.issue_0017_featured_solutions_responsive_page import Issue0017FeaturedSolutionsResponsivePage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0017FeaturedSolutionsResponsivePage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I set the viewport to desktop size")
def set_viewport_desktop(page: Issue0017FeaturedSolutionsResponsivePage):
    """Set viewport to desktop size."""
    page.set_viewport_to_desktop()


@when("I set the viewport to mobile size")
def set_viewport_mobile(page: Issue0017FeaturedSolutionsResponsivePage):
    """Set viewport to mobile size."""
    page.set_viewport_to_mobile()


@when("I view the Featured Solutions section")
def view_featured_solutions_section(page: Issue0017FeaturedSolutionsResponsivePage):
    """View the Featured Solutions section."""
    page.view_featured_solutions_section()


@then("solution cards should be displayed in a grid layout")
def grid_layout(page: Issue0017FeaturedSolutionsResponsivePage):
    """Verify cards are displayed in a grid layout."""
    page.cards_should_be_in_grid_layout()


@then("solution cards should be displayed in a single column or stacked layout")
def stacked_layout(page: Issue0017FeaturedSolutionsResponsivePage):
    """Verify cards are displayed in a stacked layout."""
    page.cards_should_be_in_stacked_layout()
