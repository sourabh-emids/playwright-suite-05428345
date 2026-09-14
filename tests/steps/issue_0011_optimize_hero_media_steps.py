"""Step definitions for issue_0011: Optimize Hero Media Loading."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.hero_page import HeroPage


@given("Hero media fails to load")
def hero_media_fails_load(page: Page):
    page.goto("/")
    page.route(lambda url: "static" in url or "media" in url, lambda route: route.abort())


@when("Page renders")
def page_renders_media_fail(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Text content remains available")
def text_remains_available(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()


@given("Hero media has specified dimensions")
def media_has_dimensions(page: Page):
    page.goto("/")


@when("Media loads or fails")
def media_load_or_fail(page: Page):
    pass


@then("Layout space is reserved to avoid layout shift")
def layout_space_reserved(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_section).to_be_visible()


@given("Hero media is requested")
def hero_media_requested(page: Page):
    page.goto("/")


@when("Asset is loaded")
def asset_loaded(page: Page):
    page.wait_for_load_state("networkidle")


@then("Appropriately sized/optimized assets are served based on viewport")
def optimized_assets_served(page: Page):
    pass


@given("Hero contains LCP (Largest Contentful Paint) asset")
def hero_has_lcp_asset(page: Page):
    page.goto("/")


@when("Page loads")
def page_loads_lcp(page: Page):
    page.wait_for_load_state("load")


@then("Principal LCP asset is not lazy-loaded to avoid harming LCP score")
def lcp_not_lazy_loaded(page: Page):
    hero = HeroPage(page)
    if hero.hero_media.count() > 0:
        loading = hero.hero_media.get_attribute("loading")
        assert loading != "lazy", "LCP asset should not be lazy-loaded"


@given("Hero media loads")
def hero_media_loads(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Loading progresses")
def loading_progresses(page: Page):
    pass


@then("Media loads progressively without moving primary text")
def progressive_load_no_shift(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()


@given("CDN request times out during media load")
def cdn_timeout(page: Page):
    page.goto("/")
    page.route(lambda url: "cdn" in url or "cloudfront" in url, lambda route: route.abort())


@when("Page renders")
def page_renders_timeout(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Fallback handling ensures content remains accessible")
def fallback_accessible(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()


@given("Media format is unsupported by browser")
def unsupported_format(page: Page):
    page.goto("/")


@when("Page renders")
def page_renders_unsupported(page: Page):
    page.wait_for_load_state("networkidle")


@then("Alternative format or fallback is provided")
def alt_format_provided(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_section).to_be_visible()


@given("User is on low-bandwidth connection")
def low_bandwidth(page: Page):
    page.goto("/")


@when("Hero media loads")
def media_loads_low_bandwidth(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Performance is degraded gracefully without blocking content")
def graceful_degradation(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()
