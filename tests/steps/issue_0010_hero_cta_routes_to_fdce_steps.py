"""Step definitions for issue_0010: Hero CTA routes to FDCE"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0010_hero_cta_routes_to_fdce_page import Issue0010HeroCTAPage


@given("The hero section is rendered with a CTA")
def hero_rendered_with_cta(page: Page):
    page_object = Issue0010HeroCTAPage(page)
    page_object.navigate_to_homepage()


@given("The hero CTA is rendered")
def hero_cta_rendered(page: Page):
    page_object = Issue0010HeroCTAPage(page)
    page_object.navigate_to_homepage()


@when("A user clicks the hero CTA")
def user_clicks_hero_cta(page: Page):
    page_object = Issue0010HeroCTAPage(page)
    page_object.click_hero_cta()


@when("Automated testing validates the URL")
def automated_validates_url(page: Page):
    """URL validation happens in assertions."""
    pass


@when("Accessibility testing analyzes the element")
def accessibility_analyzes_element(page: Page):
    """Accessibility analysis happens in assertions."""
    pass


@then("Navigation reaches the Forward-Deployed Context Engineering page at /forward-deployed-context-engineering/")
def navigation_reaches_fdce(page: Page):
    page_object = Issue0010HeroCTAPage(page)
    page_object.verify_routes_to_fdce()


@then("The URL is HTTPS and canonical")
def url_https_canonical(page: Page):
    page_object = Issue0010HeroCTAPage(page)
    page_object.verify_https_canonical()


@then("The CTA functions as a semantic link or button with proper interactive behavior")
def cta_semantic_interactive(page: Page):
    page_object = Issue0010HeroCTAPage(page)
    page_object.verify_semantic_element()
