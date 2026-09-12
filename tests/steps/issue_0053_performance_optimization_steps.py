"""Step definitions for issue_0053 - Performance and Core Web Vitals optimization."""
from pytest_bdd import given, then, when

from pages.issue_0053_performance_optimization_page import Issue0053PerformanceOptimizationPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0053PerformanceOptimizationPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I measure performance metrics")
def measure_performance(page: Issue0053PerformanceOptimizationPage):
    """Measure performance metrics."""
    page.measure_performance_metrics()


@then("the page should load within acceptable time")
def acceptable_load_time(page: Issue0053PerformanceOptimizationPage):
    """Verify page loads within acceptable time."""
    page.page_should_load_within_acceptable_time()


@then("LCP should be within acceptable range")
def lcp_acceptable(page: Issue0053PerformanceOptimizationPage):
    """Verify LCP is within acceptable range."""
    page.lcp_should_be_within_acceptable_range()
