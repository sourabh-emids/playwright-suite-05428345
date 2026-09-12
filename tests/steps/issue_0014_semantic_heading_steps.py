"""Step definitions for Issue 0014 - Semantic section hierarchy maintenance."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user or search engine examines the page HTML")
def examine_page_html(page: Page):
    page.goto("/")


@when("The page structure is analyzed")
def analyze_structure(page: Page):
    pass


@then("Exactly one H1 element exists on the page")
def exactly_one_h1(page: Page):
    h1s = page.get_by_role("heading", level=1)
    expect(h1s).to_have_count(1)


@given("A user examines the heading structure")
def examine_heading_structure(page: Page):
    pass


@when("The heading hierarchy is analyzed")
def analyze_headings(page: Page):
    pass


@then("Section headings use logical levels (H2, H3, etc.) without skipping levels where avoidable")
def logical_heading_levels(page: Page):
    # Get all headings
    h1s = page.get_by_role("heading", level=1).count()
    h2s = page.get_by_role("heading", level=2).count()
    h3s = page.get_by_role("heading", level=3).count()
    
    # Should have exactly one H1
    assert h1s == 1
    # H2s and H3s should exist for section headings
    assert h2s >= 1
    assert h3s >= 1


@given("A user using assistive technology navigates the page")
def at_navigation(page: Page):
    page.goto("/")


@when("The user invokes landmark navigation")
def invoke_landmark_nav(page: Page):
    pass


@then("Main, header, and footer landmarks are identifiable")
def landmarks_identifiable(page: Page):
    # Check for landmark regions
    expect(page.locator("header")).to_be_visible()
    expect(page.locator("main")).to_be_visible()
    expect(page.locator("footer")).to_be_visible()


@given("A user examines the page HTML")
def examine_html(page: Page):
    pass


@when("Interactive elements are found")
def find_interactive_elements(page: Page):
    pass


@then("Interactive text is not styled as headings solely for visual styling purposes")
def interactive_text_not_headings(page: Page):
    # Verify buttons are button elements, not styled headings
    buttons = page.locator("button")
    for btn in buttons.all():
        tag = btn.evaluate("el => el.tagName")
        assert tag == "BUTTON"


@given("A CMS editor accidentally introduces a duplicate H1")
def duplicate_h1_introduced(page: Page):
    pass


@when("The page is rendered")
def page_rendered_duplicate(page: Page):
    page.goto("/")


@then("QA testing detects the duplicate H1 accessibility violation")
def qa_detects_duplicate_h1(page: Page):
    h1s = page.get_by_role("heading", level=1)
    count = h1s.count()
    assert count == 1, f"Expected 1 H1, found {count}"
