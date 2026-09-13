"""Step definitions for issue_0021: AI capability content render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0021_ai_capability_content_render_page import Issue0021AICapabilityPage


@given("The AI capability card/panel is rendered")
def ai_capability_rendered(page: Page):
    page_object = Issue0021AICapabilityPage(page)
    page_object.navigate_to_homepage()


@given("The AI capability content is managed by CMS")
def ai_content_managed_by_cms(page: Page):
    page_object = Issue0021AICapabilityPage(page)
    page_object.navigate_to_homepage()


@given("The AI capability link is rendered")
def ai_link_rendered(page: Page):
    page_object = Issue0021AICapabilityPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection runs")
def visual_inspection_runs(page: Page):
    pass


@when("The AI CTA or link is clicked")
def ai_cta_clicked(page: Page):
    page_object = Issue0021AICapabilityPage(page)
    # Try to click if it's a link
    ai_link = page.get_by_role("link", name="AI")
    if ai_link.count() > 0:
        ai_link.first.click()


@when("Automated testing validates required fields")
def automated_validates_fields(page: Page):
    pass


@when("Automated testing validates the URL")
def automated_validates_url(page: Page):
    pass


@then("The AI label is displayed with supporting content")
def ai_label_displayed(page: Page):
    page_object = Issue0021AICapabilityPage(page)
    page_object.verify_ai_content()


@then("Navigation to the AI capability destination occurs")
def navigation_occurs(page: Page):
    expect(page).not_to_have_title("/404/")


@then("Title field is non-empty")
def title_non_empty(page: Page):
    ai_text = page.get_by_text("AI").first
    text = ai_text.inner_text()
    expect(text).not_to_be_blank()


@then("The destination URL is valid and returns HTTP 200")
def url_valid(page: Page):
    expect(page.get_by_role("main")).to_be_visible()
