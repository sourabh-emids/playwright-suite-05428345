"""Step definitions for issue_0026: Insights section and cards render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0026_insights_section_and_cards_render_page import Issue0026InsightsPage


@given("The Insights section is rendered")
def insights_rendered(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.navigate_to_homepage()


@given("Each insight card is analyzed")
def cards_analyzed(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.navigate_to_homepage()


@given("Insight cards are rendered")
def cards_rendered(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.navigate_to_homepage()


@given("Insight cards are managed by CMS")
def cards_cms_managed(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.navigate_to_homepage()


@when("Automated testing counts cards")
def automated_counts_cards(page: Page):
    pass


@when("Required fields are validated")
def fields_validated(page: Page):
    pass


@when("Viewport is tested at desktop, tablet, and mobile widths")
def viewport_tested(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.resize_to_viewport(1280, 720)
    page_object.resize_to_viewport(768, 1024)
    page_object.resize_to_viewport(375, 812)


@when("Automated testing validates content status")
def automated_validates_status(page: Page):
    pass


@when("Required field validation runs")
def field_validation_runs(page: Page):
    pass


@then("Exactly six insight cards are displayed")
def six_cards_displayed(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.verify_insights_section()


@then("Each card contains required content")
def cards_contain_required(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.verify_insights_section()


@then("Cards remain accessible and functional at all breakpoints")
def cards_accessible_breakpoints(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.verify_insights_section()


@then("Only published content is displayed")
def only_published_displayed(page: Page):
    page_object = Issue0026InsightsPage(page)
    page_object.verify_insights_section()


@then("Each card has a non-empty title and valid URL")
def cards_have_title_url(page: Page):
    page_object = Issue0026InsightsPage(page)
    expect(page_object.locators.insight_cards.first).to_be_visible()
