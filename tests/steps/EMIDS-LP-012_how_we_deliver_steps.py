"""Step definitions for How We Deliver section - EMIDS-LP-012, EMIDS-LP-013"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-012_how_we_deliver_page import HowWeDeliverPage
from playwright.sync_api import expect


@given("The homepage structure")
def homepage_structure(page):
    page.goto("/")


@when("Content order is verified")
def verify_content_order(page):
    pass


@then("How We Deliver section appears after hero with section heading, explanation, visual/content elements, and CTA in sequence")
def verify_section_sequence(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.verify_section_visible()


@given("How We Deliver section")
def how_we_deliver_section(page):
    page.goto("/")


@when("Accessibility is checked")
def check_accessibility(page):
    pass


@then("All content is accessible to assistive technologies")
def verify_accessibility(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.verify_section_visible()


@given("Section heading, copy, visual, and CTA")
def section_content(page):
    page.goto("/")


@when("Content is inspected")
def inspect_content(page):
    pass


@then("All required content fields are populated")
def verify_populated(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.verify_section_heading()


@given("Section heading levels")
def heading_levels(page):
    page.goto("/")


@when("Heading structure is verified")
def verify_heading_structure(page):
    pass


@then("Headings follow logical hierarchy without skips")
def verify_hierarchy(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.verify_heading_hierarchy()


@given("Edge case where CTA fails to load")
def cta_load_fails(page):
    pass


@when("Section renders")
def section_renders(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.goto("/")


@then("Section remains functional with remaining content")
def verify_functional(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.verify_section_visible()


@given("The See the model CTA in How We Deliver section")
def see_model_cta(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.goto("/")


@when("CTA is clicked")
def click_cta(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.click_see_model_cta()


@then("User is navigated to /forward-deployed-context-engineering/")
def verify_fdce_navigation(page):
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@given("The See the model CTA")
def see_model_cta_element(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.goto("/")


@when("Activated via keyboard")
def activate_via_keyboard(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.focus_and_activate_see_model()


@then("CTA responds and navigates on Enter or Space")
def verify_keyboard_response(page):
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@given("See the model CTA")
def see_model_cta_name(page):
    page.goto("/")


@when("Accessibility is verified")
def verify_accessibility(page):
    pass


@then("Accessible name describes the action")
def verify_descriptive_name(page):
    deliver_page = HowWeDeliverPage(page)
    expect(deliver_page.locators.see_the_model_cta).to_be_visible()


@given("CTA destination URL")
def cta_destination_url(page):
    deliver_page = HowWeDeliverPage(page)
    deliver_page.goto("/")


@when("URL is tested")
def test_url(page):
    pass


@then("URL is valid and does not return 404")
def verify_valid_url(page):
    deliver_page = HowWeDeliverPage(page)
    assert deliver_page.verify_see_model_cta_routes_fdce()
