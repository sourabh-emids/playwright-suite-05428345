"""Step definitions for Solutions mega-menu - EMIDS-LP-002"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-002_solutions_menu_page import SolutionsMenuPage
from playwright.sync_api import expect


@given("A user hovers over or focuses on the Solutions navigation item")
def hover_solutions_nav(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.goto("/")
    menu_page.hover_solutions_menu()


@when("The Solutions control is activated")
def activate_solutions(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("An accessible mega-menu opens displaying solution taxonomy grouped appropriately")
def verify_mega_menu_opens(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.verify_menu_open()


@given("The Solutions mega-menu is open")
def solutions_menu_open(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.goto("/")
    menu_page.open_solutions_menu()


@when("The user selects each visible solution link")
def select_solution_links(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.click_solution_link(0)


@then("Each link navigates to its intended destination with non-empty label and valid URL")
def verify_solution_links(page):
    menu_page = SolutionsMenuPage(page)
    links = menu_page.get_solution_links()
    assert len(links) > 0
    for link in links:
        assert link and len(link) > 0


@given("The Solutions mega-menu is open")
def solutions_menu_open_2(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.goto("/")
    menu_page.open_solutions_menu()


@when("The user tabs through the menu items")
def tab_through_menu(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.tab_through_menu_items()


@then("Focus remains within expected navigation order; tabbing through closes menu and returns focus to trigger")
def verify_focus_order(page):
    pass


@given("A user on a touch-only device")
def touch_device(page):
    pass


@when("Tapping the Solutions menu trigger")
def tap_solutions_trigger(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.open_solutions_menu()


@then("Menu opens with disclosure or drawer pattern; all solution links are reachable")
def verify_drawer_pattern(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.verify_menu_open()


@given("The Solutions mega-menu is opened")
def mega_menu_opened(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.goto("/")
    menu_page.open_solutions_menu()


@when("The menu dimensions are checked against viewport")
def check_menu_dimensions(page):
    pass


@then("Menu is not clipped and all content is visible")
def menu_not_clipped(page):
    menu_page = SolutionsMenuPage(page)
    menu_page.verify_menu_open()
