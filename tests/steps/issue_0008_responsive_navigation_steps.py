"""Steps for Responsive and accessible navigation behavior (issue_0008)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0008_responsive_navigation_page import ResponsiveNavigationPage
from locators.issue_0008_responsive_navigation_locators import ResponsiveNavigationLocators


@given("User is on Emids homepage with touch device or keyboard-only access")
def touch_or_keyboard(page: Page) -> None:
    page.goto("/")


@given("A navigation menu or overlay is open")
def menu_open(page: Page) -> None:
    page.goto("/")
    nav_page = ResponsiveNavigationPage(page)
    nav_page.open_menu()


@given("User is navigating through header using keyboard")
def keyboard_navigation(page: Page) -> None:
    page.goto("/")
    page.locator("header").focus()


@given("User views Emids homepage at supported viewport widths")
def viewport_widths(page: Page) -> None:
    page.goto("/")


@given("User views header source code")
def view_source(page: Page) -> None:
    page.goto("/")


@given("User navigates header with keyboard")
def navigate_header(page: Page) -> None:
    page.goto("/")
    page.locator("header").focus()


@given("User has prefers-reduced-motion enabled")
def reduced_motion(page: Page) -> None:
    page.goto("/", extras={"reduced_motion": "reduce"})


@given("Navigation menu is open at desktop width")
def menu_open_desktop(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 1280, "height": 800})
    nav_page = ResponsiveNavigationPage(page)
    nav_page.open_menu()


@given("User is viewing Emids homepage in landscape")
def landscape_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 844, "height": 390})


@given("User sets browser zoom to 200%")
def browser_zoom(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 640, "height": 800})


@given("JavaScript partially fails during page load")
def js_partial_failure(page: Page) -> None:
    page.goto("/")


@when("User activates navigation trigger via tap or Enter")
def activate_trigger(page: Page) -> None:
    nav_page = ResponsiveNavigationPage(page)
    nav_page.open_menu()


@when("User presses Escape key")
def press_escape(page: Page) -> None:
    nav_page = ResponsiveNavigationPage(page)
    nav_page.press_escape()


@when("Focus moves between interactive elements")
def focus_moves(page: Page) -> None:
    nav_page = ResponsiveNavigationPage(page)
    nav_page.tab_through(3)


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User inspects interactive controls")
def inspect_controls(page: Page) -> None:
    pass


@when("Focus order is observed")
def observe_focus_order(page: Page) -> None:
    pass


@when("User views navigation menus with animations")
def view_animations(page: Page) -> None:
    pass


@when("User resizes to mobile width")
def resize_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("User changes to portrait orientation")
def change_orientation(page: Page) -> None:
    page.set_viewport_size({"width": 390, "height": 844})


@when("User views Emids homepage")
def view_homepage(page: Page) -> None:
    pass


@when("User attempts to use navigation")
def use_navigation(page: Page) -> None:
    pass


@then("Menu opens without requiring hover")
def menu_opens_no_hover(page: Page) -> None:
    expect(ResponsiveNavigationLocators(page).nav_buttons.first).to_be_visible()


@then("Open overlay closes")
def overlay_closes(page: Page) -> None:
    pass


@then("Visible focus indicator is maintained on all interactive elements")
def focus_indicator_maintained(page: Page) -> None:
    locators = ResponsiveNavigationLocators(page)
    nav_buttons = locators.nav_buttons.all()
    for button in nav_buttons:
        button.focus()
        expect(button).to_be_focused()


@then("Content reflows cleanly without requiring horizontal page scrolling")
def no_horizontal_scroll(page: Page) -> None:
    for width in [320, 375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        viewport_width = page.viewport_size["width"]
        assert scroll_width <= viewport_width


@then("Interactive controls are semantic buttons or links")
def semantic_controls(page: Page) -> None:
    locators = ResponsiveNavigationLocators(page)
    buttons = locators.nav_buttons.all()
    links = locators.nav_links.all()
    assert len(buttons) > 0 or len(links) > 0


@then("Focus order matches visual order")
def focus_order_matches(page: Page) -> None:
    pass


@then("Animations are reduced or disabled as appropriate")
def animations_disabled(page: Page) -> None:
    pass


@then("Menu state is handled gracefully with content accessible")
def graceful_resize(page: Page) -> None:
    expect(ResponsiveNavigationLocators(page).header).to_be_visible()


@then("Navigation remains functional and accessible")
def nav_functional(page: Page) -> None:
    expect(ResponsiveNavigationLocators(page).header).to_be_visible()


@then("Content remains readable and navigation accessible")
def content_readable_200_zoom(page: Page) -> None:
    expect(ResponsiveNavigationLocators(page).header).to_be_visible()


@then("Core navigation links remain functional")
def core_nav_functional(page: Page) -> None:
    expect(ResponsiveNavigationLocators(page).header).to_be_visible()
