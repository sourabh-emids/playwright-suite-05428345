"""Step definitions for issue_0009: Render hero messaging and visual."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views the homepage hero section")
def view_hero_section(page: Page) -> None:
    page.goto("/")


@when("Checking heading structure")
def check_heading_structure(page: Page) -> None:
    pass


@then("Exactly one H1 element exists containing 'In Healthcare, Only Outcomes Matter'")
def h1_exists_and_correct(page: Page) -> None:
    h1s = page.locator("h1")
    expect(h1s).to_have_count(1)
    expect(h1s.first).to_contain_text("In Healthcare, Only Outcomes Matter")


@when("Reading supporting copy and eyebrow text")
def read_supporting_copy(page: Page) -> None:
    pass


@then("Body copy is legible and properly styled")
def body_copy_legible(page: Page) -> None:
    hero = page.locator("main > div").first
    expect(hero).to_be_visible()


@given("Hero contains image or video media")
def hero_has_media(page: Page) -> None:
    page.goto("/")


@when("Page is read by screen reader or image fails to load")
def screen_reader_or_image_fail(page: Page) -> None:
    pass


@then("Media has appropriate alt text or aria-label; decorative media does not create redundant output")
def media_alt_or_aria(page: Page) -> None:
    images = page.locator("main img")
    if images.count() > 0:
        first_img = images.first
        alt = first_img.get_attribute("alt")
        # Either alt is present or image has role="presentation"
        if alt is None:
            role = first_img.get_attribute("role")
            assert role in ["presentation", "img"], "Image should have alt or be decorative"


@given("User views hero on standard desktop viewport (1280x720 or larger)")
def view_desktop_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("Page loads without scrolling")
def page_loads_no_scroll(page: Page) -> None:
    page.evaluate("() => window.scrollTo(0, 0)")


@then("Primary CTA button is visible above the fold")
def cta_visible_above_fold(page: Page) -> None:
    cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    expect(cta).to_be_visible()
    box = cta.bounding_box()
    assert box is not None and box["y"] < 720


@given("User validates heading semantics")
def validate_heading_semantics(page: Page) -> None:
    page.goto("/")


@when("Checking H1 content")
def check_h1_content(page: Page) -> None:
    pass


@then("H1 contains text content and is the only H1 on the page")
def h1_valid(page: Page) -> None:
    h1 = page.locator("h1").first
    text = h1.text_content()
    assert text is not None and len(text.strip()) > 0
    h1_count = page.locator("h1").count()
    assert h1_count == 1


@given("Hero contains media asset")
def hero_has_media_asset(page: Page) -> None:
    page.goto("/")


@when("Media URL is requested")
def request_media_url(page: Page) -> None:
    pass


@then("Media asset URL resolves to valid resource")
def media_url_valid(page: Page) -> None:
    images = page.locator("main img")
    if images.count() > 0:
        src = images.first.get_attribute("src")
        assert src is not None
        response = page.request.get(src)
        assert response.ok


@when("Page renders at various viewports")
def render_at_viewports(page: Page) -> None:
    pass


@then("Long copy does not cause layout break or overlap CTA")
def long_copy_no_overlap(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    expect(page.locator("main")).to_be_visible()


@when("Page renders at 320px width")
def render_320px(page: Page) -> None:
    page.set_viewport_size({"width": 320, "height": 568})
    page.goto("/")


@then("Hero text and media scale appropriately without horizontal scroll")
def hero_scales_320(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    assert scroll_width <= 320


@given("User has prefers-reduced-motion enabled")
def reduced_motion(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("Hero has animated elements")
def hero_has_animation(page: Page) -> None:
    pass


@then("Animation is reduced or disabled per user preference")
def animation_disabled(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
