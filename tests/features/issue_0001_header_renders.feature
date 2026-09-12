"""Header renders on initial page load."""
from pytest_bdd import given, then


@given("I navigate to the homepage")
def navigate_to_homepage(page):
    page.goto("/")


@then("the header is visible")
def header_is_visible(page):
    header = page.locator("header, nav, [role='banner']").first
    assert header.is_visible(), "Header should be visible on initial page load"
