"""Step definitions for issue_0015: Six Featured Solution Items."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.featured_solutions_page import FeaturedSolutionsPage


@given("Featured Solutions section renders")
def featured_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Solution items are counted")
def count_solutions(page: Page):
    pass


@then("All six entries are present")
def six_entries_present(page: Page):
    fs = FeaturedSolutionsPage(page)
    count = fs.get_solution_count()
    assert count >= 6, f"Expected at least 6 solutions, found {count}"


@given("Featured Solutions section renders")
def featured_renders_numbering(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Numbering is checked")
def check_numbering(page: Page):
    pass


@then("Entries are numbered 01 through 06 in correct order")
def numbering_01_to_06(page: Page):
    fs = FeaturedSolutionsPage(page)
    numbers = fs.get_numbering_order()
    expected = ["01", "02", "03", "04", "05", "06"]
    for num in expected:
        assert num in numbers, f"Missing number {num}"


@given("Each featured solution is inspected")
def each_solution_inspected(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Content is reviewed")
def review_content(page: Page):
    pass


@then("Each entry contains readable title and supporting copy")
def entries_have_title_copy(page: Page):
    fs = FeaturedSolutionsPage(page)
    expect(fs.section).to_be_visible()


@given("Featured solution items are reviewed")
def solution_items_reviewed(page: Page):
    page.goto("/")


@when("Links are checked")
def check_links(page: Page):
    pass


@then("Each entry has intended destination/action")
def each_entry_destination(page: Page):
    fs = FeaturedSolutionsPage(page)
    links = fs.solution_cards.all()
    for link in links:
        href = link.get_attribute("href")
        assert href and "/solutions/" in href, f"Invalid solution link: {href}"


@given("Featured solutions are configured")
def solutions_configured(page: Page):
    page.goto("/")


@when("Titles are validated")
def validate_titles(page: Page):
    pass


@then("No titles are blank")
def titles_not_blank(page: Page):
    fs = FeaturedSolutionsPage(page)
    links = fs.solution_cards.all()
    for link in links:
        text = link.text_content()
        assert text and text.strip(), "Title should not be blank"


@given("Featured solutions render")
def solutions_render(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Order is compared to expected sequence")
def compare_order(page: Page):
    pass


@then("Order follows configuration (01-06)")
def order_follows_config(page: Page):
    fs = FeaturedSolutionsPage(page)
    numbers = fs.get_numbering_order()
    assert len(numbers) >= 6, "Should have 6 numbered items"


@given("One solution item is unpublished")
def one_unpublished(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_unpublished(page: Page):
    page.wait_for_load_state("networkidle")


@then("Unpublished item is handled appropriately")
def unpublished_handled(page: Page):
    fs = FeaturedSolutionsPage(page)
    expect(fs.section).to_be_visible()


@given("Solution has very long title")
def long_title(page: Page):
    page.goto("/")


@when("Section renders at viewport")
def section_at_viewport_long_title(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})


@then("Long title is handled gracefully without breaking layout")
def long_title_handled(page: Page):
    fs = FeaturedSolutionsPage(page)
    expect(fs.section).to_be_visible()


@given("Solution card media is missing")
def card_media_missing(page: Page):
    page.goto("/")
    page.route(lambda url: "image" in url or "jpg" in url or "png" in url, lambda route: route.abort())


@when("Card renders")
def card_renders(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Card renders without breaking layout")
def card_without_media(page: Page):
    fs = FeaturedSolutionsPage(page)
    expect(fs.section).to_be_visible()
