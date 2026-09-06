"""Step bindings for TC-01 homepage availability."""

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then

from pages.tc_01_homepage_page import HomepagePage


@pytest.fixture
def homepage(page: Page) -> HomepagePage:
    return HomepagePage(page)


@given("the Emids homepage is opened")
def open_homepage(homepage: HomepagePage) -> None:
    homepage.open()


@then(
    "the homepage is displayed without visible errors or broken critical "
    "content"
)
def verify_homepage(homepage: HomepagePage) -> None:
    homepage.assert_loaded_without_visible_errors()
