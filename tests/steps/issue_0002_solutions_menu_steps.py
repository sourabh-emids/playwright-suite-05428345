"""Step definitions for issue_0002 - Solutions mega-menu functionality."""
from pytest_bdd import given, parsers, then, when

from pages.issue_0002_solutions_page import Issue0002SolutionsMenuPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0002SolutionsMenuPage):
    """Navigate to the homepage."""
    page.click_solutions_navigation()


@when("I click the Solutions navigation item")
def click_solutions_navigation(page: Issue0002SolutionsMenuPage):
    """Click the Solutions navigation item."""
    page.click_solutions_navigation()


@then("the Solutions mega-menu should appear")
def mega_menu_appears(page: Issue0002SolutionsMenuPage):
    """Verify mega-menu appears."""
    page.mega_menu_should_appear()


@then('the menu should display "Solutions by Initiative"')
def menu_displays_initiative_section(page: Issue0002SolutionsMenuPage):
    """Verify 'Solutions by Initiative' section is displayed."""
    page.menu_should_display_initiative_section()


@then(parsers.parse('the menu should display "{solution}" solution'))
def menu_displays_solution(page: Issue0002SolutionsMenuPage, solution: str):
    """Verify a solution is displayed in the menu."""
    page.menu_should_display_solution(solution)


@then('the menu should display "Browse By Industry" section')
def menu_displays_industry_section(page: Issue0002SolutionsMenuPage):
    """Verify 'Browse By Industry' section is displayed."""
    page.menu_should_display_industry_section()


@then(parsers.parse('the menu should display "{industry}" industry'))
def menu_displays_industry(page: Issue0002SolutionsMenuPage, industry: str):
    """Verify an industry is displayed in the menu."""
    page.menu_should_display_industry(industry)


@then('the menu should display "The Portfolio" section')
def menu_displays_portfolio_section(page: Issue0002SolutionsMenuPage):
    """Verify 'The Portfolio' section is displayed."""
    page.menu_should_display_portfolio_section()


@then("each solution link should be clickable")
def solution_links_clickable(page: Issue0002SolutionsMenuPage):
    """Verify solution links are clickable."""
    page.solution_links_should_be_clickable()


@then("each industry link should be clickable")
def industry_links_clickable(page: Issue0002SolutionsMenuPage):
    """Verify industry links are clickable."""
    page.industry_links_should_be_clickable()


@then('the "Explore all solutions" link should be present')
def explore_all_solutions_link_present(page: Issue0002SolutionsMenuPage):
    """Verify 'Explore all solutions' link is present."""
    page.explore_all_solutions_link_should_be_present()


@then("the mega-menu should close")
def mega_menu_closes(page: Issue0002SolutionsMenuPage):
    """Verify mega-menu closes."""
    page.mega_menu_should_close()


@when(parsers.parse('I click the "{solution}" solution link'))
def click_solution_link(page: Issue0002SolutionsMenuPage, solution: str):
    """Click a specific solution link."""
    if solution == "Modernization":
        page.click_modernization_solution()


@then("I should be navigated to the Modernization page")
def on_modernization_page(page: Issue0002SolutionsMenuPage):
    """Verify user is on the Modernization page."""
    page.should_be_on_modernization_page()
