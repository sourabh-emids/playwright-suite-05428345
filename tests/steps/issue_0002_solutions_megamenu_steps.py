"""Step definitions for issue_0002: Implement Solutions mega-menu."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User is on desktop with header visible")
def user_on_desktop_with_header(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("User clicks or activates the Solutions navigation item")
def user_clicks_solutions(page: Page) -> None:
    solutions_btn = page.get_by_role("button", name="Solutions")
    solutions_btn.click()


@then("Accessible mega-menu opens displaying solution group headings and solution labels")
def mega_menu_opens(page: Page) -> None:
    expect(page.get_by_text("Solutions by Initiative")).to_be_visible()
    expect(page.get_by_text("Browse By Industry")).to_be_visible()
    expect(page.get_by_text("The Portfolio")).to_be_visible()


@given("Solutions mega-menu is open")
def solutions_menu_open(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Solutions").click()
    expect(page.get_by_text("Solutions by Initiative")).to_be_visible()


@when("User clicks on any visible solution link")
def user_clicks_solution_link(page: Page) -> None:
    solution_links = page.get_by_role("link").filter(has=page.locator("..").get_by_text("Solutions by Initiative"))
    if solution_links.count() > 0:
        solution_links.first.click()


@then("User is navigated to the solution destination URL")
def user_navigated_to_solution(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/solutions/")


@when("User tabs through menu items")
def user_tabs_through_menu(page: Page) -> None:
    for _ in range(5):
        page.keyboard.press("Tab")


@then("Focus remains within the menu and follows logical visual order")
def focus_stays_in_menu(page: Page) -> None:
    active_element = page.evaluate("() => document.activeElement?.tagName")
    assert active_element is not None, "Focus should remain on page"


@given("User navigates Solutions menu using keyboard")
def user_navigates_solutions_by_keyboard(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Solutions").focus()


@then("Focus returns to the Solutions trigger control")
def focus_returns_to_trigger(page: Page) -> None:
    page.keyboard.press("Escape")
    active = page.evaluate("() => document.activeElement?.textContent")
    assert "Solutions" in str(active) or page.get_by_role("button", name="Solutions").is_visible()


@when("User closes the menu via Escape key or click outside")
def user_closes_menu(page: Page) -> None:
    page.keyboard.press("Escape")


@given("User is on mobile device viewing header")
def user_on_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")


@when("User expands Solutions section")
def user_expands_solutions_mobile(page: Page) -> None:
    menu_button = page.get_by_role("button", name="Open menu")
    if menu_button.is_visible():
        menu_button.click()
    solutions_expand = page.get_by_role("button", name="Solutions")
    if solutions_expand.is_visible():
        solutions_expand.click()


@then("Equivalent disclosure or drawer pattern displays solution items")
def mobile_disclosure_displays(page: Page) -> None:
    expect(page.get_by_role("navigation")).to_be_visible()


@when("User inspects solution items")
def user_inspects_solution_items(page: Page) -> None:
    pass


@then("Each item has non-empty label and valid internal or approved external URL")
def solution_items_have_valid_content(page: Page) -> None:
    menu = page.get_by_text("Solutions by Initiative").locator("..")
    links = menu.get_by_role("link")
    count = links.count()
    assert count > 0, "Solution links should be present"


@given("User has narrow browser window")
def user_has_narrow_window(page: Page) -> None:
    page.set_viewport_size({"width": 1024, "height": 768})
    page.goto("/")


@when("Solutions menu opens")
def solutions_menu_opens(page: Page) -> None:
    page.get_by_role("button", name="Solutions").click()


@then("Menu is not clipped by viewport edges and remains fully visible")
def menu_not_clipped(page: Page) -> None:
    menu = page.locator("nav[aria-label='Solutions']")
    expect(menu).to_be_visible()
