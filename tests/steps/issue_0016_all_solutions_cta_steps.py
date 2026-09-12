"""Step definitions for issue_0016 - All Solutions CTA visibility and routing."""
from pytest_bdd import given, then, when

from pages.issue_0016_all_solutions_cta_page import Issue0016AllSolutionsCTAPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0016AllSolutionsCTAPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Featured Solutions section")
def view_featured_solutions_section(page: Issue0016AllSolutionsCTAPage):
    """View the Featured Solutions section."""
    page.view_featured_solutions_section()


@then('the "All solutions" CTA should be visible')
def all_solutions_cta_visible(page: Issue0016AllSolutionsCTAPage):
    """Verify All solutions CTA is visible."""
    page.all_solutions_cta_should_be_visible()


@then("the CTA should link to the solutions page")
def cta_links_to_solutions(page: Issue0016AllSolutionsCTAPage):
    """Verify CTA links to solutions page."""
    page.cta_should_link_to_solutions_page()


@when('I click the "All solutions" CTA')
def click_all_solutions_cta(page: Issue0016AllSolutionsCTAPage):
    """Click the All solutions CTA."""
    page.click_all_solutions_cta()


@then("I should be navigated to the solutions page")
def on_solutions_page(page: Issue0016AllSolutionsCTAPage):
    """Verify user is on the solutions page."""
    page.should_be_on_solutions_page()
