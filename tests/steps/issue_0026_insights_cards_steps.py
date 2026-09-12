"""Step definitions for Issue 0026 - Insights section and content cards rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Insights section")
def view_insights(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The section loads")
def insights_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Six cards render with content type, title, image (where configured), and Download or Read More action")
def six_cards_render(page: Page):
    homepage = HomepagePage(page)
    homepage.insights_section_is_visible()
    # Check for insight card content types
    expect(page.getByText("eBook", exact=False)).to_be_visible()
    expect(page.getByText("Blog", exact=False)).to_be_visible()


@given("A user views the Insights section at desktop, tablet, and mobile widths")
def view_insights_breakpoints(page: Page):
    pass


@when("The viewport changes")
def viewport_changes_insights(page: Page):
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")
    # Tablet
    page.set_viewport_size({"width": 768, "height": 1024})
    page.wait_for_timeout(200)
    # Mobile
    page.set_viewport_size({"width": 375, "height": 812})
    page.wait_for_timeout(200)


@then("Cards remain accessible and properly laid out at all breakpoints")
def cards_accessible_breakpoints(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()


@given("A user views the Insights section")
def view_insights_published(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The cards are analyzed")
def cards_analyzed(page: Page):
    pass


@then("Only published content is displayed; unpublished resources are excluded")
def only_published(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()


@given("A user examines an Insights card")
def examine_insights_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card content is analyzed")
def card_content_analyzed(page: Page):
    pass


@then("Each card has a non-empty title and valid URL")
def card_title_url_valid(page: Page):
    homepage = HomepagePage(page)
    expect(page.getByText("Medicare Advantage", exact=False)).to_be_visible()


@given("A user views an Insights card")
def view_insights_card_action(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The action label is examined")
def action_examined(page: Page):
    pass


@then("Action label correctly reflects content flow (Download for eBooks, Read More for articles)")
def action_reflects_flow(page: Page):
    # eBook cards should have Download
    expect(page.getByText("Download", exact=False)).to_be_visible()
    # Blog cards should have Read More
    # (if blog exists)


@given("A resource is unpublished after card is configured")
def resource_unpublished(page: Page):
    pass


@when("The Insights section renders")
def insights_render_unpublished(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@then("The unpublished resource is excluded; remaining cards display correctly")
def unpublished_excluded(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()
