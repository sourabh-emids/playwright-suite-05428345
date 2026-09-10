"""Step bindings for issue_0001 homepage availability."""

from playwright.sync_api import Page
from pytest_bdd import given, then

from pages.issue_0001_website_homepage_page import WebsiteHomepagePage


@given(
    "the user opens the Emids homepage",
    target_fixture="website_homepage",
)
def open_homepage(page: Page) -> WebsiteHomepagePage:
    homepage = WebsiteHomepagePage(page)
    homepage.open()
    return homepage


@then("the homepage loads successfully without a visible error page")
def verify_homepage(website_homepage: WebsiteHomepagePage) -> None:
    website_homepage.verify_homepage_loaded()
