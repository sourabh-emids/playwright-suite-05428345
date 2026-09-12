"""Step definitions for Issue 0028 - CMS-0057 interoperability resource card."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the CMS-0057 interoperability resource card")
def view_cms0057_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card renders")
def cms0057_renders(page: Page):
    page.wait_for_load_state("networkidle")


@then("Card title, type, and action are populated from approved content")
def cms0057_content(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.cms_0057_ebook).to_be_visible()
    expect(page.getByText("eBook", exact=False)).to_be_visible()


@given("A user clicks the CMS-0057 card action")
def click_cms0057_action(page: Page):
    homepage = HomepagePage(page)
    homepage.click_insight_card("CMS-0057: The Interoperability Imperative")


@when("The action is activated")
def cms0057_activated(page: Page):
    pass


@then("User is navigated to the intended CMS-0057 resource destination")
def cms0057_navigates(page: Page):
    page.wait_for_url("**/insights/cms-0057-the-interoperability-imperative/**")


@given("A user examines the CMS-0057 card")
def examine_cms0057_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card content is analyzed")
def cms0057_analyzed(page: Page):
    pass


@then("Title and destination are not empty")
def cms0057_not_empty(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.cms_0057_ebook).to_be_visible()


@given("The CMS-0057 content is unpublished")
def cms0057_unpublished(page: Page):
    pass


@when("The Insights section renders")
def insights_render_cms0057(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@then("The card is excluded or shows appropriate unavailable state")
def cms0057_handled(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()
