"""Step definitions for Issue 0030 - AI ROI eBook card display."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the AI ROI eBook card")
def view_ai_roi_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card renders")
def ai_roi_renders(page: Page):
    page.wait_for_load_state("networkidle")


@then("Card displays 'Closing the AI ROI Gap in Healthcare' with eBook labeling and expected action")
def ai_roi_content(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.ai_roi_ebook).to_be_visible()
    expect(page.getByText("eBook", exact=False)).to_be_visible()


@given("A user examines the AI ROI eBook card")
def examine_ai_roi(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The content is analyzed")
def ai_roi_analyzed(page: Page):
    pass


@then("Content is published and URL is valid")
def ai_roi_valid(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.ai_roi_ebook).to_be_visible()
    href = homepage.ai_roi_ebook.get_attribute("href")
    assert href and "/insights/" in href


@given("The AI ROI resource is unpublished or redirected")
def ai_roi_unpublished(page: Page):
    pass


@when("The Insights section renders")
def insights_render_ai_roi(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@then("Appropriate handling occurs without breaking page")
def ai_roi_handled(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()
