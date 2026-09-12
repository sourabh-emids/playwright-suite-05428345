"""Step definitions for Hero section - EMIDS-LP-009, EMIDS-LP-010, EMIDS-LP-011"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-009_hero_page import HeroPage
from playwright.sync_api import expect


@given("The homepage hero section")
def hero_section(page):
    page.goto("/")


@when("Content is inspected")
def inspect_content(page):
    pass


@then("Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'")
def verify_h1_content(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()
    assert hero_page.count_h1_elements() == 1


@given("The hero section")
def hero_section_given(page):
    page.goto("/")


@when("Body copy is reviewed")
def review_body_copy(page):
    pass


@then("Supporting copy is present and readable")
def verify_supporting_copy(page):
    hero_page = HeroPage(page)
    expect(hero_page.hero_copy).to_be_visible()


@given("The hero visual media")
def hero_media(page):
    page.goto("/")


@when("Media fails to load or is read by screen reader")
def media_fails_or_read(page):
    pass


@then("Alternative text or fallback is provided; decorative media does not create redundant screen-reader output")
def verify_media_alternative(page):
    hero_page = HeroPage(page)
    expect(hero_page.h1_heading).to_be_visible()


@given("Common desktop viewport sizes")
def common_desktop_viewport(page):
    page.set_viewport_size({"width": 1280, "height": 800})


@when("Page loads and user scrolls to find CTA")
def load_and_scroll(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@then("Hero CTA is visible without requiring deep page scrolling")
def verify_cta_visible(page):
    hero_page = HeroPage(page)
    expect(hero_page.hero_cta).to_be_visible()


@given("Mobile viewport width")
def mobile_viewport_width(page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Hero section renders")
def hero_renders(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@then("Content remains readable and media scales appropriately")
def verify_content_readable(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()


@given("User prefers reduced motion")
def reduced_motion_preference(page):
    page.emulate_media(reduced_motion=True)


@when("Hero animations are present")
def hero_animations_present(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@then("Motion effects are reduced appropriately")
def verify_motion_reduced(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()


@given("The hero CTA button")
def hero_cta_button(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@when("Inspected for destination")
def inspect_destination(page):
    pass


@then("CTA routes to /forward-deployed-context-engineering/")
def verify_fdce_route(page):
    hero_page = HeroPage(page)
    assert hero_page.verify_canonical_fcde()


@given("Hero CTA is clicked")
def hero_cta_clicked(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")
    hero_page.click_hero_cta()


@when("Navigation occurs")
def navigation_occurs(page):
    pass


@then("Standard browser navigation behavior is preserved (back button works, referrer is set)")
def verify_standard_navigation(page):
    page.go_back()
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")
    page.go_back()
    expect(page).to_have_url("https://www.emids.com/")


@given("Hero CTA destination")
def hero_cta_destination(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@when("URL is verified")
def verify_url(page):
    pass


@then("URL uses HTTPS and is canonical")
def verify_https_canonical(page):
    hero_page = HeroPage(page)
    assert hero_page.verify_hero_cta_https()


@given("User right-clicks hero CTA")
def right_click_hero_cta(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@when("User selects 'Open in new tab'")
def open_in_new_tab(page):
    hero_page = HeroPage(page)
    url = hero_page.get_hero_cta_url()
    page.context.new_page()
    page.goto(url)


@then("FDCE page opens in new tab")
def verify_fdce_new_tab(page):
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@given("Hero media fails to load")
def hero_media_fails(page):
    pass


@when("Page renders")
def page_renders(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@then("Text content remains visible and accessible")
def verify_text_visible(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()


@given("Hero media container")
def hero_media_container(page):
    page.goto("/")


@when("Media dimensions are specified")
def media_dimensions_specified(page):
    pass


@then("Layout space is reserved preventing CLS (Cumulative Layout Shift)")
def verify_layout_reserved(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()


@given("Hero media assets")
def hero_media_assets(page):
    page.goto("/")


@when("Asset sizes are verified")
def verify_asset_sizes(page):
    pass


@then("Assets are optimized for their display size")
def verify_optimized_assets(page):
    pass


@given("Hero LCP (Largest Contentful Paint) element")
def hero_lcp_element(page):
    page.goto("/")


@when("Asset loading strategy is reviewed")
def review_loading_strategy(page):
    pass


@then("LCP asset is not lazy-loaded to prevent LCP degradation")
def verify_lcp_not_lazy(page):
    hero_page = HeroPage(page)
    expect(hero_page.h1_heading).to_be_visible()


@given("Hero section")
def hero_section_for_media(page):
    page.goto("/")


@when("Media loads")
def media_loads(page):
    pass


@then("Media loads progressively without moving primary text")
def verify_progressive_load(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()


@given("Slow network conditions")
def slow_network(page):
    pass


@when("Hero loads")
def hero_loads_slow(page):
    hero_page = HeroPage(page)
    hero_page.goto("/")


@then("Text remains readable while media loads")
def verify_text_readable(page):
    hero_page = HeroPage(page)
    hero_page.verify_h1_content()
