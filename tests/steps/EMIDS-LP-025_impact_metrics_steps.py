"""Step definitions for Impact section - EMIDS-LP-025"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-025_impact_metrics_page import ImpactMetricsPage
from playwright.sync_api import expect


@given("Impact section")
def impact_section(page):
    page.goto("/")


@when("Metrics are inspected")
def inspect_metrics(page):
    pass


@then("All four values visible: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, 450+ Platforms Launched")
def verify_all_metrics(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.verify_all_metrics()


@given("Metrics with optional count-up animation")
def metrics_with_animation(page):
    pass


@when("Animation is disabled or skipped")
def animation_disabled(page):
    page.emulate_media(reduced_motion=True)


@then("Final meaningful values remain understandable")
def verify_final_values(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.goto("/")
    impact_page.verify_all_metrics()


@given("Screen reader testing")
def screen_reader_testing(page):
    pass


@when("Impact section is read")
def read_impact_section(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.goto("/")


@then("Screen readers receive final meaningful values")
def verify_screen_reader_values(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.verify_all_metrics()


@given("Metric values with special characters")
def special_characters(page):
    page.goto("/")


@when("Values are rendered")
def render_values(page):
    pass


@then("Currency symbols ($) and plus signs (+) are preserved where approved")
def verify_special_chars(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.verify_special_characters()


@given("CMS content management")
def cms_management(page):
    pass


@when("Values are updated")
def update_values(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.goto("/")


@then("Value and label pairs remain properly associated")
def verify_pairs(page):
    impact_page = ImpactMetricsPage(page)
    impact_page.verify_all_metrics()
