"""Step definitions for issue_0009 - Hero section rendering and H1 uniqueness."""
from pytest_bdd import given, then, when

from pages.issue_0009_hero_page import Issue0009HeroPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0009HeroPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the hero section")
def view_hero_section(page: Issue0009HeroPage):
    """View the hero section."""
    page.view_hero_section()


@then("the hero section should be visible")
def hero_section_visible(page: Issue0009HeroPage):
    """Verify hero section is visible."""
    page.hero_section_should_be_visible()


@then("there should be exactly one H1 heading")
def exactly_one_h1(page: Issue0009HeroPage):
    """Verify exactly one H1 heading exists."""
    page.there_should_be_exactly_one_h1()


@then('the H1 should contain "In Healthcare, Only Outcomes Matter"')
def h1_contains_text(page: Issue0009HeroPage):
    """Verify H1 contains expected text."""
    page.h1_should_contain_text()


@then("the subtitle should be present")
def subtitle_present(page: Issue0009HeroPage):
    """Verify subtitle is present."""
    page.subtitle_should_be_present()
