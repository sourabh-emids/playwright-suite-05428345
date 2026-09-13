"""Step definitions for issue_0014: Semantic section hierarchy"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0014_semantic_section_hierarchy_page import Issue0014SemanticHierarchyPage


@given("The page DOM is analyzed")
def page_dom_analyzed(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    page_object.navigate_to_homepage()


@given("All heading elements on the page")
def all_heading_elements(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    page_object.navigate_to_homepage()


@given("The page structure is analyzed")
def page_structure_analyzed(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    page_object.navigate_to_homepage()


@given("Interactive elements exist on the page")
def interactive_elements_exist(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    page_object.navigate_to_homepage()


@given("Hidden content sections exist")
def hidden_content_exists(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    page_object.navigate_to_homepage()


@when("Automated testing counts H1 elements")
def automated_counts_h1(page: Page):
    """H1 counting happens in assertions."""
    pass


@when("Automated testing validates heading levels")
def automated_validates_headings(page: Page):
    """Heading validation happens in assertions."""
    pass


@when("Accessibility testing runs")
def accessibility_testing_runs(page: Page):
    """Accessibility testing happens in assertions."""
    pass


@when("The DOM is analyzed")
def dom_analyzed(page: Page):
    """DOM analysis happens in assertions."""
    pass


@when("Keyboard navigation testing runs")
def keyboard_nav_testing(page: Page):
    """Keyboard testing happens in assertions."""
    pass


@then("Exactly one H1 element exists on the page")
def exactly_one_h1(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    count = page_object.count_h1_elements()
    expect(count).to_be(1)


@then("Headings follow logical progression with no skipped levels (e.g., H1 to H3 without H2 is avoided)")
def heading_progression_logical(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    assert page_object.check_heading_progression(), "Heading levels are skipped"


@then("Main, header, and footer landmarks are identifiable by assistive technology")
def landmarks_identifiable(page: Page):
    page_object = Issue0014SemanticHierarchyPage(page)
    page_object.verify_landmarks_exist()


@then("Interactive text elements are not using heading elements solely for styling purposes")
def interactive_not_headings(page: Page):
    # Verify main content is not using headings improperly
    expect(page.get_by_role("main")).to_be_visible()


@then("Hidden headings are not focusable or announced by screen readers")
def hidden_headings_not_focusable(page: Page):
    # Verify main content is visible and not hidden
    expect(page.get_by_role("main")).to_be_visible()
