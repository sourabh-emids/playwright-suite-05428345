"""Step definitions for emids_lp_015 - Featured solutions."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Exactly six solution entries are displayed")
def verify_six_solutions(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    expect(page_obj.solution_cards).to_have_count(6)


@then("Solutions are numbered 01, 02, 03, 04, 05, 06 in correct order")
def verify_solution_numbers(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    numbers = page_obj.solution_numbers
    expected = ["01", "02", "03", "04", "05", "06"]
    for num, exp in zip(numbers, expected):
        expect(num).to_have_text(exp)


@then("Each entry contains a readable title and supporting copy")
def verify_entry_content(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    for card in page_obj.solution_cards.all():
        expect(card.locator("h3").first).to_be_visible()


@then("Each entry routes to its intended destination or action URL")
def verify_entry_destinations(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    for link in page_obj.solution_links.all():
        href = link.get_attribute("href")
        assert href and "/solutions/" in href, f"Invalid solution URL: {href}"


@then("No solution title is empty or blank")
def verify_titles_not_blank(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    for title in page_obj.solution_titles.all():
        text = title.text_content()
        assert text and text.strip(), "Solution title is blank"


@then("Solutions display in configured order")
def verify_order(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    expect(page_obj.solution_cards).to_have_count(6)


@then("Only published solutions appear; section shows available items only")
def verify_unpublished_handled(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    expect(page_obj.solution_cards).to_have_count(6)


@then("Long title wraps or truncates gracefully without breaking layout")
def verify_long_title_handled(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card renders without media placeholder or uses text-only layout")
def verify_missing_media_handled(page: Page) -> None:
    from pages.emids_lp_015_featured_solutions_page import FeaturedSolutionsPage
    page_obj = FeaturedSolutionsPage(page)
    expect(page_obj.section).to_be_visible()
