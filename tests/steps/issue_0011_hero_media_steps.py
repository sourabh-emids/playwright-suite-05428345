"""Step definitions for issue_0011 - Hero media optimization and load behavior."""
from pytest_bdd import given, then, when

from pages.issue_0011_hero_media_page import Issue0011HeroMediaPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0011HeroMediaPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the hero section")
def view_hero_section(page: Issue0011HeroMediaPage):
    """View the hero section."""
    page.view_hero_section()


@then("any media in the hero should load without errors")
def media_loads_without_errors(page: Issue0011HeroMediaPage):
    """Verify media loads without errors."""
    page.media_should_load_without_errors()


@then("the page should have good performance characteristics")
def good_performance(page: Issue0011HeroMediaPage):
    """Verify page has good performance."""
    page.page_should_have_good_performance()
