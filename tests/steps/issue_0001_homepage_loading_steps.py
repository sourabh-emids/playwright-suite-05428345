"""Steps for issue_0001: Homepage loads without errors."""
from pytest_bdd import given, when, then

from pages.issue_0001_homepage_loading_page import HomepageLoadingPage


@given("A user has access to a web browser")
def user_has_web_browser(page):
    return page


@when("The user navigates to https://www.emids.com/")
def navigate_to_homepage(page, homepage_page):
    homepage_page.load_homepage()
    homepage_page.dismiss_cookie_consent()


@then("The homepage loads successfully without obvious errors")
def verify_homepage_loads(page, homepage_page):
    homepage_page.verify_page_loads_without_errors()
