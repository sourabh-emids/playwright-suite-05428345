"""Step bindings for TC-03 primary calls to action."""

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_03_primary_cta_page import PrimaryCtaPage


@pytest.fixture
def primary_cta(page: Page) -> PrimaryCtaPage:
    return PrimaryCtaPage(page)


@given("a page with the Contact Us call to action is open")
def prepare_contact_us(primary_cta: PrimaryCtaPage) -> None:
    primary_cta.open_homepage()


@when("the user selects Contact Us")
def select_contact_us(primary_cta: PrimaryCtaPage) -> None:
    primary_cta.select_contact_us()


@then("the contact page is displayed")
def verify_contact_page(primary_cta: PrimaryCtaPage) -> None:
    primary_cta.assert_contact_destination()


@given("the partnerships page with Learn More calls to action is open")
def prepare_partners_page(primary_cta: PrimaryCtaPage) -> None:
    primary_cta.open_partners_page()


@when("the user selects Learn More for Snowflake")
def select_learn_more(primary_cta: PrimaryCtaPage) -> None:
    primary_cta.select_snowflake_learn_more()


@then("the Snowflake partner page is displayed")
def verify_partner_page(primary_cta: PrimaryCtaPage) -> None:
    primary_cta.assert_snowflake_destination()
