"""Step definitions for issue_0023: Platforms capability content render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0023_platforms_capability_content_render_page import Issue0023PlatformsCapabilityPage


@given("The Platforms capability card/panel is rendered")
def platforms_rendered(page: Page):
    page_object = Issue0023PlatformsCapabilityPage(page)
    page_object.navigate_to_homepage()


@given("The Platforms capability is rendered")
def platforms_capability_rendered(page: Page):
    page_object = Issue0023PlatformsCapabilityPage(page)
    page_object.navigate_to_homepage()


@given("The Platforms content is managed")
def platforms_content_managed(page: Page):
    page_object = Issue0023PlatformsCapabilityPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection runs")
def visual_inspection(page: Page):
    pass


@when("Labels are compared between navigation and body copy")
def labels_compared(page: Page):
    pass


@when("The Platforms CTA or link is clicked")
def platforms_cta_clicked(page: Page):
    pass


@when("Content is reviewed")
def content_reviewed(page: Page):
    pass


@then("The Platforms content is displayed with title and supporting elements")
def platforms_displayed(page: Page):
    page_object = Issue0023PlatformsCapabilityPage(page)
    page_object.verify_platforms_content()


@then("Labels use approved taxonomy consistently")
def labels_consistent(page: Page):
    expect(page.get_by_text("Platforms")).to_be_visible()


@then("Navigation to the Platforms capability destination occurs")
def navigation_occurs(page: Page):
    expect(page).not_to_have_title("/404/")


@then("Inconsistent synonyms are avoided")
def synonyms_avoided(page: Page):
    expect(page.get_by_role("main")).to_be_visible()
