from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0003_cta_page import Issue0003CtaPage


@given(
    "the Emids homepage containing primary calls to action is open",
    target_fixture="cta_page",
)
def homepage_with_ctas(page: Page) -> Issue0003CtaPage:
    cta_page = Issue0003CtaPage(page)
    cta_page.open()
    return cta_page


@when('the user selects the Contact Us action labelled "Connect"')
def select_contact_cta(cta_page: Issue0003CtaPage) -> None:
    cta_page.select_contact_cta()


@then("the contact page opens")
def verify_contact_page(cta_page: Issue0003CtaPage) -> None:
    cta_page.assert_expected_destination_opened()


@when(
    "the user returns home and selects the learn-more action labelled "
    '"See How We Deliver Outcomes"'
)
def select_learn_more_cta(cta_page: Issue0003CtaPage) -> None:
    cta_page.open()
    cta_page.select_learn_more_cta()


@then("the forward-deployed context engineering page opens")
def verify_learn_more_page(cta_page: Issue0003CtaPage) -> None:
    cta_page.assert_expected_destination_opened()
