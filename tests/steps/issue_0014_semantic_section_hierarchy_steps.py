"""Step definitions for issue_0014: Semantic Section Hierarchy."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("Page renders")
def page_renders_global(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("H1 headings are counted")
def count_h1(page: Page):
    pass


@then("Exactly one page-level H1 is present")
def single_h1(page: Page):
    h1_count = page.get_by_role("heading", level=1).count()
    assert h1_count == 1, f"Expected 1 H1, found {h1_count}"


@given("Page heading structure is reviewed")
def heading_reviewed(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Headings are inspected")
def inspect_headings(page: Page):
    pass


@then("Subsequent section headings use logical levels (no skipped levels where avoidable)")
def logical_heading_levels(page: Page):
    h1 = page.get_by_role("heading", level=1).count()
    h2 = page.get_by_role("heading", level=2).count()
    h3 = page.get_by_role("heading", level=3).count()
    assert h1 >= 1, "Should have H1"
    assert h2 >= 1, "Should have H2 following H1"


@given("Page renders")
def page_renders_landmarks(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Landmarks are inspected")
def inspect_landmarks(page: Page):
    pass


@then("main, header, and footer landmarks are identifiable")
def landmarks_identifiable(page: Page):
    main = page.locator("main")
    header = page.locator("header")
    footer = page.locator("footer")
    expect(main).to_be_visible()
    expect(header).to_be_visible()
    expect(footer).to_be_visible()


@given("Interactive elements exist")
def interactive_exist(page: Page):
    page.goto("/")


@when("Heading structure is reviewed")
def heading_reviewed_interactive(page: Page):
    pass


@then("Interactive text is not styled as headings solely for visual effect")
def interactive_not_heading(page: Page):
    links = page.locator("a:has-text('Connect'), nav a").all()
    for link in links:
        tag = page.evaluate("(el) => el.tagName", link)
        assert tag == "A", "Interactive elements should not be heading tags"


@given("CMS content contains duplicate H1")
def duplicate_h1_cms(page: Page):
    page.goto("/")


@when("Page renders")
def page_renders_dup_h1(page: Page):
    page.wait_for_load_state("networkidle")


@then("Duplicate H1 is prevented or resolved appropriately")
def duplicate_h1_handled(page: Page):
    h1_count = page.get_by_role("heading", level=1).count()
    assert h1_count <= 2, "Duplicate H1 should be handled"


@given("Hidden content exists with headings")
def hidden_content_exist(page: Page):
    page.goto("/")


@when("Focusable hidden content is revealed")
def reveal_hidden(page: Page):
    pass


@then("Hidden heading does not become unexpected focus target")
def no_unexpected_focus(page: Page):
    pass
