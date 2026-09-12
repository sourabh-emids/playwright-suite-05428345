"""Step definitions for issue_0015 - Six featured solutions rendering and numbering."""
from pytest_bdd import given, then, when

from pages.issue_0015_featured_solutions_page import Issue0015FeaturedSolutionsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0015FeaturedSolutionsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Featured Solutions section")
def view_featured_solutions_section(page: Issue0015FeaturedSolutionsPage):
    """View the Featured Solutions section."""
    page.view_featured_solutions_section()


@then("six solution cards should be visible")
def six_solution_cards_visible(page: Issue0015FeaturedSolutionsPage):
    """Verify six solution cards are visible."""
    page.six_solution_cards_should_be_visible()


@then("each solution should have a number")
def solution_has_number(page: Issue0015FeaturedSolutionsPage):
    """Verify each solution has a number."""
    page.each_solution_should_have_number()


@then("each solution should have a title")
def solution_has_title(page: Issue0015FeaturedSolutionsPage):
    """Verify each solution has a title."""
    page.each_solution_should_have_title()


@then("each solution should have a description")
def solution_has_description(page: Issue0015FeaturedSolutionsPage):
    """Verify each solution has a description."""
    page.each_solution_should_have_description()
