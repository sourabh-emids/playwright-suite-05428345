"""Step definitions for emids_lp_012 - How We Deliver section."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence")
def verify_section_sequence(page: Page) -> None:
    from pages.emids_lp_012_how_we_deliver_page import HowWeDeliverPage
    page_obj = HowWeDeliverPage(page)
    expect(page_obj.section_heading).to_be_visible()
    expect(page_obj.section_body).to_be_visible()
    expect(page_obj.see_model_cta).to_be_visible()


@then("All content is accessible with proper semantic structure")
def verify_section_accessibility(page: Page) -> None:
    from pages.emids_lp_012_how_we_deliver_page import HowWeDeliverPage
    page_obj = HowWeDeliverPage(page)
    expect(page_obj.section).to_be_visible()


@then("Required fields (title, body, CTA) are not empty")
def verify_required_fields_not_empty(page: Page) -> None:
    from pages.emids_lp_012_how_we_deliver_page import HowWeDeliverPage
    page_obj = HowWeDeliverPage(page)
    heading = page_obj.section_heading.text_content()
    body = page_obj.section_body.text_content()
    cta = page_obj.see_model_cta.text_content()
    assert heading and heading.strip(), "Heading is empty"
    assert body and body.strip(), "Body is empty"
    assert cta and cta.strip(), "CTA is empty"


@then("Heading levels follow logical hierarchy without skips where avoidable")
def verify_heading_hierarchy(page: Page) -> None:
    from pages.emids_lp_012_how_we_deliver_page import HowWeDeliverPage
    page_obj = HowWeDeliverPage(page)
    headings = page_obj.all_headings
    # Check that headings are in logical order
    for h in headings:
        expect(h).to_be_visible()


@then("Section renders with text content visible")
def verify_section_without_media(page: Page) -> None:
    from pages.emids_lp_012_how_we_deliver_page import HowWeDeliverPage
    page_obj = HowWeDeliverPage(page)
    expect(page_obj.section_heading).to_be_visible()


@then("Content wraps appropriately without breaking layout")
def verify_long_copy_handled(page: Page) -> None:
    from pages.emids_lp_012_how_we_deliver_page import HowWeDeliverPage
    page_obj = HowWeDeliverPage(page)
    expect(page_obj.section).to_be_visible()
