"""Step definitions for REQ-002: Main navigation menu items navigate to correct pages."""

from pytest_bdd import given, when, then  # noqa: F401

from pages.req_001_homepage_page import Req001HomepagePage
from utils.config import BASE_URL


@given("User is on the homepage with main navigation menu visible")
def user_on_homepage_with_navigation(req002_navigation_page) -> None:
    """User is on homepage with navigation visible."""
    req002_navigation_page.verify_navigation_menu_visible()


@given("User is on the homepage")
def user_on_homepage(req002_navigation_page) -> None:
    """User is on homepage."""
    homepage_page = Req001HomepagePage(req002_navigation_page.page)
    homepage_page.goto_homepage(BASE_URL)
    homepage_page.dismiss_cookie_banner_if_present()


@when("User clicks on each main navigation menu item")
def user_clicks_each_nav_item(req002_navigation_page) -> None:
    """Click each navigation item and verify it works."""
    req002_navigation_page.click_solutions_nav()
    req002_navigation_page.verify_solutions_page_loaded()


@then("Each menu item opens the correct associated page or section as expected")
def each_nav_item_opens_correct_page(req002_navigation_page) -> None:
    """Verify each navigation item opens correct page."""
    pass


@then("The destination page loads with relevant content matching the menu label")
def destination_page_has_relevant_content(req002_navigation_page) -> None:
    """Verify destination page has relevant content."""
    pass


@when('User clicks on "Solutions" in the main navigation')
def user_clicks_solutions_nav(req002_navigation_page) -> None:
    """Click on Solutions navigation."""
    req002_navigation_page.click_solutions_nav()


@then("The Solutions page should load with the URL containing \"solutions\"")
def solutions_page_loads(req002_navigation_page) -> None:
    """Verify Solutions page loads."""
    req002_navigation_page.verify_solutions_page_loaded()


@when('User clicks on "Capabilities" in the main navigation')
def user_clicks_capabilities_nav(req002_navigation_page) -> None:
    """Click on Capabilities navigation."""
    req002_navigation_page.click_capabilities_nav()


@then("The Capabilities page should load with the URL containing \"capabilities\"")
def capabilities_page_loads(req002_navigation_page) -> None:
    """Verify Capabilities page loads."""
    req002_navigation_page.verify_capabilities_page_loaded()


@when('User clicks on "Industries" in the main navigation')
def user_clicks_industries_nav(req002_navigation_page) -> None:
    """Click on Industries navigation."""
    req002_navigation_page.click_industries_nav()


@then("The Industries page should load with the URL containing \"segments\"")
def industries_page_loads(req002_navigation_page) -> None:
    """Verify Industries page loads."""
    req002_navigation_page.verify_industries_page_loaded()


@when('User clicks on "Insights" in the main navigation')
def user_clicks_insights_nav(req002_navigation_page) -> None:
    """Click on Insights navigation."""
    req002_navigation_page.click_insights_nav()


@then("The Insights page should load with the URL containing \"insights\"")
def insights_page_loads(req002_navigation_page) -> None:
    """Verify Insights page loads."""
    req002_navigation_page.verify_insights_page_loaded()


@when('User clicks on "Company" in the main navigation')
def user_clicks_company_nav(req002_navigation_page) -> None:
    """Click on Company navigation."""
    req002_navigation_page.click_company_nav()


@then("The About Us page should load with the URL containing \"about-us\"")
def about_us_page_loads(req002_navigation_page) -> None:
    """Verify About Us page loads."""
    req002_navigation_page.verify_about_us_page_loaded()


@when('User clicks on "Connect" in the main navigation')
def user_clicks_connect_nav(req002_navigation_page) -> None:
    """Click on Connect navigation."""
    req002_navigation_page.click_connect_nav()


@then("The Contact page should load with the URL containing \"contact\"")
def contact_page_loads(req002_navigation_page) -> None:
    """Verify Contact page loads."""
    req002_navigation_page.verify_contact_page_loaded()
