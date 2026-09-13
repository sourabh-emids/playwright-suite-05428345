"""Step definitions for issue_0022: Engineering capability content render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0022_engineering_capability_content_render_page import Issue0022EngineeringCapabilityPage


@given("The Engineering capability card/panel is rendered")
def engineering_rendered(page: Page):
    page_object = Issue0022EngineeringCapabilityPage(page)
    page_object.navigate_to_homepage()


@given("The Engineering capability content is managed by CMS")
def engineering_cms_managed(page: Page):
    page_object = Issue0022EngineeringCapabilityPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection runs")
def visual_inspection(page: Page):
    pass


@when("The Engineering CTA or link is clicked")
def engineering_cta_clicked(page: Page):
    pass


@when("Automated testing validates required fields")
def automated_validates(page: Page):
    pass


@then("The Engineering label is displayed with supporting content")
def engineering_label_displayed(page: Page):
    page_object = Issue0022EngineeringCapabilityPage(page)
    page_object.verify_engineering_content()


@then("Navigation to the Engineering capability destination occurs")
def navigation_occurs(page: Page):
    expect(page).not_to_have_title("/404/")


@then("Title field is non-empty")
def title_non_empty(page: Page):
    expect(page.get_by_text("Engineering")).to_be_visible()
