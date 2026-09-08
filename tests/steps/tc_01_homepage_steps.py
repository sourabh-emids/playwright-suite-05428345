import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then

from pages.tc_01_homepage_page import Tc01HomepagePage


@pytest.fixture
def tc_01_homepage(page: Page) -> Tc01HomepagePage:
    return Tc01HomepagePage(page)


@given("the public Emids homepage is opened")
def open_homepage(tc_01_homepage: Tc01HomepagePage) -> None:
    tc_01_homepage.open()


@then("the primary homepage content is visible")
def verify_primary_content(tc_01_homepage: Tc01HomepagePage) -> None:
    tc_01_homepage.assert_primary_content()


@then("no visible page load failure is shown")
def verify_no_load_failure(tc_01_homepage: Tc01HomepagePage) -> None:
    tc_01_homepage.assert_no_visible_load_failure()
