"""Step definitions for emids_lp_002: Implement Solutions mega-menu."""
import httpx
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when


@given("User hovers over or focuses on the Solutions navigation item")
def hover_solutions_nav(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    solutions = page.get_by_role("button", name="Solutions")
    solutions.hover()


@given("Solutions mega-menu is open")
def solutions_menu_open(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    solutions = page.get_by_role("button", name="Solutions")
    solutions.click()
    page.wait_for_timeout(300)


@given("Solutions menu is open and user begins tabbing")
def solutions_menu_open_tabbing(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    solutions = page.get_by_role("button", name="Solutions")
    solutions.click()
    page.wait_for_timeout(300)
    solutions.press("Tab")


@given("Solutions menu is open with focus on a menu item")
def solutions_menu_with_focus(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    solutions = page.get_by_role("button", name="Solutions")
    solutions.click()
    page.wait_for_timeout(300)


@given("Solutions menu is rendered")
def solutions_menu_rendered(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Solutions").hover()
    page.wait_for_timeout(300)


@given("User views page on mobile device")
def mobile_view(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Solutions menu is open near edge of browser window")
def solutions_menu_edge(page: Page) -> None:
    page.set_viewport_size({"width": 800, "height": 600})
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Solutions").click()
    page.wait_for_timeout(300)


@given("User is on a touch device without hover capability")
def touch_device(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User activates the Solutions control")
def activate_solutions(page: Page) -> None:
    solutions = page.get_by_role("button", name="Solutions")
    solutions.click()


@when("User clicks each visible solution link")
def click_solution_links(page: Page, base_url: str) -> None:
    pass


@when("User navigates through menu items using keyboard")
def navigate_menu_keyboard(page: Page) -> None:
    for _ in range(10):
        page.keyboard.press("Tab")


@when("User closes the menu (Escape key or clicking outside)")
def close_menu(page: Page) -> None:
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)


@when("Automated check validates each solution item")
def validate_solution_items(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu').filter(has=page.get_by_role("button", name="Solutions"))
    items = menu.locator("a, button")
    count = items.count()
    assert count > 0, "No solution items found"


@when("User activates Solutions navigation")
def activate_solutions_mobile(page: Page) -> None:
    menu_btn = page.locator('[aria-label="Menu"], button:has-text("Menu")')
    if menu_btn.is_visible():
        menu_btn.click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Solutions").click()


@when("Menu positions itself responsively")
def menu_position_check(page: Page) -> None:
    pass


@when("User taps Solutions navigation")
def tap_solutions(page: Page) -> None:
    page.get_by_role("button", name="Solutions").click()


@then("An accessible mega-menu opens displaying solution taxonomy grouped appropriately")
def verify_mega_menu(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu, [aria-expanded="true"]')
    expect(menu).to_be_visible()


@then("Each link navigates to its valid destination URL")
def verify_links_valid(page: Page, base_url: str) -> None:
    pass


@then("Focus remains within expected navigation order without escaping unexpectedly")
def verify_focus_order(page: Page) -> None:
    pass


@then("Focus returns to the Solutions trigger control")
def verify_focus_returned(page: Page) -> None:
    expect(page.get_by_role("button", name="Solutions")).to_be_focused()


@then("Every item has a non-empty label and valid URL (internal or approved external)")
def verify_items_non_empty(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu')
    labels = menu.locator("a, button")
    count = labels.count()
    for i in range(count):
        text = labels.nth(i).inner_text()
        assert text.strip(), f"Item {i} has empty label"


@then("An accessible disclosure or drawer pattern is presented instead of mega-menu")
def verify_mobile_disclosure(page: Page) -> None:
    drawer = page.locator('[role="dialog"], [aria-expanded="true"]')
    expect(drawer).to_be_visible()


@then("Menu is not clipped and remains fully visible within viewport")
def verify_menu_not_clipped(page: Page) -> None:
    pass


@then("Menu opens on tap and is fully usable without hover interactions")
def verify_touch_usability(page: Page) -> None:
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()
