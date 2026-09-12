"""Step definitions for issue_0013 - See the model CTA routing and operation."""
from pytest_bdd import given, then, when

from pages.issue_0013_see_model_cta_page import Issue0013SeeModelCTAPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0013SeeModelCTAPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the How We Deliver section")
def view_how_we_deliver_section(page: Issue0013SeeModelCTAPage):
    """View the How We Deliver section."""
    page.view_how_we_deliver_section()


@then('the "See the model" CTA should be visible')
def see_model_cta_visible(page: Issue0013SeeModelCTAPage):
    """Verify See the model CTA is visible."""
    page.see_model_cta_should_be_visible()


@then("the CTA should link to the FDCE page")
def cta_links_to_fdce(page: Issue0013SeeModelCTAPage):
    """Verify CTA links to FDCE page."""
    page.cta_should_link_to_fdce_page()


@when('I click the "See the model" CTA')
def click_see_model_cta(page: Issue0013SeeModelCTAPage):
    """Click the See the model CTA."""
    page.click_see_model_cta()


@then("I should be navigated to the FDCE page")
def on_fdce_page(page: Issue0013SeeModelCTAPage):
    """Verify user is on the FDCE page."""
    page.should_be_on_fdce_page()
