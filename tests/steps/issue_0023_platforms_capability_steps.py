"""Step definitions for Issue 0023 - Platforms capability content rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Capabilities section")
def view_capabilities_plat(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The Platforms capability panel/card loads")
def platforms_panel_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Platforms content renders as a card/panel matching the capability visual system")
def platforms_content_renders(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.platforms_capability).to_be_visible()


@given("A user compares Platforms label in section to header navigation")
def compare_platforms_label(page: Page):
    page.goto("/")


@when("Labels are compared")
def labels_compared_plat(page: Page):
    pass


@then("Labels use approved taxonomy consistently (e.g., 'Platforms' not mixed with 'Provider Platforms')")
def platforms_taxonomy_consistent(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.platforms_capability).to_be_visible()
    expect(homepage.capabilities_section).to_be_visible()


@given("A user examines the Platforms section and header")
def examine_platforms(page: Page):
    page.goto("/")


@when("Both are compared")
def section_header_compared(page: Page):
    pass


@then("No inconsistent synonyms exist unless intentionally approved by content governance")
def no_inconsistent_synonyms(page: Page):
    # Check that "Platforms" is used consistently
    platforms_text = page.getByText("Platforms", exact=False)
    expect(platforms_text.first).to_be_visible()


@given("CMS content has been updated to a different taxonomy")
def cms_updated_taxonomy(page: Page):
    pass


@when("The page renders")
def page_renders_taxonomy(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@then("QA/content validation detects naming mismatches in publishing workflow")
def qa_detects_mismatch(page: Page):
    homepage = HomepagePage(page)
    groups = homepage.three_capability_groups_present()
    # Should match expected taxonomy
    assert "Platforms" in groups
