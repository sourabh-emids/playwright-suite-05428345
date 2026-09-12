"""Step definitions for issue_0040 - Marketo marketing integration consent gating."""
from pytest_bdd import given, then

from pages.issue_0040_marketo_consent_page import Issue0040MarketoConsentPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0040MarketoConsentPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@then("Marketo should not be active")
def marketo_not_active(page: Issue0040MarketoConsentPage):
    """Verify Marketo is not active."""
    page.marketo_should_not_be_active_before_consent()
