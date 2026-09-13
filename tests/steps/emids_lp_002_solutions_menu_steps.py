"""Step definitions for emids_lp_002 - Solutions mega-menu."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("The user hovers or focuses on the Solutions navigation item")
def hover_solutions_nav(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    solutions_page.hover_solutions_button()


@when("The user activates the Solutions control")
def activate_solutions_control(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    solutions_page.click_solutions_button()


@then("An accessible mega-menu opens displaying solution group headings, solution labels, and URLs")
def verify_mega_menu_opens(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    expect(solutions_page.mega_menu).to_be_visible()
    expect(solutions_page.solutions_heading).to_be_visible()
    expect(solutions_page.solution_links).to_have_count(10)


@then("All visible solution links are keyboard selectable and pointer-clickable")
def verify_solution_links_keyboard_and_pointer(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    links = solutions_page.solution_links
    for link in links:
        expect(link).to_be_visible()
        expect(link).to_be_enabled()


@then("Focus follows expected visual navigation order within the menu")
def verify_focus_order_in_menu(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    first_link = solutions_page.solution_links.first
    first_link.focus()
    expect(first_link).to_be_focused()


@then("Focus returns to the Solutions trigger control")
def verify_focus_returns_to_trigger(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    solutions_page.close_menu()
    expect(solutions_page.solutions_button).to_be_focused()


@then("An accessible disclosure or drawer pattern is used instead of mega-menu layout")
def verify_mobile_disclosure_pattern(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    solutions_page.click_solutions_button()
    expect(solutions_page.mobile_menu).to_be_visible()


@then("Menu is positioned to remain fully visible within the viewport")
def verify_menu_visible_in_viewport(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    page.set_viewport_size({"width": 768, "height": 600})
    solutions_page.click_solutions_button()
    menu_box = solutions_page.mega_menu.bounding_box()
    assert menu_box is not None
    assert menu_box["x"] >= 0
    assert menu_box["y"] >= 0


@then("Every item has a non-empty label and a valid internal or approved external URL")
def verify_solution_items_have_labels_and_urls(page: Page) -> None:
    from pages.emids_lp_002_solutions_page import SolutionsMenuPage
    solutions_page = SolutionsMenuPage(page)
    links = solutions_page.solution_links
    for link in links:
        text = link.text_content()
        assert text and text.strip(), "Link has no label"
        href = link.get_attribute("href")
        assert href, "Link has no href"
