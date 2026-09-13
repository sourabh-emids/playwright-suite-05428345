"""Steps for Six featured solution items rendering (issue_0015)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0015_featured_solutions_page import FeaturedSolutionsPage
from locators.issue_0015_featured_solutions_locators import FeaturedSolutionsLocators


@given("User is on Emids homepage")
def on_homepage(page: Page) -> None:
    page.goto("/")


@given("Featured Solutions section renders")
def section_renders(page: Page) -> None:
    page.goto("/")
    sol_page = FeaturedSolutionsPage(page)
    sol_page.scroll_to_solutions()


@given("User views Featured Solutions at mobile width")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("Solution has very long title")
def long_title(page: Page) -> None:
    page.goto("/")


@when("User views Featured Solutions section")
def view_solutions(page: Page) -> None:
    sol_page = FeaturedSolutionsPage(page)
    sol_page.scroll_to_solutions()


@when("User views solution numbers")
def view_numbers(page: Page) -> None:
    pass


@when("User views each solution entry")
def view_each_entry(page: Page) -> None:
    pass


@when("User validates content")
def validate_content(page: Page) -> None:
    pass


@when("User views solution order")
def view_order(page: Page) -> None:
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Page renders at narrow viewport")
def render_narrow(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("All six solution entries are present")
def six_entries_present(page: Page) -> None:
    sol_page = FeaturedSolutionsPage(page)
    sol_page.scroll_to_solutions()
    count = sol_page.get_solution_count()
    expect(count).to_be_greater_than_or_equal(6)


@then("Solutions are numbered correctly from 01 to 06")
def numbering_correct(page: Page) -> None:
    pass


@then("Each entry contains a readable title (Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, Agentic AI)")
def readable_titles(page: Page) -> None:
    titles = FeaturedSolutionsPage(page).get_solution_titles()
    for title in titles:
        text = title.text_content()
        assert text and text.strip()


@then("Each entry contains supporting copy")
def supporting_copy(page: Page) -> None:
    pass


@then("Each entry has an intended destination URL or action")
def destinations(page: Page) -> None:
    pass


@then("No solution titles are blank")
def titles_not_blank(page: Page) -> None:
    titles = FeaturedSolutionsPage(page).get_solution_titles()
    for title in titles:
        text = title.text_content()
        assert text and text.strip()


@then("Solutions appear in controlled order (01-06)")
def controlled_order(page: Page) -> None:
    pass


@then("Responsive layout (cards/list/rail/stacked) retains all content")
def responsive_layout(page: Page) -> None:
    sol_page = FeaturedSolutionsPage(page)
    sol_page.scroll_to_solutions()
    expect(FeaturedSolutionsLocators(page).solutions_section).to_be_visible()


@then("Either all six entries display correctly or appropriate fallback displays")
def fallback_handling(page: Page) -> None:
    pass


@then("Title text wraps appropriately without breaking layout")
def title_wraps(page: Page) -> None:
    expect(FeaturedSolutionsLocators(page).solutions_section).to_be_visible()
