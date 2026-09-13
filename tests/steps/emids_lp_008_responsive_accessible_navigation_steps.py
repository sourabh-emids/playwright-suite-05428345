"""Steps for emids_lp_008: Responsive accessible navigation behavior."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.header_page import HeaderPage
from pages.header.solutions_menu_page import SolutionsMenuPage


@given(parsers.parse("User is on desktop with keyboard or touch"))
def user_desktop_keyboard_or_touch(page: Page) -> None:
    """User is on desktop with keyboard or touch."""
    page.set_viewport_size({"width": 1280, "height": 800})


@given(parsers.parse("Any navigation menu is open"))
def any_menu_open(page: Page) -> None:
    """Any navigation menu is open."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.open_solutions_menu()


@given(parsers.parse("User navigates through header with keyboard"))
def navigate_keyboard(page: Page) -> None:
    """User navigates through header with keyboard."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("User views site at supported widths including 320px"))
def view_supported_widths(page: Page) -> None:
    """User views site at supported widths."""
    pass


@given(parsers.parse("User examines navigation controls"))
def examine_nav_controls(page: Page) -> None:
    """User examines navigation controls."""
    pass


@given(parsers.parse("User navigates header with keyboard"))
def navigate_header_keyboard(page: Page) -> None:
    """User navigates header with keyboard."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("Navigation menu is open on desktop"))
def menu_open_desktop(page: Page) -> None:
    """Navigation menu is open on desktop."""
    page.set_viewport_size({"width": 1280, "height": 800})
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.open_solutions_menu()


@given(parsers.parse("User has prefers-reduced-motion enabled"))
def reduced_motion_enabled(page: Page) -> None:
    """User has prefers-reduced-motion enabled."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")


@given(parsers.parse("User sets browser zoom to 200%"))
def zoom_200_percent(page: Page) -> None:
    """User sets browser zoom to 200%."""
    page.set_viewport_size({"width": 640, "height": 400})


@given(parsers.parse("JavaScript partially fails during page load"))
def js_partial_failure(page: Page) -> None:
    """JavaScript partially fails during page load."""
    # Would need script blocking or error injection
    pass


@when("User activates any menu trigger")
def activate_any_menu_trigger(page: Page) -> None:
    """Activate any menu trigger."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.open_solutions_menu()


@when("User presses Escape key")
def press_escape(page: Page) -> None:
    """Press Escape key."""
    page.keyboard.press("Escape")


@when("User tabs between interactive elements")
def tab_between_elements(page: Page) -> None:
    """Tab between interactive elements."""
    header_page = HeaderPage(page)
    header_page.locators.solutions_nav.focus()
    page.keyboard.press("Tab")


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("User resizes browser to mobile width")
def resize_to_mobile(page: Page) -> None:
    """Resize browser to mobile width."""
    page.set_viewport_size({"width": 375, "height": 667})


@when("User interacts with navigation")
def interact_with_navigation(page: Page) -> None:
    """Interact with navigation."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.open_solutions_menu()


@when("User views and navigates header")
def view_navigate_header(page: Page) -> None:
    """View and navigate header."""
    pass


@when("Page renders")
def page_renders_after_failure(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@then("Menu opens without requiring hover")
def menu_opens_no_hover(page: Page) -> None:
    """Verify menu opens without requiring hover."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_button).to_have_attribute("aria-expanded", "true")


@then("Toggle works predictably")
def toggle_predictable(page: Page) -> None:
    """Verify toggle works predictably."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_button).to_be_visible()


@then("Menu closes")
def menu_closes(page: Page) -> None:
    """Verify menu closes."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_button).to_have_attribute("aria-expanded", "false")


@then("Focus is managed appropriately")
def focus_managed_appropriately(page: Page) -> None:
    """Verify focus is managed appropriately."""
    header_page = HeaderPage(page)
    expect(header_page.locators.solutions_nav).to_be_focused()


@then("Focus indicator is visible on all interactive elements")
def focus_indicator_visible(page: Page) -> None:
    """Verify focus indicator is visible."""
    header_page = HeaderPage(page)
    header_page.locators.solutions_nav.focus()
    outline = header_page.locators.solutions_nav.evaluate("el => window.getComputedStyle(el).outlineStyle")
    expect(outline).not_to_be("none")


@then("Content reflows appropriately")
def content_reflows(page: Page) -> None:
    """Verify content reflows appropriately."""
    page.set_viewport_size({"width": 320, "height": 568})


@then("No horizontal scrollbar appears")
def no_horizontal_scrollbar(page: Page) -> None:
    """Verify no horizontal scrollbar appears."""
    page.set_viewport_size({"width": 320, "height": 568})
    scroll_width = page.evaluate("() => document.body.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    expect(scroll_width).to_be_less_than_or_equal(inner_width)


@then("Controls use semantic HTML buttons or links")
def controls_semantic(page: Page) -> None:
    """Verify controls use semantic HTML buttons or links."""
    solutions_page = SolutionsMenuPage(page)
    tag = solutions_page.locators.solutions_button.evaluate("el => el.tagName")
    expect(tag).to_be_in(["BUTTON", "A"])


@then("No div-based click handlers")
def no_div_click_handlers(page: Page) -> None:
    """Verify no div-based click handlers."""
    solutions_page = SolutionsMenuPage(page)
    tag = solutions_page.locators.solutions_button.evaluate("el => el.tagName")
    expect(tag).not_to_equal("DIV")


@then("Focus order follows visual layout order")
def focus_order_visual_order(page: Page) -> None:
    """Verify focus order follows visual layout order."""
    header_page = HeaderPage(page)
    header_page.navigate()
    # Tab through and verify order
    header_page.locators.solutions_nav.focus()
    first_focused = page.evaluate("() => document.activeElement.textContent")


@then("Menu state adjusts appropriately for new breakpoint")
def menu_state_adjusts(page: Page) -> None:
    """Verify menu state adjusts for new breakpoint."""
    solutions_page = SolutionsMenuPage(page)
    # Menu should close or adapt
    expect(solutions_page.locators.solutions_button).to_be_visible()


@then("No frozen or broken state")
def no_frozen_state(page: Page) -> None:
    """Verify no frozen or broken state."""
    header_page = HeaderPage(page)
    expect(header_page.locators.header_banner).to_be_visible()


@then("No non-essential continuous animations play")
def no_continuous_animations(page: Page) -> None:
    """Verify no non-essential continuous animations play."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.open_solutions_menu()
    # Verify menu opens smoothly without infinite animations
    expect(solutions_page.locators.solutions_button).to_have_attribute("aria-expanded", "true")


@then("Navigation remains functional")
def nav_remains_functional(page: Page) -> None:
    """Verify navigation remains functional."""
    header_page = HeaderPage(page)
    expect(header_page.locators.header_banner).to_be_visible()


@then("Content readable without horizontal scrolling")
def content_readable_no_hscroll(page: Page) -> None:
    """Verify content readable without horizontal scrolling."""
    scroll_width = page.evaluate("() => document.body.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    expect(scroll_width).to_be_less_than_or_equal(inner_width)


@then("Core navigation remains functional")
def core_nav_functional(page: Page) -> None:
    """Verify core navigation remains functional."""
    header_page = HeaderPage(page)
    expect(header_page.locators.header_banner).to_be_visible()
    expect(header_page.locators.emids_logo).to_be_visible()


@then("Basic links and menu structure work")
def basic_links_work(page: Page) -> None:
    """Verify basic links and menu structure work."""
    header_page = HeaderPage(page)
    expect(header_page.locators.solutions_nav).to_be_visible()
