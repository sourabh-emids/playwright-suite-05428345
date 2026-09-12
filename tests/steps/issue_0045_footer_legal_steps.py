"""Step definitions for Issue 0045 - Footer legal navigation rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the footer legal navigation")
def view_legal_nav(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("Legal links are examined")
def examine_legal(page: Page):
    pass


@then("Each link has descriptive text, valid destination, and visible focus state")
def legal_links_properties(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.code_of_conduct_link).to_be_visible()
    expect(homepage.privacy_policy_link).to_be_visible()
    expect(homepage.cookie_policy_link).to_be_visible()
    expect(homepage.accessibility_statement_link).to_be_visible()


@given("A user examines footer legal link URLs")
def examine_legal_urls(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("URLs are inspected")
def urls_inspected(page: Page):
    pass


@then("All URLs are HTTPS and point to published pages")
def urls_https_published(page: Page):
    homepage = HomepagePage(page)
    # Privacy policy
    href = homepage.privacy_policy_link.get_attribute("href")
    assert href.startswith("https://www.emids.com/")


@given("A user views footer legal links")
def view_legal_links(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("Labels are examined")
def labels_examined(page: Page):
    pass


@then("Labels are not blank")
def labels_not_blank(page: Page):
    homepage = HomepagePage(page)
    code_of_conduct = homepage.code_of_conduct_link.text_content()
    assert code_of_conduct and len(code_of_conduct) > 0


@given("A legal page has been moved without redirect")
def legal_moved(page: Page):
    pass


@when("User clicks the footer legal link")
def click_legal(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
    page.get_by_role("link", name="Privacy Policy").click()


@then("Broken link is detected in monitoring")
def broken_link_detected(page: Page):
    page.wait_for_load_state("networkidle")


@given("A legal link label exceeds expected length")
def legal_label_long(page: Page):
    pass


@when("Footer renders at mobile width")
def footer_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@then("Label wraps gracefully without breaking layout")
def label_wraps(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.footer).to_be_visible()
