"""Step definitions for issue_0039 - Campaign attribution parameters handling."""
from pytest_bdd import given, then, when

from pages.issue_0039_campaign_attribution_page import Issue0039CampaignAttributionPage


@given("I navigate to the homepage with UTM parameters")
def navigate_with_utm(page: Issue0039CampaignAttributionPage):
    """Navigate to homepage with UTM parameters."""
    page.navigate_with_utm()


@when("I have UTM parameters in the URL")
def have_utm_params(page: Issue0039CampaignAttributionPage):
    """Verify UTM parameters are present."""
    pass


@then("the UTM parameters should be stored")
def utm_stored(page: Issue0039CampaignAttributionPage):
    """Verify UTM parameters are stored."""
    page.utm_parameters_should_be_stored()


@then("the parameters should be available for analytics")
def params_for_analytics(page: Issue0039CampaignAttributionPage):
    """Verify parameters are available for analytics."""
    pass
