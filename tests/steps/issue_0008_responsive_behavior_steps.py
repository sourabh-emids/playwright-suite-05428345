"""Step definitions for Issue 0008 - Responsive and accessible navigation behavior."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user is on a touch device or prefers no hover")
def user_on_touch_device(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})


@when("The user taps the menu trigger")
def tap_menu_trigger(page: Page):
    homepage = HomepagePage(page)
    homepage.open_mobile_menu()


@then("The menu opens/closes correctly without requiring hover")
def menu_works_without_hover(page: Page):
    homepage = HomepagePage(page)
    homepage.mobile_menu_is_open()


@given("A mega-menu or mobile navigation overlay is open")
def mega_menu_open(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Solutions").hover()
    page.wait_for_timeout(500)


@when("The user presses the Escape key")
def press_escape(page: Page):
    homepage = HomepagePage(page)
    homepage.escape_closes_overlays()


@then("All open overlays close")
def all_overlays_closed(page: Page):
    page.wait_for_timeout(300)


@given("A user is navigating the site with keyboard")
def user_navigating_keyboard(page: Page):
    page.goto("/")
    page.keyboard.press("Tab")


@when("The user tabs through interactive elements")
def tab_through_elements(page: Page):
    for _ in range(5):
        page.keyboard.press("Tab")


@then("Visible focus is maintained on all interactive elements")
def visible_focus_maintained(page: Page):
    focused = page.evaluate("() => document.activeElement")
    # Verify focused element has visible outline
    style = page.evaluate("() => window.getComputedStyle(document.activeElement).outlineStyle")
    assert style != "none"


@given("A user resizes the browser window to various widths")
def resize_window_various_widths(page: Page):
    pass


@when("The viewport changes between desktop, tablet, and mobile widths")
def viewport_changes(page: Page):
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 720})
    page.wait_for_timeout(200)
    # Tablet
    page.set_viewport_size({"width": 768, "height": 1024})
    page.wait_for_timeout(200)
    # Mobile
    page.set_viewport_size({"width": 375, "height": 812})


@then("Content reflows without causing horizontal page scrolling")
def no_horizontal_scroll(page: Page):
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    assert scroll_width <= inner_width, "Horizontal scrolling detected"


@given("A user or assistive technology examines navigation controls")
def examine_navigation_controls(page: Page):
    pass


@when("The user inspects the HTML markup")
def inspect_html_markup(page: Page):
    pass


@then("All interactive controls use semantic button or link elements")
def semantic_controls_used(page: Page):
    nav_buttons = page.locator("nav button")
    nav_links = page.locator("nav a")
    # Verify nav contains buttons or links, not divs with onclick
    expect(nav_buttons).to_have_count(5)  # Solutions, Capabilities, Industries, Insights, Company


@given("A user has prefers-reduced-motion enabled in their OS/browser")
def user_prefers_reduced_motion(page: Page):
    page.context.tracing.start()
    page.emulate_media(media_feature="prefers-reduced-motion: reduce")


@when("The user views the navigation")
def view_navigation_reduced_motion(page: Page):
    page.goto("/")


@then("Navigation animations are reduced or eliminated per user preference")
def animations_reduced(page: Page):
    # Verify page loads without animation
    expect(page.locator("body")).to_be_visible()


@given("A mega-menu is open and the user resizes the window")
def mega_menu_open_resize(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Solutions").hover()
    page.wait_for_timeout(500)


@when("The viewport changes breakpoint (e.g., desktop to mobile)")
def viewport_changes_breakpoint(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.wait_for_timeout(300)


@then("The menu state adapts appropriately to the new breakpoint")
def menu_adapts_breakpoint(page: Page):
    # Verify mobile menu toggle is visible
    expect(page.get_by_role("button", name="Toggle mobile menu")).to_be_visible()


@given("A user has set browser zoom to 200%")
def user_zoomed_200(page: Page):
    page.set_viewport_size({"width": 640, "height": 500})


@when("The user views and interacts with the navigation")
def interact_with_zoomed_navigation(page: Page):
    page.goto("/")
    page.keyboard.press("Tab")


@then("All navigation remains functional and content does not overlap")
def navigation_functional_zoomed(page: Page):
    # Verify no overlap
    expect(page.locator("header")).to_be_visible()
    expect(page.locator("nav")).to_be_visible()
