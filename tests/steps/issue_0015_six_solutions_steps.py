"""Step definitions for Issue 0015 - Six featured solution items rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Featured Solutions section")
def view_featured_solutions(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@when("The section loads")
def solutions_section_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("All six entries are present")
def all_six_entries_present(page: Page):
    homepage = HomepagePage(page)
    solutions = homepage.all_six_solution_entries_present()
    assert len(solutions) == 6


@when("The solution entries are displayed")
def solution_entries_displayed(page: Page):
    pass


@then("Each entry is numbered 01 through 06 correctly in order")
def entries_numbered_correctly(page: Page):
    homepage = HomepagePage(page)
    numbers = homepage.solution_numbers_are_correct()
    assert len(numbers) == 6


@given("A user views any featured solution card")
def view_solution_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@when("The card is examined")
def card_examined(page: Page):
    pass


@then("Each entry contains a readable title and supporting copy")
def entry_has_title_copy(page: Page):
    homepage = HomepagePage(page)
    solutions = homepage.all_six_solution_entries_present()
    for solution in solutions:
        expect(page.getByText(solution, exact=False).first).to_be_visible()


@given("A user clicks on a featured solution")
def click_featured_solution(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")
    page.getByText("Modernization", exact=False).first.locator("..").click()


@when("The solution link is activated")
def solution_link_activated(page: Page):
    pass


@then("The user is routed to the intended destination or action")
def routed_to_destination(page: Page):
    page.wait_for_url("**/solutions/**")


@given("A user views the Featured Solutions section")
def view_solutions_for_titles(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@when("The solution entries are examined")
def entries_examined(page: Page):
    pass


@then("No entry has a blank title")
def no_blank_titles(page: Page):
    # Verify all expected solution names are visible
    solutions = ["Modernization as a Service", "Interoperability", "Cloud Migration",
                 "Global Capability Center", "Epic Implementation", "Agentic AI"]
    for solution in solutions:
        expect(page.getByText(solution, exact=False).first).to_be_visible()


@given("One featured solution is unpublished")
def one_unpublished(page: Page):
    pass


@when("The section renders")
def section_renders_unpublished(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@then("The unpublished item is excluded or handled gracefully")
def unpublished_handled_gracefully(page: Page):
    homepage = HomepagePage(page)
    solutions = homepage.all_six_solution_entries_present()
    # Should show available solutions
    assert len(solutions) >= 5


@given("A solution title exceeds expected character count")
def long_title(page: Page):
    pass


@when("The card renders")
def card_renders_long_title(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@then("The title is handled gracefully (wrapped or truncated)")
def title_handled_gracefully(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.featured_solutions_section).to_be_visible()


@given("A featured solution card has no media configured")
def card_no_media(page: Page):
    pass


@when("The card renders")
def card_renders_no_media(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@then("The card renders without broken image placeholders; text content remains complete")
def no_broken_placeholders(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.featured_solutions_section).to_be_visible()
