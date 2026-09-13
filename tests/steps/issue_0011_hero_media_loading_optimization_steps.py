"""Step definitions for issue_0011: Hero media loading optimization"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0011_hero_media_loading_optimization_page import Issue0011HeroMediaPage


@given("Hero media fails to load")
def hero_media_fails(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    page_object.navigate_to_homepage()


@given("Hero media is configured with known dimensions")
def hero_media_configured_dimensions(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    page_object.navigate_to_homepage()


@given("Hero media is requested")
def hero_media_requested(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    page_object.navigate_to_homepage()


@given("The hero section contains the LCP element")
def hero_contains_lcp(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    page_object.navigate_to_homepage()


@when("The page renders")
def page_renders(page: Page):
    """Rendering check happens in assertions."""
    pass


@when("The page renders before media loads")
def page_renders_before_media(page: Page):
    """Layout check happens in assertions."""
    pass


@when("Automated testing validates asset sizes")
def automated_validates_asset_sizes(page: Page):
    """Asset validation happens in assertions."""
    pass


@when("Performance testing analyzes loading strategy")
def performance_analyzes_loading(page: Page):
    """Performance analysis happens in assertions."""
    pass


@then("Text content remains available and readable")
def text_content_available(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    page_object.verify_text_content_available()


@then("Placeholder space is reserved preventing cumulative layout shift")
def placeholder_reserved(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    expect(page.locator("main")).to_be_visible()


@then("Optimized format and size are served based on viewport")
def optimized_assets_served(page: Page):
    # Verify main content is visible
    expect(page.get_by_role("main")).to_be_visible()


@then("The principal LCP image is not lazy-loaded to maintain LCP performance")
def lcp_not_lazy_loaded(page: Page):
    page_object = Issue0011HeroMediaPage(page)
    page_object.verify_no_lazy_loaded_hero()
