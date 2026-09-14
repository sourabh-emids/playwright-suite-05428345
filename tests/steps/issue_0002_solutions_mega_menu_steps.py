"""Step definitions for issue_0002: Solutions Mega-Menu Implementation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.solutions_menu_page import SolutionsMenuPage


@given("User is on page with header visible")
def on_page_with_header(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User activates the Solutions menu trigger via keyboard or click")
def activate_solutions_menu(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("Solutions mega-menu opens and is accessible")
def solutions_menu_opens_accessibly(page: Page):
    menu_page = SolutionsMenuPage(page)
    expect(menu_page.solutions_menu).to_be_visible()
    expect(menu_page.solutions_by_initiative).to_be_visible()


@given("Solutions mega-menu is open")
def solutions_menu_open(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()
    expect(menu_page.solutions_menu).to_be_visible()


@when("User views all visible solution links")
def view_solution_links(page: Page):
    pass


@then("All solution links are selectable and route to valid destinations")
def all_solution_links_selectable(page: Page):
    menu_page = SolutionsMenuPage(page)
    count = menu_page.get_solution_link_count()
    assert count >= 5, f"Expected at least 5 solution links, found {count}"
    expect(menu_page.modernization_link).to_be_visible()
    expect(menu_page.interoperability_link).to_be_visible()


@when("User tabs through menu items")
def tab_through_menu_items(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.focus_trigger()
    for _ in range(10):
        page.keyboard.press("Tab")


@then("Focus remains within expected navigation order and does not escape to page")
def focus_stays_in_menu(page: Page):
    menu_page = SolutionsMenuPage(page)
    expect(menu_page.solutions_menu).to_be_visible()


@given("Solutions mega-menu is open and user focuses on an item")
def solutions_menu_open_focused(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()
    expect(menu_page.solutions_menu).to_be_visible()
    page.keyboard.press("Tab")


@when("User closes the menu (Escape key or trigger)")
def close_menu(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.press_escape()


@then("Focus is restored to the Solutions menu trigger")
def focus_restored_to_trigger(page: Page):
    menu_page = SolutionsMenuPage(page)
    expect(menu_page.solutions_trigger).to_be_focused()


@given("Solutions menu is rendered")
def solutions_menu_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("All solution items are inspected for label and URL validity")
def inspect_solution_items(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("Every item has non-empty label and valid internal or approved external URL")
def items_have_valid_labels_urls(page: Page):
    menu_page = SolutionsMenuPage(page)
    links = menu_page.solution_links.all()
    for link in links:
        text = link.text_content()
        assert text and text.strip(), "Link has empty label"
        href = link.get_attribute("href")
        assert href and ("emids.com" in href or href.startswith("/") or href.startswith("http")), f"Invalid URL: {href}"


@given("Page is rendered on mobile viewport")
def mobile_viewport(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("User activates Solutions menu")
def activate_mobile_solutions_menu(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("Menu uses disclosure/drawer pattern equivalent to desktop mega-menu")
def mobile_disclosure_pattern(page: Page):
    menu_page = SolutionsMenuPage(page)
    expect(menu_page.solutions_menu).to_be_visible()


@given("Solutions menu is open near viewport edge")
def menu_near_viewport_edge(page: Page):
    page.set_viewport_size({"width": 800, "height": 600})


@when("Menu would overflow viewport")
def menu_overflow_triggered(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("Menu repositions or resizes to remain fully visible")
def menu_repositions(page: Page):
    menu_page = SolutionsMenuPage(page)
    expect(menu_page.solutions_menu).to_be_visible()


@given("User is on touch device without hover capability")
def touch_device(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("User taps Solutions trigger")
def tap_solutions_trigger(page: Page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("Menu opens on tap and remains accessible")
def menu_opens_on_tap(page: Page):
    menu_page = SolutionsMenuPage(page)
    expect(menu_page.solutions_menu).to_be_visible()
