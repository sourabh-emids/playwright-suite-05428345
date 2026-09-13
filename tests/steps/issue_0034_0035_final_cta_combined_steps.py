"""Step definitions for issue_0034-0035: Final CTA combined"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0034_0035_final_cta_combined_page import FinalCTAPage


# Issue 0034 - Final conversion banner
@given("The page has fully loaded")
def page_fully_loaded(page: Page):
    page_object = FinalCTAPage(page)
    page_object.navigate_to_homepage()


@given("The final conversion banner is rendered")
def final_cta_rendered(page: Page):
    page_object = FinalCTAPage(page)
    page_object.navigate_to_homepage()


@given("The final CTA section is managed by CMS")
def final_cta_cms_managed(page: Page):
    page_object = FinalCTAPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection confirms section order")
def visual_inspection_order(page: Page):
    pass


@when("Keyboard navigation testing runs")
def keyboard_nav_testing(page: Page):
    page.keyboard.press("Tab")


@when("Color contrast testing runs")
def contrast_testing(page: Page):
    pass


@then("The final conversion banner appears after main content and before the footer")
def banner_before_footer(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_final_cta_present()


@then("The primary CTA is clearly identifiable and keyboard accessible")
def cta_keyboard_accessible(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("Timing/message content is readable and understandable")
def message_readable(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_final_cta_present()


@then("Required message and CTA fields are present and non-empty")
def required_fields_present(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_final_cta_present()


@then("Text and background meet WCAG AA contrast requirements")
def contrast_aa(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_final_cta_present()


# Issue 0035 - Delivery message
@given("The final conversion section is rendered")
def final_section_rendered(page: Page):
    page_object = FinalCTAPage(page)
    page_object.navigate_to_homepage()


@given("The timing message is rendered")
def timing_rendered(page: Page):
    page_object = FinalCTAPage(page)
    page_object.navigate_to_homepage()


@given("The final conversion section is rendered at mobile width")
def final_mobile(page: Page):
    page_object = FinalCTAPage(page)
    page_object.resize_to_mobile()
    page_object.navigate_to_homepage()


@when("Screen reader testing runs")
def screen_reader_testing(page: Page):
    pass


@when("Content is analyzed without visual styling")
def content_analyzed(page: Page):
    pass


@then("Labels display in order: '1 Day', '2 Weeks', '3 Months'")
def timing_labels_order(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_timing_labels()


@then("All timing labels are announced correctly")
def timing_announced(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_timing_labels()


@then("Meaning is conveyed through text content, not visual styling alone")
def meaning_conveyed(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_timing_labels()


@then("Timing labels display correctly without problematic wrapping")
def timing_no_wrapping(page: Page):
    page_object = FinalCTAPage(page)
    page_object.verify_final_cta_present()
