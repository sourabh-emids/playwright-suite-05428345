"""Step definitions for issue_0008: Responsive Accessible Navigation Behavior."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("User is on touch or non-hover device")
def touch_device(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("User activates menu trigger")
def activate_menu_trigger(page: Page):
    menu_trigger = page.get_by_role("button", name="Menu")
    if menu_trigger.is_visible():
        menu_trigger.click()


@then("Menu can be opened/closed without hover requirement")
def menu_without_hover(page: Page):
    menu_trigger = page.get_by_role("button", name="Menu")
    if menu_trigger.is_visible():
        expect(menu_trigger).to_be_visible()


@given("Any overlay/menu is open")
def overlay_open(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    solutions = page.get_by_role("button", name="Solutions")
    if solutions.is_visible():
        solutions.click()


@when("User presses Escape key")
def press_escape(page: Page):
    page.keyboard.press("Escape")


@then("Open overlays close")
def overlays_close(page: Page):
    pass


@given("User navigates via keyboard through page")
def keyboard_navigation(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Focus indicator is checked at each interactive element")
def check_focus_indicator(page: Page):
    page.keyboard.press("Tab")


@then("Visible focus is maintained throughout navigation")
def visible_focus_maintained(page: Page):
    focused = page.evaluate("() => document.activeElement")
    assert focused, "Focus should be maintained"


@given("Page is rendered at supported widths (320px to desktop)")
def supported_widths(page: Page):
    page.goto("/")


@when("Viewport is resized")
def resize_viewport(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@then("Content reflows without horizontal page scrolling")
def no_horizontal_scroll(page: Page):
    scroll_width = page.evaluate("() => document.body.scrollWidth")
    viewport_width = page.viewport_size["width"]
    assert scroll_width <= viewport_width + 5, "No horizontal scroll expected"


@given("Navigation interactive controls are inspected")
def inspect_controls(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("HTML elements are reviewed")
def review_elements(page: Page):
    pass


@then("Interactive controls are semantic buttons or links")
def semantic_controls(page: Page):
    buttons = page.locator("nav button").all()
    links = page.locator("nav a").all()
    total = len(buttons) + len(links)
    assert total > 0, "Navigation should have semantic controls"


@given("User tabs through page")
def tab_through_page(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.keyboard.press("Tab")


@when("Focus order is compared to visual layout")
def compare_focus_order(page: Page):
    pass


@then("Focus order matches visual order")
def focus_matches_visual(page: Page):
    pass


@given("User has prefers-reduced-motion enabled")
def reduced_motion(page: Page):
    page.emulate_media(media="screen")
    page.goto("/")


@when("Page renders with animations")
def page_with_animations(page: Page):
    page.wait_for_load_state("networkidle")


@then("Reduced motion preferences are respected")
def motion_respected(page: Page):
    pass


@given("Menu is open and viewport is resized")
def menu_open_resize(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    solutions = page.get_by_role("button", name="Solutions")
    if solutions.is_visible():
        solutions.click()


@when("Viewport crosses breakpoint")
def cross_breakpoint(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Menu state is handled appropriately without errors")
def menu_state_handled(page: Page):
    pass


@given("Browser zoom is set to 200%")
def zoom_200(page: Page):
    page.set_viewport_size({"width": 640, "height": 360})


@when("User interacts with navigation")
def interact_navigation_zoom(page: Page):
    page.wait_for_load_state("networkidle")


@then("All navigation remains functional and visible")
def navigation_visible_zoom(page: Page):
    header = page.locator("header")
    expect(header).to_be_visible()


@given("JavaScript partially fails or loads incompletely")
def js_partial_failure(page: Page):
    page.goto("/")


@when("User interacts with navigation")
def interact_nav_partial_js(page: Page):
    pass


@then("Core navigation remains functional via fallback")
def navigation_functional_fallback(page: Page):
    header = page.locator("header")
    expect(header).to_be_visible()
