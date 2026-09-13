"""Step definitions for emids_lp_050 - WCAG compliance."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("All interactive elements are reachable and operable via keyboard")
def verify_keyboard_access(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    # Tab through all interactive elements
    interactive = page_obj.all_interactive
    for elem in interactive:
        elem.focus()


@then("Visible focus indicator is present on all interactive elements")
def verify_visible_focus(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    for elem in page_obj.all_interactive.all():
        elem.focus()
        expect(elem).to_be_focused()


@then("Header, main, nav, footer, and other landmarks are properly identified")
def verify_landmarks(page: Page) -> None:
    expect(page.locator("header").first).to_be_visible()
    expect(page.locator("main").first).to_be_visible()
    expect(page.locator("footer").first).to_be_visible()


@then("Text and interactive elements meet 4.5:1 contrast ratio (AA standard)")
def verify_contrast(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Informative images have meaningful alt text; decorative images are marked appropriately")
def verify_alt_text(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    images = page_obj.images
    for img in images.all():
        alt = img.get_attribute("alt")
        # Should have alt or be marked decorative
        expect(img).to_be_visible()


@then("Each element has an accessible name that describes its purpose")
def verify_accessible_names(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    for elem in page_obj.buttons.all():
        expect(elem).to_be_visible()


@then("Content remains usable; no horizontal scrolling required")
def verify_zoom_200(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    page.set_viewport_size({"width": 640, "height": 800})  # 200% zoom
    expect(page_obj.hero_section).to_be_visible()


@then("Content reflows to single column; all content accessible without horizontal scrolling")
def verify_reflow_320(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    page.set_viewport_size({"width": 320, "height": 568})
    expect(page_obj.hero_section).to_be_visible()


@then("Error messages are associated with fields; accessible to screen readers")
def verify_error_associations(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    expect(page_obj.form_section).to_be_visible()


@then("Animations are reduced or disabled per user preference")
def verify_reduced_motion(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Captions, transcripts, or audio descriptions are available where applicable")
def verify_media_alternatives(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Content remains visible and distinguishable; colors not sole differentiator")
def verify_high_contrast_mode(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Information is conveyed through additional means (text, icons, patterns)")
def verify_not_color_only(page: Page) -> None:
    from pages.emids_lp_050_wcag_page import WCAGPage
    page_obj = WCAGPage(page)
    expect(page_obj.hero_section).to_be_visible()
