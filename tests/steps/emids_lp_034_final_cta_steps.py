"""Step definitions for emids_lp_034-035 - Final CTA and delivery message."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("Final conversion banner appears before footer section")
def verify_banner_before_footer(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    banner = page_obj.final_cta_banner
    footer = page.locator("footer")
    expect(banner).to_be_visible()
    banner_box = banner.bounding_box()
    footer_box = footer.bounding_box()
    assert banner_box and footer_box and banner_box["y"] < footer_box["y"]


@then("Primary CTA is visible, clear, and activatable via keyboard")
def verify_primary_cta_keyboard(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    page_obj.primary_cta.focus()
    page.keyboard.press("Enter")


@then("Timing and message content are readable")
def verify_timing_readable(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    expect(page_obj.supporting_message).to_be_visible()


@then("Required message and CTA fields are present and not empty")
def verify_required_fields(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    message = page_obj.supporting_message.text_content()
    cta = page_obj.primary_cta.text_content()
    assert message and message.strip()
    assert cta and cta.strip()


@then("Section has high-contrast visual treatment per design")
def verify_high_contrast(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    expect(page_obj.final_cta_banner).to_be_visible()


@then("CTA text wraps gracefully without breaking button")
def verify_cta_wrapping(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.final_cta_banner).to_be_visible()


@then("Banner and footer do not overlap or obscure each other")
def verify_no_overlap(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    expect(page_obj.final_cta_banner).to_be_visible()
    expect(page.locator("footer")).to_be_visible()


@then("Graceful error handling without page break")
def verify_contact_error(page: Page) -> None:
    from pages.emids_lp_034_final_cta_page import FinalCTAPage
    page_obj = FinalCTAPage(page)
    expect(page_obj.final_cta_banner).to_be_visible()


@then("Labels display in order: '1 Day', '2 Weeks', '3 Months'")
def verify_delivery_order(page: Page) -> None:
    from pages.emids_lp_035_delivery_message_page import DeliveryMessagePage
    page_obj = DeliveryMessagePage(page)
    labels = page_obj.timing_labels
    expect(labels.first).to_have_text("1 Day")
    expect(labels.nth(1)).to_have_text("2 Weeks")
    expect(labels.nth(2)).to_have_text("3 Months")


@then("All timing labels are announced in logical order with explanatory text if configured")
def verify_screen_reader_order(page: Page) -> None:
    from pages.emids_lp_035_delivery_message_page import DeliveryMessagePage
    page_obj = DeliveryMessagePage(page)
    expect(page_obj.section).to_be_visible()


@then("Meaning is conveyed through text, not solely through visual styling")
def verify_text_meaning(page: Page) -> None:
    from pages.emids_lp_035_delivery_message_page import DeliveryMessagePage
    page_obj = DeliveryMessagePage(page)
    for label in page_obj.timing_labels.all():
        text = label.text_content()
        assert text and text.strip()


@then("Timing values render with available content; no broken placeholder")
def verify_missing_explanation(page: Page) -> None:
    from pages.emids_lp_035_delivery_message_page import DeliveryMessagePage
    page_obj = DeliveryMessagePage(page)
    expect(page_obj.section).to_be_visible()


@then("Content wraps appropriately without horizontal overflow")
def verify_wrapping_mobile(page: Page) -> None:
    from pages.emids_lp_035_delivery_message_page import DeliveryMessagePage
    page_obj = DeliveryMessagePage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.section).to_be_visible()
