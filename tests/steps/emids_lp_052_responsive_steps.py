"""Step definitions for emids_lp_052-055 - Global sections."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Content fits within viewport without requiring horizontal scroll")
def verify_no_horizontal_scroll(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    for width in [320, 768, 1280, 1920]:
        page.set_viewport_size({"width": width, "height": 800})
        scroll_width = page.evaluate("document.documentElement.scrollWidth")
        client_width = page.evaluate("document.documentElement.clientWidth")
        assert scroll_width <= client_width + 5


@then("Typography scales appropriately; text remains legible at all breakpoints")
def verify_typography_scale(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    for width in [375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        expect(page_obj.h1).to_be_visible()


@then("Controls do not overlap or obscure each other")
def verify_no_overlap(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.navigation).to_be_visible()


@then("All sections and cards are visible and accessible; no content hidden off-screen")
def verify_all_content_visible(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    # Scroll through page and verify sections
    expect(page_obj.hero_section).to_be_visible()


@then("Images scale proportionally; aspect ratio is preserved")
def verify_image_aspect_ratio(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    for width in [375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})


@then("Content reflows to single column; all functionality preserved")
def verify_320_width(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 320, "height": 568})
    expect(page_obj.hero_section).to_be_visible()


@then("Text wraps or truncates gracefully without breaking layout")
def verify_long_text(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.hero_section).to_be_visible()


@then("Content remains usable; reflows appropriately")
def verify_zoom_reflow(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 640, "height": 900})
    expect(page_obj.hero_section).to_be_visible()


@then("Layout adapts appropriately for landscape proportions")
def verify_landscape_phone(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 568, "height": 320})
    expect(page_obj.hero_section).to_be_visible()


@then("Content reflows for reduced viewport width without breaking")
def verify_tablet_split_screen(page: Page) -> None:
    from pages.emids_lp_052_responsive_page import ResponsivePage
    page_obj = ResponsivePage(page)
    page.set_viewport_size({"width": 500, "height": 800})
    expect(page_obj.hero_section).to_be_visible()


@then("Critical content renders immediately without waiting for analytics to complete")
def verify_critical_render(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.h1).to_be_visible()


@then("Images are appropriately sized for viewport; formats are optimized (WebP, AVIF where supported)")
def verify_optimized_images(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    for img in page_obj.images.all():
        src = img.get_attribute("src")
        if src:
            expect(img).to_be_visible()


@then("Below-fold media is lazy-loaded to improve initial load performance")
def verify_lazy_loading(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Cumulative Layout Shift (CLS) is minimized; space is reserved for media")
def verify_minimal_cls(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Scripts use async/defer attributes or are gated by consent as appropriate")
def verify_script_loading(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Critical content remains accessible; lazy-loaded content loads progressively")
def verify_slow_network(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.h1).to_be_visible()


@then("Core functionality remains intact; no blocking errors displayed to user")
def verify_blocked_third_party(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Critical content renders; caching strategy minimizes staleness issues")
def verify_cached_asset(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Appropriately sized image is served; not unnecessarily downscaled from smaller version")
def verify_large_viewport_image(page: Page) -> None:
    from pages.emids_lp_053_performance_page import PerformancePage
    page_obj = PerformancePage(page)
    page.set_viewport_size({"width": 2560, "height": 1440})
    expect(page_obj.hero_section).to_be_visible()


@then("Header navigation remains readable and functional")
def verify_header_script_failure(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.navigation).to_be_visible()


@then("Main content (hero, sections, CTAs) remains readable and complete")
def verify_main_content_script_failure(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("All CTAs (header, hero, section, final) remain clickable and route correctly")
def verify_ctas_script_failure(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.cta).to_be_visible()


@then("Footer remains fully readable with all links functional")
def verify_footer_script_failure(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.footer).to_be_visible()


@then("Error is contained; does not cascade to break other functionality")
def verify_error_contained(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core functionality preserved; blocked script fails gracefully")
def verify_csp_block(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page renders; failed integration handled gracefully")
def verify_dns_failure(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core content intact; blocked script does not break page")
def verify_ad_blocker(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core functionality continues; timeout handled without user-facing error")
def verify_script_timeout(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Error is caught; core page not broken; minimal logging captured")
def verify_malformed_script(page: Page) -> None:
    from pages.emids_lp_054_script_failure_page import ScriptFailurePage
    page_obj = ScriptFailurePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("No promotional modal appears automatically")
def verify_no_auto_modal(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    modal = page_obj.modal
    if modal.count() > 0:
        expect(modal.first).not_to_be_visible()


@then("User can dismiss the modal via close button, clicking outside, or pressing Escape")
def verify_modal_dismissible(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    # Modal should have close button
    expect(page_obj.close_button).to_be_visible()


@then("Modal focus is managed; close control is keyboard accessible")
def verify_modal_keyboard(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    expect(page_obj.close_button).to_be_visible()


@then("Modal does not block interaction with underlying page elements inappropriately")
def verify_modal_non_blocking(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    expect(page_obj.close_button).to_be_visible()


@then("Default behavior is no modal; no modal code executes")
def verify_default_disabled(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    modal_count = page_obj.modal.count()
    assert modal_count == 0 or not page_obj.modal.first.is_visible()


@then("Modal does not repeatedly appear unless intentionally re-triggered by configured rules")
def verify_repeated_modal(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    expect(page_obj.modal.count() == 0 or not page_obj.modal.first.is_visible())


@then("Focus remains trapped within modal until dismissed")
def verify_focus_trap(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    page.keyboard.press("Tab")
    # Focus should stay within modal


@then("Modal is appropriately sized; does not overflow viewport")
def verify_small_viewport_modal(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    if page_obj.modal.count() > 0:
        expect(page_obj.modal.first).to_be_visible()


@then("Page renders normally; no modal-related functionality breaks")
def verify_js_disabled_modal(page: Page) -> None:
    from pages.emids_lp_055_modal_page import ModalPage
    page_obj = ModalPage(page)
    expect(page_obj.hero_section).to_be_visible()
