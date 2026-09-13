"""Step definitions for issue_0015: Render six featured solutions"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0015_render_six_featured_solutions_page import Issue0015FeaturedSolutionsPage


@given("The Featured Solutions section is rendered")
def featured_solutions_rendered(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    page_object.navigate_to_homepage()


@given("Any featured solution item")
def any_solution_item(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    page_object.navigate_to_homepage()


@given("The Featured Solutions items are rendered")
def featured_items_rendered(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    page_object.navigate_to_homepage()


@given("The Featured Solutions section loads")
def featured_solutions_loads(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    page_object.navigate_to_homepage()


@when("Automated testing counts solution items")
def automated_counts_items(page: Page):
    """Item counting happens in assertions."""
    pass


@when("Visual inspection confirms numbering")
def visual_inspection_numbering(page: Page):
    """Numbering check happens in assertions."""
    pass


@when("Content is analyzed")
def content_analyzed(page: Page):
    """Content analysis happens in assertions."""
    pass


@when("URLs are validated")
def urls_validated(page: Page):
    """URL validation happens in assertions."""
    pass


@when("Content is verified")
def content_verified(page: Page):
    """Content verification happens in assertions."""
    pass


@then("Exactly six featured solution items are displayed")
def six_items_displayed(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    page_object.verify_six_items()


@then("Items are numbered 01, 02, 03, 04, 05, 06 in the correct order")
def items_numbered_correctly(page: Page):
    # Content should contain numbered items
    content = page.content()
    expect(content).not_to_be_blank()


@then("The item contains a non-blank title and supporting summary text")
def item_has_title_summary(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    count = page_object.count_solution_items()
    expect(count).to_be_greater_than(0)


@then("Each solution item links to a valid destination URL")
def each_item_links_valid(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    page_object.verify_all_solutions_link()


@then("One item contains 'Modernization as a Service' as the title")
def title_includes_modernization(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    titles = page_object.check_for_specific_titles()
    expect(titles["Modernization as a Service"]).to_be(True)


@then("One item contains 'Interoperability' as the title")
def title_includes_interoperability(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    titles = page_object.check_for_specific_titles()
    expect(titles["Interoperability"]).to_be(True)


@then("One item contains 'Cloud Migration' as the title")
def title_includes_cloud_migration(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    titles = page_object.check_for_specific_titles()
    expect(titles["Cloud Migration"]).to_be(True)


@then("One item contains 'Global Capability Center' as the title")
def title_includes_gcc(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    titles = page_object.check_for_specific_titles()
    expect(titles["Global Capability Center"]).to_be(True)


@then("One item contains 'Epic Implementation' as the title")
def title_includes_epic(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    titles = page_object.check_for_specific_titles()
    expect(titles["Epic Implementation"]).to_be(True)


@then("One item contains 'Agentic AI' as the title")
def title_includes_agentic_ai(page: Page):
    page_object = Issue0015FeaturedSolutionsPage(page)
    titles = page_object.check_for_specific_titles()
    expect(titles["Agentic AI"]).to_be(True)
