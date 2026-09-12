"""Step definitions for issue_0050 - WCAG 2.1 AA compliance across landing page."""
from pytest_bdd import given, then, when

from pages.issue_0050_wcag_compliance_page import Issue0050WCAGCompliancePage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0050WCAGCompliancePage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I analyze the page for accessibility")
def analyze_accessibility(page: Issue0050WCAGCompliancePage):
    """Analyze the page for accessibility."""
    page.analyze_for_accessibility()


@then("the page should have sufficient color contrast")
def color_contrast(page: Issue0050WCAGCompliancePage):
    """Verify page has sufficient color contrast."""
    page.page_should_have_sufficient_color_contrast()


@then("interactive elements should have focus indicators")
def focus_indicators(page: Issue0050WCAGCompliancePage):
    """Verify interactive elements have focus indicators."""
    page.interactive_elements_should_have_focus_indicators()


@then("images should have alt text")
def images_have_alt(page: Issue0050WCAGCompliancePage):
    """Verify images have alt text."""
    page.images_should_have_alt_text()
