"""Step definitions for issue_0037 - Google Tag Manager consent-governed loading."""
from pytest_bdd import given, then

from pages.issue_0037_gtm_consent_page import Issue0037GTMConsentPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0037GTMConsentPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@then("GTM should not be active")
def gtm_not_active(page: Issue0037GTMConsentPage):
    """Verify GTM is not active."""
    page.gtm_should_not_be_active_before_consent()
