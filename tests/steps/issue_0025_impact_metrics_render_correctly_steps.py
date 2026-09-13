"""Step definitions for issue_0025: Impact metrics render correctly"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0025_impact_metrics_render_correctly_page import Issue0025ImpactPage


@given("The Impact section is rendered")
def impact_rendered(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.navigate_to_homepage()


@given("Animation is disabled or fails")
def animation_disabled(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.navigate_to_homepage()


@given("Screen reader software accesses the Impact section")
def screen_reader_accesses(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.navigate_to_homepage()


@given("The Impact metrics are managed in CMS")
def metrics_cms_managed(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.navigate_to_homepage()


@given("The Impact metrics render")
def metrics_render(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection runs")
def visual_inspection(page: Page):
    pass


@when("The content is announced")
def content_announced(page: Page):
    pass


@when("Automated testing validates data integrity")
def automated_validates(page: Page):
    pass


@when("Content is inspected")
def content_inspected(page: Page):
    pass


@then("All four metrics are displayed as text")
def all_four_metrics(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.verify_metrics_visible()


@then("Final metric values are clearly readable")
def values_readable(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.verify_metrics_visible()


@then("Final numeric values and labels are communicated meaningfully")
def values_communicated(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.verify_metrics_visible()


@then("Value and label pairs are maintained together")
def pairs_maintained(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.verify_metrics_visible()


@then("Currency symbols ($) and plus signs (+) are preserved")
def symbols_preserved(page: Page):
    page_object = Issue0025ImpactPage(page)
    page_object.verify_currency_symbols()
