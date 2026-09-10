from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0001_homepage_page import Issue0001HomepagePage


@given("the Emids website is available", target_fixture="homepage")
def emids_website_available(page: Page) -> Issue0001HomepagePage:
    return Issue0001HomepagePage(page)


@when("the user opens the Emids homepage")
def open_homepage(homepage: Issue0001HomepagePage) -> None:
    homepage.open()


@then(
    "the homepage loads with its expected content and no obvious error page"
)
def verify_homepage(homepage: Issue0001HomepagePage) -> None:
    homepage.assert_loaded_without_obvious_errors()
