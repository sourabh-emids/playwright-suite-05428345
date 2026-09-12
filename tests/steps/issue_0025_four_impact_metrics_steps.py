"""Step definitions for issue_0025 - Four impact proof metrics rendering."""
from pytest_bdd import given, then, when

from pages.issue_0025_four_impact_metrics_page import Issue0025FourImpactMetricsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0025FourImpactMetricsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Impact section")
def view_impact_section(page: Issue0025FourImpactMetricsPage):
    """View the Impact section."""
    page.view_impact_section()


@then("four metrics should be visible")
def four_metrics_visible(page: Issue0025FourImpactMetricsPage):
    """Verify four metrics are visible."""
    page.four_metrics_should_be_visible()


@then("each metric should have a number and label")
def metric_has_number_and_label(page: Issue0025FourImpactMetricsPage):
    """Verify each metric has a number and label."""
    page.each_metric_should_have_number_and_label()
