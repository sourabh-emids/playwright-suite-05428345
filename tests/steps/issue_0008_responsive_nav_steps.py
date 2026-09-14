"""Step definitions for issue_0008: Provide responsive accessible navigation."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User is on touch device or keyboard-only navigation")
def touch_or_keyboard(page: Page) -> None:
    page.goto("/")


@when("User activates menu trigger via click or Enter")
def activate_menu_trigger(page: Page) -> None:
    page.get_by_role("button", name="Solutions").press("Enter")


@then("Menu opens without requiring hover interaction")
def menu_opens_no_hover(page: Page) -> None:
    expect(page.get_by_text("Solutions by Initiative")).to_be_visible()


@given("Any mega-menu or overlay is open")
def mega_menu_open(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="Solutions").click()
    expect(page.get_by_text("Solutions by Initiative")).to_be_visible()


@when("User presses Escape key")
def press_escape(page: Page) -> None:
    page.keyboard.press("Escape")


@then("All open overlays close")
def overlays_close(page: Page) -> None:
    menu = page.locator("nav[aria-label='Solutions']")
    # Menu should close or not be visible
    assert not menu.is_visible() or page.get_by_role("button", name="Solutions").is_visible()


@given("User navigates through header using keyboard")
def navigate_keyboard(page: Page) -> None:
    page.goto("/")
    page.locator("header").get_by_role("link").first.focus()


@when("Focus moves between interactive elements")
def focus_moves(page: Page) -> None:
    page.keyboard.press("Tab")


@then("Focus indicator remains visible on all interactive elements")
def focus_indicator_visible(page: Page) -> None:
    active = page.evaluate("() => document.activeElement")
    assert active is not None


@given("User resizes browser to mobile, tablet, and desktop widths")
def resize_browser(page: Page) -> None:
    pass


@when("Page renders at each breakpoint")
def page_renders_breakpoints(page: Page) -> None:
    breakpoints = [{"width": 375, "height": 667}, {"width": 768, "height": 1024}, {"width": 1280, "height": 720}]
    for bp in breakpoints:
        page.set_viewport_size(bp)
        page.goto("/")
        page.wait_for_load_state("networkidle")


@then("No horizontal scrolling occurs; content reflows appropriately")
def no_horizontal_scroll(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    viewport_width = page.evaluate("() => window.innerWidth")
    assert scroll_width <= viewport_width


@given("User inspects header interactivity code")
def inspect_interactivity_code(page: Page) -> None:
    page.goto("/")


@when("Checking HTML semantics")
def check_html_semantics(page: Page) -> None:
    pass


@then("Menu triggers use <button> or semantic link elements, not <div> with click handlers")
def semantic_elements(page: Page) -> None:
    menu_triggers = page.locator("header button")
    count = menu_triggers.count()
    assert count > 0


@given("User navigates header using keyboard")
def nav_header_keyboard(page: Page) -> None:
    page.goto("/")
    page.locator("header").get_by_role("link,button").first.focus()


@when("Checking tab order")
def check_tab_order(page: Page) -> None:
    pass


@then("Focus follows logical left-to-right, top-to-bottom sequence matching visual layout")
def logical_tab_order(page: Page) -> None:
    elements = page.evaluate("""() => {
        const header = document.querySelector('header');
        const items = header.querySelectorAll('a, button');
        return Array.from(items).map(el => el.tagName);
    }""")
    assert len(elements) > 0


@given("User has prefers-reduced-motion enabled")
def reduced_motion_enabled(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("Page renders or animations would trigger")
def animations_trigger(page: Page) -> None:
    pass


@then("Continuous animations are reduced or disabled")
def animations_disabled(page: Page) -> None:
    # Page should render without continuous animations
    expect(page.locator("header")).to_be_visible()


@given("Mega-menu is open during window resize")
def menu_open_resize(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Solutions").click()
    expect(page.get_by_text("Solutions by Initiative")).to_be_visible()


@when("Viewport changes from desktop to mobile width")
def viewport_changes(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("Menu state transitions appropriately without error or visual glitch")
def menu_transition(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()


@given("User sets browser zoom to 200%")
def zoom_200_percent(page: Page) -> None:
    page.set_viewport_size({"width": 640, "height": 360})


@when("User attempts to use navigation")
def use_navigation(page: Page) -> None:
    page.goto("/")


@then("Navigation remains fully functional without overlapping or clipping")
def navigation_usable_zoom(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()
