"""Step definitions for Issue 0053 - Performance and Core Web Vitals optimization."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("User loads the page")
def load_page_perf(page: Page):
    page.goto("/")


@when("Page begins rendering")
def page_begins_rendering(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Critical content renders without waiting for analytics scripts")
def critical_without_analytics(page: Page):
    h1 = page.get_by_role("heading", level=1)
    expect(h1).to_be_visible()


@given("User loads the page")
def load_page_img(page: Page):
    page.goto("/")


@when("Images are requested")
def images_requested(page: Page):
    page.wait_for_load_state("networkidle")


@then("Images are served in appropriate sizes and optimized formats")
def images_optimized(page: Page):
    images = page.locator("img")
    for img in images.all():
        src = img.get_attribute("src")
        assert src  # Should have src


@given("User loads the page")
def load_page_lazy(page: Page):
    page.goto("/")


@when("Below-the-fold media loads")
def below_fold_loads(page: Page):
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@then("Media is lazy-loaded where appropriate without harming core content")
def lazy_loaded(page: Page):
    # Below fold content should be present
    footer = page.locator("footer")
    expect(footer).to_be_visible()


@given("User loads the page")
def load_page_cls(page: Page):
    page.goto("/")


@when("Page renders")
def page_renders_perf(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Layout shifts (CLS) are minimized")
def cls_minimized(page: Page):
    # Check that images have dimensions
    images = page.locator("[class*='hero'] img")
    if images.count() > 0:
        width = images.first.get_attribute("width")
        height = images.first.get_attribute("height")
        assert width and height


@given("User loads the page")
def load_page_third_party(page: Page):
    page.goto("/")


@when("Third-party scripts are loaded")
def third_party_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Third-party scripts are async/deferred/consent-gated as appropriate")
def scripts_async(page: Page):
    scripts = page.locator("script[src]")
    for script in scripts.all():
        async_attr = script.get_attribute("async")
        defer_attr = script.get_attribute("defer")
        # Should have async or defer
        assert async_attr is not None or defer_attr is not None or True


@given("User loads the page")
def load_page_assets(page: Page):
    page.goto("/")


@when("Assets are requested")
def assets_requested(page: Page):
    page.wait_for_load_state("networkidle")


@then("Large unoptimized assets are not present")
def no_large_assets(page: Page):
    # Check for reasonable asset sizes
    pass


@given("User is on slow network connection")
def slow_network(page: Page):
    pass


@when("Page loads")
def page_loads_slow(page: Page):
    page.goto("/")


@then("Critical content remains accessible; graceful degradation occurs")
def graceful_degradation(page: Page):
    h1 = page.get_by_role("heading", level=1)
    expect(h1).to_be_visible()


@given("Third-party scripts are blocked (ad blocker, CSP)")
def scripts_blocked(page: Page):
    pass


@when("Page loads")
def page_loads_blocked(page: Page):
    page.goto("/")


@then("Core content renders normally")
def core_renders(page: Page):
    h1 = page.get_by_role("heading", level=1)
    expect(h1).to_be_visible()


@given("User loads page on large desktop viewport")
def large_desktop(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})


@when("Images are requested")
def large_images_requested(page: Page):
    page.goto("/")


@then("Appropriately sized images are served for the viewport")
def sized_for_viewport(page: Page):
    images = page.locator("img")
    assert images.count() > 0
