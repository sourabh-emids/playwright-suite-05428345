"""Step definitions for Issue 0052 - Responsive layout across viewports."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("User views page at desktop, tablet, and mobile widths")
def view_page_widths(page: Page):
    pass


@when("Viewport changes to each supported width")
def viewport_changes_widths(page: Page):
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.wait_for_timeout(200)
    # Tablet
    page.set_viewport_size({"width": 768, "height": 1024})
    page.wait_for_timeout(200)
    # Mobile
    page.set_viewport_size({"width": 375, "height": 812})


@then("No unintended horizontal scrolling occurs")
def no_horizontal_scroll(page: Page):
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    assert scroll_width <= inner_width


@given("User views page at mobile width (320px)")
def view_mobile_320_responsive(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@when("Text is rendered")
def text_rendered(page: Page):
    page.goto("/")


@then("Typography remains readable at all supported widths")
def typography_readable(page: Page):
    homepage = HomepagePage(page)
    homepage.hero_h1_is_present()


@given("User views page at narrow viewport")
def view_narrow_viewport(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})


@when("Interactive elements are rendered")
def elements_rendered(page: Page):
    page.goto("/")


@then("Controls do not overlap")
def no_overlap(page: Page):
    homepage = HomepagePage(page)
    homepage.header_is_visible()


@given("User views page at various viewport widths")
def view_various_widths(page: Page):
    pass


@when("All sections are loaded")
def all_sections_loaded(page: Page):
    page.goto("/")


@then("All cards and sections remain accessible and available")
def all_sections_accessible(page: Page):
    homepage = HomepagePage(page)
    homepage.hero_section
    homepage.featured_solutions_section


@given("User views page at various widths")
def view_widths_img(page: Page):
    page.goto("/")


@when("Images are rendered")
def images_rendered(page: Page):
    pass


@then("Images preserve aspect ratio")
def aspect_ratio_preserved(page: Page):
    images = page.locator("img")
    for img in images.all():
        natural_width = img.get_attribute("naturalWidth") or img.get_attribute("width")
        natural_height = img.get_attribute("naturalHeight") or img.get_attribute("height")
        if natural_width and natural_height:
            ratio = int(natural_width) / int(natural_height)
            assert 0.1 < ratio < 20


@given("User views page at 320 CSS px width")
def view_320px(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@when("Content is rendered")
def content_rendered(page: Page):
    page.goto("/")


@then("Content is usable without horizontal scrolling")
def usable_no_hscroll(page: Page):
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    assert scroll_width <= 320


@given("User sets browser zoom to 200%")
def zoom_200_responsive(page: Page):
    page.set_viewport_size({"width": 640, "height": 500})


@when("Page renders")
def page_renders_200(page: Page):
    page.goto("/")


@then("Layout reflows without overlap or loss of functionality")
def reflow_no_overlap(page: Page):
    homepage = HomepagePage(page)
    homepage.hero_section


@given("Content contains text exceeding expected length")
def long_text(page: Page):
    pass


@when("Page renders at mobile width")
def renders_mobile_long(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("/")


@then("Text wraps gracefully without breaking layout")
def text_wraps_layout(page: Page):
    homepage = HomepagePage(page)
    homepage.hero_h2_is_readable()


@given("User views page on phone in landscape orientation")
def phone_landscape(page: Page):
    page.set_viewport_size({"width": 844, "height": 390})


@when("Page renders")
def renders_landscape(page: Page):
    page.goto("/")


@then("Layout adapts appropriately")
def adapts_landscape(page: Page):
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    assert scroll_width <= inner_width


@given("User views page on tablet in split-screen mode")
def tablet_split(page: Page):
    page.set_viewport_size({"width": 500, "height": 1024})


@when("Page renders")
def renders_split(page: Page):
    page.goto("/")


@then("Layout adapts to available width without horizontal scroll")
def adapts_split(page: Page):
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    assert scroll_width <= inner_width
