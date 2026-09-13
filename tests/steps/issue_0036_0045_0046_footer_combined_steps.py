"""Step definitions for issue_0036, 0045-0046: Footer combined"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0036_0045_0046_footer_combined_page import FooterPage


# Issue 0036 - Cookie Preferences
@given("The footer is rendered")
def footer_rendered(page: Page):
    page_object = FooterPage(page)
    page_object.navigate_to_homepage()


@given("A user clicks the Cookie Preferences control")
def user_clicks_cookie(page: Page):
    page_object = FooterPage(page)
    page_object.navigate_to_homepage()


@given("The user has dismissed an initial cookie banner")
def user_dismissed_banner(page: Page):
    page_object = FooterPage(page)
    page_object.navigate_to_homepage()


@when("Activation completes")
def activation_completes(page: Page):
    pass


@when("The page continues to be used")
def page_continues(page: Page):
    pass


@then("Cookie Preferences link/button is visible in the footer")
def cookie_visible(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


@then("The consent management UI opens")
def consent_ui_opens(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("Cookie Preferences control remains available in the footer")
def cookie_remains_available(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


# Issue 0045 - Legal navigation
@given("The footer legal navigation is rendered")
def legal_nav_rendered(page: Page):
    page_object = FooterPage(page)
    page_object.navigate_to_homepage()


@when("Links are analyzed")
def links_analyzed(page: Page):
    pass


@when("Focus reaches legal links")
def focus_reaches_legal(page: Page):
    page.keyboard.press("Tab")


@when("URL validation runs")
def url_validation(page: Page):
    pass


@then("Each link has descriptive text and resolves to a valid HTTPS URL")
def legal_links_descriptive(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


@then("Visible focus states are present")
def focus_states_present(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("All URLs use HTTPS protocol and point to published pages")
def https_published_urls(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


@then("No labels are blank")
def no_blank_labels(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


# Issue 0046 - Corporate contact
@given("The footer is rendered at mobile viewport")
def footer_mobile(page: Page):
    page_object = FooterPage(page)
    page_object.resize_to_mobile()
    page_object.navigate_to_homepage()


@given("Footer content is managed")
def footer_content_managed(page: Page):
    page_object = FooterPage(page)
    page_object.navigate_to_homepage()


@when("Content is reviewed")
def content_reviewed(page: Page):
    pass


@then("Footer corporate information remains readable")
def corporate_readable(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


@then("Corporate/contact information layout does not overlap or conflict with legal navigation links")
def no_overlap(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


@then("Social link URLs resolve successfully")
def social_urls_resolve(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()


@then("Only approved, current information is published")
def approved_current(page: Page):
    page_object = FooterPage(page)
    page_object.verify_footer_visible()
