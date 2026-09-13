"""Step definitions for issue_0016: All Solutions CTA functionality"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0016_all_solutions_cta_functionality_page import Issue0016AllSolutionsCTAPage


@given("The Featured Solutions section is rendered")
def featured_solutions_rendered(page: Page):
    page_object = Issue0016AllSolutionsCTAPage(page)
    page_object.navigate_to_homepage()


@given("A user clicks the All Solutions CTA")
def user_clicks_all_solutions(page: Page):
    page_object = Issue0016AllSolutionsCTAPage(page)
    page_object.navigate_to_homepage()


@given("The CTA is rendered")
def cta_rendered(page: Page):
    page_object = Issue0016AllSolutionsCTAPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection confirms CTA presence")
def visual_inspection_cta(page: Page):
    """Visual inspection happens in assertions."""
    pass


@when("Navigation completes")
def navigation_completes(page: Page):
    """Navigation check happens in assertions."""
    pass


@when("Automated testing validates the URL")
def automated_validates_url(page: Page):
    """URL validation happens in assertions."""
    pass


@then("The All Solutions CTA is visible after or within the section")
def cta_visible_in_section(page: Page):
    page_object = Issue0016AllSolutionsCTAPage(page)
    page_object.verify_cta_visible()


@then("The user lands on /solutions/")
def user_lands_on_solutions(page: Page):
    page_object = Issue0016AllSolutionsCTAPage(page)
    page_object.click_all_solutions_cta()
    page_object.verify_routes_to_solutions()


@then("The URL follows canonical format")
def url_canonical_format(page: Page):
    page_object = Issue0016AllSolutionsCTAPage(page)
    page_object.verify_canonical_url()
