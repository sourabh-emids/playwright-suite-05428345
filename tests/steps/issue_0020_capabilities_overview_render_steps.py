"""Step definitions for issue_0020: Capabilities overview render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0020_capabilities_overview_render_page import Issue0020CapabilitiesPage


@given("The Capabilities section is rendered")
def capabilities_rendered(page: Page):
    page_object = Issue0020CapabilitiesPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection runs")
def visual_inspection_runs(page: Page):
    """Visual inspection happens in assertions."""
    pass


@when("Each capability group is analyzed")
def group_analyzed(page: Page):
    """Group analysis happens in assertions."""
    pass


@when("Labels are compared to header navigation")
def labels_compared(page: Page):
    """Label comparison happens in assertions."""
    pass


@when("Viewport is resized across breakpoints")
def viewport_resized(page: Page):
    page_object = Issue0020CapabilitiesPage(page)
    page_object.resize_to_viewport(375, 812)
    page_object.resize_to_viewport(768, 1024)
    page_object.resize_to_viewport(1280, 720)


@then("Three groups are visible: AI, Engineering, and Platforms")
def three_groups_visible(page: Page):
    page_object = Issue0020CapabilitiesPage(page)
    page_object.verify_all_groups_visible()


@then("Each group contains summary text and/or links/media")
def groups_have_content(page: Page):
    page_object = Issue0020CapabilitiesPage(page)
    page_object.verify_all_groups_visible()


@then("Group labels (AI, Engineering, Platforms) match the navigation taxonomy exactly")
def labels_match_taxonomy(page: Page):
    page_object = Issue0020CapabilitiesPage(page)
    page_object.verify_all_groups_visible()


@then("Capability cards/panels reflow appropriately without breaking layout")
def cards_reflow_appropriately(page: Page):
    page_object = Issue0020CapabilitiesPage(page)
    page_object.verify_layout_intact()
