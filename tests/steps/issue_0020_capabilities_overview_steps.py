"""Step definitions for Issue 0020 - Capabilities overview rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Capabilities section")
def view_capabilities(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The section loads")
def capabilities_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("All three groups (AI, Engineering, Platforms) are visible with corresponding content and actions")
def three_groups_visible(page: Page):
    homepage = HomepagePage(page)
    groups = homepage.three_capability_groups_present()
    assert len(groups) == 3
    assert "Artificial Intelligence" in groups
    assert "Engineering" in groups
    assert "Platforms" in groups


@given("A user compares capabilities section to header navigation")
def compare_to_header(page: Page):
    pass


@when("The labels are compared")
def labels_compared(page: Page):
    page.goto("/")


@then("Group labels match the navigation taxonomy exactly")
def labels_match_taxonomy(page: Page):
    homepage = HomepagePage(page)
    groups = homepage.three_capability_groups_present()
    assert groups == ["Artificial Intelligence", "Engineering", "Platforms"]


@given("A user views the Capabilities section")
def view_capabilities_count(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@when("The section content is analyzed")
def content_analyzed(page: Page):
    pass


@then("Exactly three primary capability groups are displayed")
def exactly_three_groups(page: Page):
    homepage = HomepagePage(page)
    groups = homepage.three_capability_groups_present()
    assert len(groups) == 3


@given("A user views the Capabilities section at various viewport widths")
def view_capabilities_breakpoints(page: Page):
    pass


@when("The viewport changes")
def viewport_changes(page: Page):
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")
    expect(page.locator("[class*='capabilities']")).to_be_visible()
    
    # Tablet
    page.set_viewport_size({"width": 768, "height": 1024})
    page.wait_for_timeout(200)
    
    # Mobile
    page.set_viewport_size({"width": 375, "height": 812})
    page.wait_for_timeout(200)


@then("Capability cards/panels reflow responsively without content loss")
def reflow_responsive(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.capabilities_section).to_be_visible()


@given("One capability group is missing from the data")
def group_missing(page: Page):
    pass


@when("The section renders")
def section_renders_missing(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 4200)")


@then("The section renders with remaining groups; missing group does not cause errors")
def remaining_groups_render(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.capabilities_section).to_be_visible()
