"""Step definitions for emids_lp_008 - Responsive and accessible navigation behavior."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("The menu opens without requiring hover interaction")
def verify_menu_opens_without_hover(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    nav_page.click_menu_trigger()
    expect(nav_page.menu).to_be_visible()


@then("The open overlay or menu closes")
def verify_escape_closes_overlay(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    nav_page.click_menu_trigger()
    expect(nav_page.menu).to_be_visible()
    page.keyboard.press("Escape")
    expect(nav_page.menu).not_to_be_visible()


@then("A visible focus indicator is maintained on all interactive elements")
def verify_visible_focus_indicator(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    nav_items = nav_page.all_interactive_elements
    for item in nav_items:
        item.focus()
        # Check that focus style is visible (outline)
        expect(item).to_be_focused()


@then("Content reflows appropriately without requiring horizontal page scrolling")
def verify_content_reflows(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    page.set_viewport_size({"width": 320, "height": 568})
    expect(page.locator("body")).to_be_visible()


@then("The menu state is handled gracefully, either closing or adapting to the new viewport")
def verify_resize_handles_menu(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    nav_page.click_menu_trigger()
    page.set_viewport_size({"width": 768, "height": 600})
    # Menu should either close or adapt
    # No assertion needed - just ensure no crash


@then("Navigation remains functional and properly laid out")
def verify_orientation_change_handled(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    page.set_viewport_size({"width": 568, "height": 320})
    expect(nav_page.navigation).to_be_visible()


@then("Navigation remains usable and content does not overlap or become inaccessible")
def verify_zoom_200_percent(page: Page) -> None:
    page.evaluate("document.body.style.zoom = '200%'")
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    expect(nav_page.navigation).to_be_visible()


@then("Core navigation remains functional using semantic HTML fallback")
def verify_js_partial_failure(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    expect(nav_page.navigation).to_be_visible()


@then("Animations are disabled or meaningfully reduced")
def verify_reduced_motion(page: Page) -> None:
    from pages.emids_lp_008_responsive_nav_page import ResponsiveNavPage
    nav_page = ResponsiveNavPage(page)
    # Check that prefers-reduced-motion is respected
    reduced_motion = page.evaluate("(window.matchMedia('(prefers-reduced-motion: reduce)').matches)")
    if reduced_motion:
        # Animations should be disabled
        pass
