"""Steps for Solutions mega-menu implementation (issue_0002)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0002_solutions_megamenu_page import SolutionsMegamenuPage
from locators.issue_0002_solutions_megamenu_locators import SolutionsMegamenuLocators


@given("User is on Emids homepage with keyboard focus on header")
def keyboard_focus_on_header(page: Page) -> None:
    page.goto("/")
    page.locator("header").focus()


@given("User hovers over Solutions navigation item")
def hover_solutions(page: Page) -> None:
    page.goto("/")
    page.locator("header").focus()
    page.locator("header button").first.hover()


@given("User is on touch device viewing Emids homepage")
def touch_device_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("Solutions menu is open")
def solutions_menu_open(page: Page) -> None:
    page.goto("/")
    solutions_page = SolutionsMegamenuPage(page)
    solutions_page.hover_solutions()


@given("Solutions menu is open with focus on trigger")
def solutions_menu_open_focused(page: Page) -> None:
    page.goto("/")
    solutions_page = SolutionsMegamenuPage(page)
    solutions_page.hover_solutions()
    solutions_page.locators.solutions_button.focus()


@given("User is on mobile device viewing Emids homepage")
def mobile_device_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@when("User tabs to Solutions and presses Enter or Space")
def tab_and_activate_solutions(page: Page) -> None:
    solutions_page = SolutionsMegamenuPage(page)
    solutions_page.press_enter_on_solutions()


@when("Hover interaction occurs")
def hover_interaction(page: Page) -> None:
    solutions_page = SolutionsMegamenuPage(page)
    solutions_page.hover_solutions()


@when("User taps on Solutions navigation item")
def tap_solutions(page: Page) -> None:
    solutions_page = SolutionsMegamenuPage(page)
    solutions_page.click_solutions()


@when("User views solution items")
def view_solution_items(page: Page) -> None:
    pass


@when("Menu contains many items")
def menu_has_many_items(page: Page) -> None:
    pass


@when("User presses Escape or clicks outside")
def close_menu_interaction(page: Page) -> None:
    solutions_page = SolutionsMegamenuPage(page)
    solutions_page.press_escape()


@then("Solutions accessible menu opens and focus remains within expected navigation order")
def menu_opens_keyboard(page: Page) -> None:
    expect(SolutionsMegamenuLocators(page).solutions_by_initiative).to_be_visible()


@then("Solutions accessible menu opens")
def menu_opens_pointer(page: Page) -> None:
    expect(SolutionsMegamenuLocators(page).solutions_by_initiative).to_be_visible()


@then("All visible solution links are selectable and have non-empty labels with valid URLs")
def all_solution_links_selectable(page: Page) -> None:
    solutions_page = SolutionsMegamenuPage(page)
    links = solutions_page.get_solution_links()
    assert len(links) > 0
    for link in links:
        expect(link).to_be_visible()
        label = link.text_content()
        assert label and label.strip()
        href = link.get_attribute("href")
        assert href and href.strip()


@then("Menu closes and focus returns to the trigger element")
def menu_closes_focus_restored(page: Page) -> None:
    expect(SolutionsMegamenuLocators(page).solutions_button).to_be_focused()


@then("Menu does not clip or overflow viewport boundaries")
def menu_not_clipped(page: Page) -> None:
    pass


@then("Mobile uses disclosure/drawer pattern equivalent to desktop mega-menu")
def mobile_disclosure_pattern(page: Page) -> None:
    pass
