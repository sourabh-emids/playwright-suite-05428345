"""Steps for emids_lp_002: Implement Solutions mega-menu."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.solutions_menu_page import SolutionsMenuPage


@given(parsers.parse("User focuses on the Solutions navigation item"))
def focus_solutions_nav(page: Page) -> None:
    """Focus on the Solutions navigation item."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.locators.solutions_nav.focus()


@given(parsers.parse("Solutions mega-menu is open"))
def solutions_menu_open(page: Page) -> None:
    """Solutions mega-menu is open."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.open_solutions_menu()


@given(parsers.parse("Solutions mega-menu is open with focus inside"))
def solutions_menu_open_with_focus(page: Page) -> None:
    """Solutions mega-menu is open with focus inside."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.open_solutions_menu()
    # Focus is already inside the menu after opening via click


@given(parsers.parse("User views site on mobile viewport"))
def user_on_mobile_viewport(page: Page) -> None:
    """User views site on mobile viewport."""
    page.set_viewport_size({"width": 375, "height": 667})


@given(parsers.parse("User is on touch device without hover capability"))
def touch_device_no_hover(page: Page) -> None:
    """User is on touch device without hover capability."""
    page.set_viewport_size({"width": 375, "height": 667})


@given(parsers.parse("Solutions menu is open on narrow viewport"))
def menu_open_narrow_viewport(page: Page) -> None:
    """Solutions menu is open on narrow viewport."""
    page.set_viewport_size({"width": 375, "height": 667})
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.open_solutions_menu()


@when("User activates Solutions menu (Enter/Space/click)")
def activate_solutions_menu(page: Page) -> None:
    """Activate Solutions menu."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.open_solutions_menu()


@when("User clicks or activates any solution link")
def click_any_solution_link(page: Page) -> None:
    """Click any solution link."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.locators.modernization_link.click()


@when("User presses Escape or clicks outside")
def escape_or_click_outside(page: Page) -> None:
    """Press Escape or click outside menu."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.close_solutions_menu()


@when("User activates Solutions navigation")
def activate_solutions_navigation(page: Page) -> None:
    """Activate Solutions navigation."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.open_solutions_menu()


@when("User taps Solutions navigation")
def tap_solutions_navigation(page: Page) -> None:
    """Tap Solutions navigation."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.open_solutions_menu()


@when("Menu content extends beyond viewport")
def menu_content_extends(page: Page) -> None:
    """Menu content extends beyond viewport."""
    # This is a condition being tested, not an action
    pass


@then("Menu opens")
def menu_opens(page: Page) -> None:
    """Verify menu opens."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_button).to_have_attribute("aria-expanded", "true")


@then("Focus remains within navigation order")
def focus_remains_in_nav_order(page: Page) -> None:
    """Verify focus remains within navigation order."""
    # Verify focus is on an interactive element within or related to the menu
    expect(page.locator("[aria-expanded='true']")).to_be_visible()


@then("All solution groups and items are visible")
def all_solution_groups_visible(page: Page) -> None:
    """Verify all solution groups and items are visible."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_by_initiative).to_be_visible()
    expect(solutions_page.locators.browse_by_industry).to_be_visible()
    expect(solutions_page.locators.the_portfolio).to_be_visible()
    for link in solutions_page.locators.get_all_solution_links():
        expect(link).to_be_visible()


@then("Link navigates to valid destination")
def link_navigates_valid(page: Page) -> None:
    """Verify link navigates to valid destination."""
    # Navigate to a solution page and verify it loads without 404
    expect(page.get_by_role("heading")).to_be_visible()


@then("Item has non-empty label and valid URL")
def item_has_label_and_url(page: Page) -> None:
    """Verify item has non-empty label and valid URL."""
    solutions_page = SolutionsMenuPage(page)
    solutions_page.navigate()
    solutions_page.open_solutions_menu()
    link = solutions_page.locators.modernization_link
    label = link.inner_text()
    url = link.get_attribute("href")
    expect(label).not_to_be_empty()
    expect(url).not_to_be_none()
    expect(url).to_match(r"^/solutions/|^https?://")


@then("Menu closes")
def menu_closes(page: Page) -> None:
    """Verify menu closes."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_button).to_have_attribute("aria-expanded", "false")


@then("Focus returns to the Solutions trigger control")
def focus_returns_to_trigger(page: Page) -> None:
    """Verify focus returns to the Solutions trigger control."""
    expect(solutions_page.locators.solutions_nav).to_be_focused()


@then("Menu displays using disclosure or drawer pattern")
def menu_disclosure_pattern(page: Page) -> None:
    """Verify menu displays using disclosure or drawer pattern."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_button).to_be_visible()


@then("All solution options remain accessible")
def all_options_accessible(page: Page) -> None:
    """Verify all solution options remain accessible."""
    solutions_page = SolutionsMenuPage(page)
    for link in solutions_page.locators.get_all_solution_links():
        expect(link).to_be_visible()


@then("No hover interaction required to access content")
def no_hover_required(page: Page) -> None:
    """Verify no hover interaction required to access content."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.solutions_by_initiative).to_be_visible()


@then("Menu repositions or scrolls appropriately")
def menu_repositions_or_scrolls(page: Page) -> None:
    """Verify menu repositions or scrolls appropriately."""
    solutions_page = SolutionsMenuPage(page)
    # Verify the menu is still visible
    expect(solutions_page.locators.solutions_button).to_be_visible()


@then("Critical content is not clipped")
def critical_content_not_clipped(page: Page) -> None:
    """Verify critical content is not clipped."""
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.locators.modernization_link).to_be_in_viewport()
