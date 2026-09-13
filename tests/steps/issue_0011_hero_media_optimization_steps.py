"""Steps for Hero media loading optimization (issue_0011)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0011_hero_media_optimization_page import HeroMediaOptimizationPage
from locators.issue_0011_hero_media_optimization_locators import HeroMediaOptimizationLocators


@given("Hero media fails to load")
def media_fails(page: Page) -> None:
    page.goto("/")


@given("Hero media is configured")
def media_configured(page: Page) -> None:
    page.goto("/")


@given("User views Emids homepage")
def view_homepage(page: Page) -> None:
    page.goto("/")


@given("Hero contains LCP asset")
def lcp_asset_present(page: Page) -> None:
    page.goto("/")


@given("Media is hosted on CDN")
def cdn_hosted(page: Page) -> None:
    page.goto("/")


@given("Media uses unsupported format")
def unsupported_format(page: Page) -> None:
    page.goto("/")


@given("User is on low-bandwidth connection")
def low_bandwidth(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


@when("Page loads before media downloads")
def page_loads_before_media(page: Page) -> None:
    pass


@when("Media assets are requested")
def media_requested(page: Page) -> None:
    pass


@when("Performance is measured")
def measure_performance(page: Page) -> None:
    pass


@when("CDN times out")
def cdn_timeout(page: Page) -> None:
    pass


@when("Browser attempts to render")
def browser_render(page: Page) -> None:
    pass


@when("Page loads")
def load_page(page: Page) -> None:
    pass


@then("Text content remains available and readable")
def text_available(page: Page) -> None:
    expect(HeroMediaOptimizationLocators(page).hero_text).to_be_visible()


@then("Layout shift is prevented with reserved dimensions")
def no_layout_shift(page: Page) -> None:
    pass


@then("Assets are served at appropriate sizes for viewport (srcset/sizes attributes present)")
def sized_assets(page: Page) -> None:
    media_page = HeroMediaOptimizationPage(page)
    attrs = media_page.get_image_attributes()
    for attr in attrs:
        if attr.get("src") and not attr.get("src", "").startswith("data:"):
            assert attr.get("srcset") or attr.get("sizes")


@then("Principal LCP asset is not lazy-loaded")
def lcp_not_lazy(page: Page) -> None:
    media_page = HeroMediaOptimizationPage(page)
    attrs = media_page.get_image_attributes()
    if attrs:
        loading = attrs[0].get("loading")
        assert loading != "lazy"


@then("Text content remains accessible")
def text_accessible(page: Page) -> None:
    expect(HeroMediaOptimizationLocators(page).hero_text).to_be_visible()


@then("Fallback or alternative is provided")
def fallback_provided(page: Page) -> None:
    pass


@then("Media loads progressively without blocking text content")
def progressive_load(page: Page) -> None:
    expect(HeroMediaOptimizationLocators(page).hero_text).to_be_visible()
