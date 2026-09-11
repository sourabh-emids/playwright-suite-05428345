"""Step definitions for REQ-001: Homepage loads successfully."""

from pytest_bdd import given, when, then  # noqa: F401

from utils.config import BASE_URL


@given("User navigates to the website URL \"https://www.emids.com/\"")
def user_navigates_to_homepage(req001_homepage_page) -> None:
    """Navigate to the homepage."""
    req001_homepage_page.goto_homepage(BASE_URL)
    req001_homepage_page.dismiss_cookie_banner_if_present()


@given("User has successfully loaded the homepage")
def user_has_loaded_homepage(req001_homepage_page) -> None:
    """Verify homepage is loaded and dismiss cookie banner."""
    req001_homepage_page.dismiss_cookie_banner_if_present()
    req001_homepage_page.verify_main_heading_visible()


@when("The browser initiates and completes the page load request")
def browser_loads_page(req001_homepage_page) -> None:
    """Verify page loads successfully."""
    req001_homepage_page.verify_page_loads_without_errors()


@then("Homepage loads successfully without obvious errors, broken layouts, or missing critical content")
def homepage_loads_without_errors(req001_homepage_page) -> None:
    """Verify homepage loads without errors."""
    req001_homepage_page.verify_page_loads_without_errors()


@when("Page resources finish rendering (images, scripts, stylesheets)")
def page_resources_finish_rendering(req001_homepage_page) -> None:
    """Wait for resources to load."""
    req001_homepage_page.page.wait_for_load_state("networkidle")


@then("All visible elements display correctly and the page becomes interactive")
def all_elements_display_correctly(req001_homepage_page) -> None:
    """Verify all visible elements are displayed."""
    req001_homepage_page.verify_all_resources_loaded()


@then("The page title should be \"Emids - Digital Engineering, Core Platforms, and AI Solutions\"")
def page_title_is_correct(req001_homepage_page) -> None:
    """Verify page title is correct."""
    req001_homepage_page.verify_page_title("Emids - Digital Engineering, Core Platforms, and AI Solutions")


@then("The main heading should be visible")
def main_heading_visible(req001_homepage_page) -> None:
    """Verify main heading is visible."""
    req001_homepage_page.verify_main_heading_visible()
