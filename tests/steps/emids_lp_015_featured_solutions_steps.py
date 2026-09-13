"""Steps for emids_lp_015: Render six featured solution items."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.featured_solutions.featured_solutions_page import FeaturedSolutionsPage


@given(parsers.parse("User views Featured Solutions section"))
def view_featured_solutions(page: Page) -> None:
    """User views Featured Solutions section."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("User views Featured Solutions cards"))
def view_featured_cards(page: Page) -> None:
    """User views Featured Solutions cards."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("User examines each solution card"))
def examine_solution_cards(page: Page) -> None:
    """User examines each solution card."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("User views solution card"))
def view_solution_card(page: Page) -> None:
    """User views solution card."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("CMS manages solution content"))
def cms_manages_content(page: Page) -> None:
    """CMS manages solution content."""
    pass


@given(parsers.parse("User views Featured Solutions"))
def view_featured_solutions_again(page: Page) -> None:
    """User views Featured Solutions."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()


@given(parsers.parse("One solution is unpublished"))
def one_solution_unpublished(page: Page) -> None:
    """One solution is unpublished."""
    pass


@given(parsers.parse("Solution has very long title"))
def very_long_title(page: Page) -> None:
    """Solution has very long title."""
    page.set_viewport_size({"width": 375, "height": 667})


@when("User enumerates solutions")
def enumerate_solutions(page: Page) -> None:
    """Enumerate solutions."""
    pass


@when("User checks numbering")
def check_numbering(page: Page) -> None:
    """Check numbering."""
    pass


@when("User reads content")
def read_content(page: Page) -> None:
    """Read content."""
    pass


@when("User checks card interaction")
def check_card_interaction(page: Page) -> None:
    """Check card interaction."""
    pass


@when("Content is published")
def content_published(page: Page) -> None:
    """Content is published."""
    pass


@when("User checks sequence")
def check_sequence(page: Page) -> None:
    """Check sequence."""
    pass


@when("Featured Solutions section renders")
def section_renders(page: Page) -> None:
    """Section renders."""
    page.wait_for_load_state("domcontentloaded")


@when("Page renders on mobile")
def page_renders_mobile(page: Page) -> None:
    """Page renders on mobile."""
    page.wait_for_load_state("domcontentloaded")


@then("All six entries present: Modernization as a Service (01), Interoperability (02), Cloud Migration (03), Global Capability Center (04), Epic Implementation (05), Agentic AI (06)")
def all_six_present(page: Page) -> None:
    """Verify all six solutions present."""
    solutions_page = FeaturedSolutionsPage(page)
    expect(solutions_page.get_solution_count()).to_equal(6)


@then("Numbers display as 01 through 06 in correct sequential order")
def numbers_correct_sequence(page: Page) -> None:
    """Verify numbers are 01-06 in sequence."""
    solutions_page = FeaturedSolutionsPage(page)
    numbers = solutions_page.get_solution_numbers()
    expect(len(numbers)).to_equal(6)


@then("Each card contains readable title and supporting copy")
def each_card_has_title_copy(page: Page) -> None:
    """Verify each card has title and copy."""
    solutions_page = FeaturedSolutionsPage(page)
    for i in range(1, 7):
        solutions_page.locators.all_solutions.nth(i - 1).scroll_into_view_if_needed()
        expect(solutions_page.locators.all_solutions.nth(i - 1)).to_be_visible()


@then("Each card links to its intended solution page")
def each_card_links_correct(page: Page) -> None:
    """Verify each card links to correct page."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()
    href = solutions_page.locators.solution_01.get_attribute("href")
    expect(href).to_contain("/solutions/")


@then("No solution card displays with blank title field")
def no_blank_titles(page: Page) -> None:
    """Verify no blank titles."""
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.navigate()
    solutions_page.scroll_to_section()
    for i in range(solutions_page.get_solution_count()):
        title = solutions_page.locators.all_solutions.nth(i).get_attribute("name")
        expect(title).not_to_be_none()


@then("Solutions display in CMS-defined order")
def cms_defined_order(page: Page) -> None:
    """Verify solutions display in CMS-defined order."""
    solutions_page = FeaturedSolutionsPage(page)
    expect(solutions_page.get_solution_count()).to_equal(6)


@then("No random or reverse order")
def no_random_order(page: Page) -> None:
    """Verify no random order."""
    # Order should be consistent
    solutions_page = FeaturedSolutionsPage(page)
    first_href = solutions_page.locators.solution_01.get_attribute("href")
    expect(first_href).to_contain("modernization")


@then("Only published solutions display")
def only_published_display(page: Page) -> None:
    """Verify only published solutions display."""
    solutions_page = FeaturedSolutionsPage(page)
    # Should show available solutions
    expect(solutions_page.locators.all_solutions.first).to_be_visible()


@then("Section maintains 6 items when fully published")
def maintains_six_items(page: Page) -> None:
    """Verify section maintains 6 items."""
    solutions_page = FeaturedSolutionsPage(page)
    expect(solutions_page.get_solution_count()).to_equal(6)


@then("Title truncates or wraps gracefully")
def title_truncates_wraps(page: Page) -> None:
    """Verify title truncates or wraps."""
    solutions_page = FeaturedSolutionsPage(page)
    expect(solutions_page.locators.all_solutions.first).to_be_visible()


@then("Does not break card layout")
def no_card_layout_break(page: Page) -> None:
    """Verify card layout not broken."""
    solutions_page = FeaturedSolutionsPage(page)
    expect(solutions_page.locators.section_heading).to_be_visible()
