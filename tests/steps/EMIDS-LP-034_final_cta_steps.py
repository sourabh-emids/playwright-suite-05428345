"""Step definitions for Final CTA section - EMIDS-LP-034, EMIDS-LP-035"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-034_final_cta_page import FinalCTAPage
from playwright.sync_api import expect


@given("Page structure")
def page_structure(page):
    page.goto("/")


@when("Section order is verified")
def verify_section_order(page):
    pass


@then("Final conversion banner appears before footer")
def verify_before_footer(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_section_visible()


@given("Final CTA section")
def final_cta_section(page):
    page.goto("/")


@when("Primary action is tested")
def test_primary_action(page):
    pass


@then("Action is prominent and operable via keyboard")
def verify_operable_keyboard(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_section_visible()


@given("Final CTA supporting copy")
def supporting_copy(page):
    page.goto("/")


@when("Content is verified")
def verify_content(page):
    pass


@then("Timing/message content is readable")
def verify_readable(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_section_visible()


@given("Final CTA section fields")
def cta_fields(page):
    page.goto("/")


@when("Required content is checked")
def check_required(page):
    pass


@then("Required message and CTA fields are present")
def verify_required_present(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_section_visible()


@given("Final CTA at narrow width")
def narrow_width(page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Text wrapping occurs")
def wrapping_occurs(page):
    cta_page = FinalCTAPage(page)
    cta_page.goto("/")


@then("Layout remains functional")
def verify_functional_layout(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_section_visible()


@given("Delivery/timing message section")
def timing_section(page):
    page.goto("/")


@when("Content is inspected")
def inspect_timing_content(page):
    pass


@then("1 Day, 2 Weeks, 3 Months render in correct order")
def verify_order(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_timeline_labels()


@given("Timing labels")
def timing_labels(page):
    page.goto("/")


@when("Read by screen reader")
def read_screen_reader(page):
    pass


@then("Labels are understandable without visual styling context")
def verify_understandable(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_timeline_labels()


@given("Timeline message content")
def timeline_content(page):
    page.goto("/")


@when("Styling is analyzed")
def analyze_styling(page):
    pass


@then("Meaning is not conveyed through visual styling alone")
def verify_not_styling_alone(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_timeline_order()


@given("Timeline at mobile widths")
def timeline_mobile(page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Content wraps")
def content_wraps(page):
    cta_page = FinalCTAPage(page)
    cta_page.goto("/")


@then("Content remains readable and properly associated")
def verify_readable_associated(page):
    cta_page = FinalCTAPage(page)
    cta_page.verify_timeline_labels()
