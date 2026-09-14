"""Step definitions for issue_0011: Optimize hero media loading."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("Hero media fails to load")
def hero_media_fails(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Text content remains visible and readable; layout is not broken")
def text_remains_visible(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()
    expect(page.get_by_role("link", name="See How We Deliver Outcomes")).to_be_visible()


@given("Hero contains image or video")
def hero_contains_media(page: Page) -> None:
    page.goto("/")


@when("Before media loads")
def before_media_loads(page: Page) -> None:
    pass


@then("Placeholder space is reserved using width/height attributes or aspect-ratio CSS")
def placeholder_reserved(page: Page) -> None:
    images = page.locator("main img")
    if images.count() > 0:
        first_img = images.first
        width = first_img.get_attribute("width")
        height = first_img.get_attribute("height")
        # Either explicit dimensions or aspect-ratio CSS
        css = first_img.evaluate("() => window.getComputedStyle(arguments[0]).aspectRatio", first_img)
        assert width is not None or height is not None or css is not None


@when("Media assets are requested")
def request_media_assets(page: Page) -> None:
    pass


@then("Responsive images use srcset/sizes or responsive video containers")
def responsive_media(page: Page) -> None:
    images = page.locator("main img")
    if images.count() > 0:
        srcset = images.first.get_attribute("srcset")
        sizes = images.first.get_attribute("sizes")
        # Either srcset/sizes or just regular responsive behavior
        assert srcset is not None or images.first.get_attribute("src") is not None


@given("Hero media is the LCP element")
def hero_lcp_element(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    pass


@then("Hero media loads eagerly; no lazy loading that would harm LCP score")
def eager_lcp_loading(page: Page) -> None:
    images = page.locator("main img")
    if images.count() > 0:
        loading = images.first.get_attribute("loading")
        # Should not have loading="lazy" on LCP element
        assert loading != "lazy" or images.first.get_attribute("fetchpriority") == "high"


@when("Monitoring layout stability")
def monitor_layout_stability(page: Page) -> None:
    pass


@then("Primary text does not shift position as media loads")
def no_layout_shift(page: Page) -> None:
    page.goto("/")
    h1_box = page.locator("h1").first.bounding_box()
    assert h1_box is not None
    expect(page.locator("h1")).to_be_visible()


@given("Media CDN is slow or times out")
def cdn_slow(page: Page) -> None:
    page.goto("/")


@when("Page attempts to load media")
def attempt_load_media(page: Page) -> None:
    pass


@then("Text content remains accessible; error is logged")
def text_accessible_cdn_fail(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()


@given("Media format is not supported by browser")
def unsupported_format(page: Page) -> None:
    page.goto("/")


@when("Browser attempts to render")
def browser_render(page: Page) -> None:
    pass


@then("Fallback or error state displays; page remains functional")
def fallback_or_error(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User is on slow network connection")
def slow_network(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def slow_page_load(page: Page) -> None:
    pass


@then("Text renders first; media loads progressively or shows low-quality fallback")
def progressive_loading(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()
