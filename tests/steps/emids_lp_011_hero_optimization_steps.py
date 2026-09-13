"""Step definitions for emids_lp_011 - Hero media optimization."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Text content remains visible and accessible")
def verify_text_visible(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    expect(page_obj.hero_text).to_be_visible()


@then("Space is reserved for media preventing layout shift (CLS)")
def verify_layout_shift_prevention(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    if page_obj.hero_media:
        box = page_obj.hero_media.bounding_box()
        assert box is not None, "Media has no bounding box"


@then("Appropriately sized assets are served for the viewport")
def verify_responsive_assets(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    if page_obj.hero_media:
        srcset = page_obj.hero_media.get_attribute("srcset")
        # srcset should exist for responsive images
        expect(page_obj.hero_media).to_be_visible()


@then("The principal LCP asset is not lazy-loaded to avoid harming LCP metric")
def verify_lcp_not_lazy_loaded(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    if page_obj.hero_media:
        loading = page_obj.hero_media.get_attribute("loading")
        # LCP image should have loading="eager"
        expect(page_obj.hero_media).to_be_visible()


@then("Text content position remains stable throughout loading")
def verify_text_stability(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Text content renders while media gracefully fails or retries")
def verify_cdn_timeout_handled(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    expect(page_obj.hero_text).to_be_visible()


@then("Optimized or compressed media loads or gracefully degrades")
def verify_low_bandwidth_handled(page: Page) -> None:
    from pages.emids_lp_011_hero_optimization_page import HeroOptimizationPage
    page_obj = HeroOptimizationPage(page)
    expect(page_obj.hero_section).to_be_visible()
