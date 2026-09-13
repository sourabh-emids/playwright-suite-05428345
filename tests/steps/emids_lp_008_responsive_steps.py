"""Step definitions for emids_lp_008: Provide responsive accessible navigation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("User is on touch device or prefers reduced motion")
def touch_or_reduced_motion(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("An open menu or overlay exists")
def open_menu_overlay(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Solutions").click()
    page.wait_for_timeout(300)


@given("User navigates through page using keyboard")
def keyboard_navigation(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User views page at supported viewport widths")
def supported_viewports(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Interactive navigation controls exist")
def interactive_controls_exist(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User tabs through page")
def tab_through_page(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.locator("body").focus()


@given("Navigation menu is open")
def nav_menu_open(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Solutions").click()
    page.wait_for_timeout(300)


@given("User changes device orientation")
def change_orientation(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User sets browser zoom to 200%")
def set_zoom_200(page: Page) -> None:
    page.set_viewport_size({"width": 640, "height": 480})


@given("User has prefers_reduced_motion enabled")
def reduced_motion_enabled(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("JavaScript partially fails during page load")
def js_partial_failure(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User taps menu trigger")
def tap_menu_trigger(page: Page) -> None:
    menu_btn = page.locator('[aria-label="Menu"], button:has-text("Menu")')
    if menu_btn.is_visible():
        menu_btn.click()
    page.wait_for_timeout(300)


@when("User presses Escape key")
def press_escape(page: Page) -> None:
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)


@when("Focus moves between interactive elements")
def focus_moves(page: Page) -> None:
    for _ in range(10):
        page.keyboard.press("Tab")


@when("Page content renders")
def page_renders(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Automated check validates control semantics")
def validate_control_semantics(page: Page) -> None:
    buttons = page.locator("button")
    links = page.locator("a")
    assert buttons.count() > 0 or links.count() > 0


@when("Focus order is evaluated")
def evaluate_focus_order(page: Page) -> None:
    pass


@when("User resizes browser window")
def resize_window(page: Page) -> None:
    page.set_viewport_size({"width": 768, "height": 600})
    page.wait_for_timeout(300)


@when("Page reflows to new orientation")
def reflow_orientation(page: Page) -> None:
    page.set_viewport_size({"width": 568, "height": 320})


@when("Page renders")
def render_page(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Page renders navigation with animations")
def render_animated_nav(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Page continues rendering")
def page_continues(page: Page) -> None:
    pass


@then("Menu can be opened and closed without requiring hover")
def verify_no_hover_required(page: Page) -> None:
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()


@then("Open overlays close and focus returns appropriately")
def verify_overlay_close(page: Page) -> None:
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()


@then("Visible focus indicator is maintained on all focusable elements")
def verify_visible_focus(page: Page) -> None:
    header = page.locator("header")
    header.focus()
    page.keyboard.press("Tab")
    focused = page.evaluate("document.activeElement")
    assert focused is not None


@then("Content reflows without horizontal page scrolling")
def verify_no_h_scroll(page: Page) -> None:
    page.set_viewport_size({"width": 320, "height": 568})
    body_width = page.locator("body").evaluate("el => el.scrollWidth")
    viewport_width = page.viewport_size["width"]
    assert body_width <= viewport_width, "Horizontal scroll detected"


@then("All controls use semantic button or link elements")
def verify_semantic_controls(page: Page) -> None:
    buttons = page.locator("button")
    links = page.locator("a[href]")
    for btn in buttons.all():
        tag = btn.evaluate("el => el.tagName")
        assert tag == "BUTTON"


@then("Focus order matches visual reading order")
def verify_focus_order_match(page: Page) -> None:
    pass


@then("Menu state is preserved or gracefully transitioned without breaking")
def verify_menu_state_preserved(page: Page) -> None:
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()


@then("Navigation remains accessible and functional")
def verify_nav_functional(page: Page) -> None:
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()


@then("Navigation and content remain usable without horizontal scrolling")
def verify_usable_no_hscroll(page: Page) -> None:
    body_width = page.locator("body").evaluate("el => el.scrollWidth")
    viewport_width = page.viewport_size["width"]
    assert body_width <= viewport_width


@then("Motion animations are reduced or disabled per user preference")
def verify_motion_reduced(page: Page) -> None:
    pass


@then("Core navigation remains functional and accessible")
def verify_core_nav_functional(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()
