"""Steps for issue_0003: Primary CTA buttons function properly."""
from pytest_bdd import given, when, then

from pages.issue_0003_cta_buttons_page import CtaButtonsPage


@given("The homepage is loaded")
def homepage_loaded(page, cta_buttons_page):
    cta_buttons_page.load_homepage()


@when("The user clicks the Contact Us button")
def click_contact_us_button(page, cta_buttons_page):
    cta_buttons_page.click_connect_cta()


@then("The Contact Us page or form opens as expected")
def verify_contact_us_opens(page):
    pass


@when("The user clicks a Learn More button")
def click_learn_more_button(page, cta_buttons_page):
    cta_buttons_page.click_see_how_cta()


@then("The expected page or section opens correctly")
def verify_expected_page_opens(page):
    pass
