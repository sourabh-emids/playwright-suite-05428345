"""Step definitions for issue_0034 - Final conversion banner rendering and CTA."""
from pytest_bdd import given, then, when

from pages.issue_0034_final_conversion_banner_page import Issue0034FinalConversionBannerPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0034FinalConversionBannerPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the page")
def view_page(page: Issue0034FinalConversionBannerPage):
    """View the page."""
    page.view_page()


@then("the final CTA banner should be visible")
def final_cta_banner_visible(page: Issue0034FinalConversionBannerPage):
    """Verify final CTA banner is visible."""
    page.final_cta_banner_should_be_visible()


@then("the timing message should be visible")
def timing_message_visible(page: Issue0034FinalConversionBannerPage):
    """Verify timing message is visible."""
    page.timing_message_should_be_visible()


@then("the Connect CTA should be present")
def connect_cta_present(page: Issue0034FinalConversionBannerPage):
    """Verify Connect CTA is present."""
    page.connect_cta_should_be_present()
