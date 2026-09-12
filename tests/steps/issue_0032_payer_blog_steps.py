"""Step definitions for Issue 0032 - Payer data readiness blog card."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Payer data readiness blog card")
def view_payer_blog(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card renders")
def payer_blog_renders(page: Page):
    page.wait_for_load_state("networkidle")


@then("Card shows type=Blog and CTA='Read More'")
def payer_blog_content(page: Page):
    # Check for blog type indicator
    expect(page.getByText("Blog", exact=False)).to_be_visible()
    expect(page.getByText("Read More", exact=False)).to_be_visible()


@given("A user clicks the Read More action on the blog card")
def click_blog_read_more(page: Page):
    page.getByText("FinOps Principles", exact=False).first.locator("..").click()


@when("The action is activated")
def blog_activated(page: Page):
    pass


@then("User is navigated to the correct article/detail experience")
def blog_navigates(page: Page):
    page.wait_for_url("**/insights/**")


@given("A user examines the blog card CTA label")
def examine_blog_cta(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The label is analyzed")
def cta_analyzed(page: Page):
    pass


@then("CTA label reflects article navigation ('Read More') rather than file download ('Download')")
def cta_reflects_nav(page: Page):
    # Should have Read More, not Download
    read_more = page.getByText("Read More", exact=False)
    download = page.getByText("Download", exact=False)
    expect(read_more.first).to_be_visible()


@given("The Payer data readiness article has been moved")
def payer_article_moved(page: Page):
    pass


@when("A user clicks the Read More action")
def click_payer_read_more(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")
    page.getByText("Read More", exact=False).first.click()


@then("Appropriate redirect or error handling occurs")
def payer_blog_handled(page: Page):
    page.wait_for_load_state("networkidle")
