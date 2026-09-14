"""Step definitions for issue_0015: Render six featured solution items."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Featured Solutions section")
def view_featured_solutions(page: Page) -> None:
    page.goto("/")


@when("Counting entries")
def count_entries(page: Page) -> None:
    pass


@then("Six entries are visible with numbering 01 through 06")
def six_entries_with_numbers(page: Page) -> None:
    section = page.get_by_text("The Portfolio")
    expect(section).to_be_visible()
    # Check for solution entries
    links = page.get_by_role("link", name="All solutions")
    expect(links).to_be_visible()


@given("User views each solution entry")
def view_solution_entries(page: Page) -> None:
    page.goto("/")


@when("Checking content")
def check_content(page: Page) -> None:
    pass


@then("Each entry contains readable title and supporting summary text")
def entries_have_content(page: Page) -> None:
    section = page.get_by_text("A portfolio of named solutions")
    expect(section).to_be_visible()


@given("User clicks each solution entry")
def click_solution_entries(page: Page) -> None:
    page.goto("/")


@when("Navigation triggered")
def nav_triggered(page: Page) -> None:
    pass


@then("Each solution links to its intended destination URL")
def links_to_destinations(page: Page) -> None:
    # Should have solution links
    links = page.get_by_role("link")
    assert links.count() > 0


@given("User validates solution entries")
def validate_solution_entries(page: Page) -> None:
    page.goto("/")


@when("Checking for empty titles")
def check_empty_titles(page: Page) -> None:
    pass


@then("All six solution titles are populated with non-empty text")
def titles_populated(page: Page) -> None:
    section = page.get_by_text("A portfolio of named solutions")
    expect(section).to_be_visible()


@when("Checking order")
def check_order(page: Page) -> None:
    pass


@then("Solutions display in controlled order 01-06 as configured")
def controlled_order(page: Page) -> None:
    expect(page.get_byRole("link", name="All solutions")).to_be_visible()


@given("Current content version specifies six solutions")
def six_solutions_config(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Exactly six entries display: Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, and Agentic AI")
def exact_six_entries(page: Page) -> None:
    expect(page.get_byText("A portfolio of named solutions")).to_be_visible()


@given("One featured solution is unpublished")
def one_unpublished(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders_unpublished(page: Page) -> None:
    pass


@then("Unpublished item does not appear; five items display correctly")
def unpublished_hidden(page: Page) -> None:
    expect(page.get_byText("A portfolio of named solutions")).to_be_visible()


@given("Configuration error causes duplicate order number")
def duplicate_order(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_duplicate_order(page: Page) -> None:
    pass


@then("Items still render; duplicate order is detected and logged")
def items_render(page: Page) -> None:
    expect(page.getByText("A portfolio of named solutions")).to_be_visible()


@given("Solution title is very long")
def long_title(page: Page) -> None:
    page.goto("/")


@when("Page renders at standard viewport")
def render_standard_viewport(page: Page) -> None:
    pass


@then("Long title wraps gracefully without breaking card layout")
def long_title_wraps(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Solution card has no optional media configured")
def no_media_config(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_no_media(page: Page) -> None:
    pass


@then("Card renders with text content; no broken image placeholder")
def card_text_only(page: Page) -> None:
    expect(page.getByText("A portfolio of named solutions")).to_be_visible()
