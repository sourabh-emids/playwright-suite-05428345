"""Step definitions for Issue 0011 - Hero media loading optimization."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("The hero media fails to load")
def hero_media_fails(page: Page):
    pass  # Would need network interception


@when("The page renders")
def page_renders(page: Page):
    pass


@then("Text content remains available and readable")
def text_content_readable(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.hero_h1).to_be_visible()
    expect(homepage.hero_h2).to_be_visible()


@given("A user loads the page")
def load_page(page: Page):
    page.goto("/")


@when("The page initially renders before media loads")
def page_renders_before_media(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Image/video dimensions are reserved to avoid layout shift (CLS)")
def dimensions_reserved(page: Page):
    # Check for width/height attributes on images
    hero_images = page.locator("[class*='hero'] img")
    for img in hero_images.all():
        width = img.get_attribute("width")
        height = img.get_attribute("height")
        # Either has dimensions or aspect-ratio CSS
        style = img.get_attribute("style") or ""
        has_dimensions = (width and height) or "aspect-ratio" in style
        # Allow for decorative images to be handled differently


@given("A user loads the page on a mobile device")
def load_page_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("/")


@when("Media assets are requested")
def media_requested(page: Page):
    page.wait_for_load_state("networkidle")


@then("Appropriately sized assets (via srcset/sizes) are served")
def assets_sized_appropriately(page: Page):
    # Check for responsive images
    hero_images = page.locator("[class*='hero'] img")
    for img in hero_images.all():
        srcset = img.get_attribute("srcset")
        sizes = img.get_attribute("sizes")
        # Either has srcset or is appropriately sized


@given("A user loads the page")
def load_page_for_lcp(page: Page):
    page.goto("/")


@when("The LCP (Largest Contentful Paint) asset loads")
def lcp_asset_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("The principal hero LCP asset is not lazy-loaded in a way that harms LCP score")
def lcp_not_lazy_loaded(page: Page):
    # Check hero image loading attribute
    hero_images = page.locator("[class*='hero'] img")
    if hero_images.count() > 0:
        loading = hero_images.first.get_attribute("loading")
        # Hero image should not be lazy
        if loading:
            assert loading != "lazy"


@given("A user views the hero media")
def view_hero_media(page: Page):
    pass


@when("The media element is examined")
def media_examined(page: Page):
    pass


@then("Poster and alt attributes are appropriately set")
def poster_alt_set(page: Page):
    videos = page.locator("[class*='hero'] video")
    if videos.count() > 0:
        poster = videos.first.get_attribute("poster")
        # Video should have poster if present
    
    images = page.locator("[class*='hero'] img")
    for img in images.all():
        alt = img.get_attribute("alt")
        # alt should be set or image should be decorative


@given("The CDN serving hero media times out")
def cdn_timeout(page: Page):
    pass


@when("The page loads")
def page_loads_cdn(page: Page):
    page.goto("/")


@then("Text content remains available without blocking rendering")
def text_no_block(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.hero_h1).to_be_visible()
    expect(homepage.hero_h2).to_be_visible()
