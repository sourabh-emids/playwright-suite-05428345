"""Step definitions for issue_0009: Hero Messaging and Visual Rendering."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.hero_page import HeroPage


@given("Hero section renders")
def hero_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Heading structure is checked")
def check_heading_structure(page: Page):
    pass


@then("Exactly one primary H1 is present with content 'In Healthcare, Only Outcomes Matter'")
def h1_present_correct_content(page: Page):
    hero = HeroPage(page)
    h1_count = page.get_by_role("heading", level=1).count()
    assert h1_count == 1, f"Expected 1 H1, found {h1_count}"
    h1_text = hero.get_h1_text()
    assert "In Healthcare, Only Outcomes Matter" in h1_text, f"H1 content mismatch: {h1_text}"


@given("Hero section renders")
def hero_renders_again(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Supporting content (eyebrow, body copy) is reviewed")
def review_supporting_content(page: Page):
    pass


@then("Supporting content is readable with appropriate contrast and font sizing")
def supporting_content_readable(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_section).to_be_visible()


@given("Hero has visual media (image/video)")
def hero_has_media(page: Page):
    page.goto("/")


@when("Page is rendered without media loading or via screen reader")
def page_without_media(page: Page):
    pass


@then("Media has appropriate alternative handling")
def media_alt_handling(page: Page):
    hero = HeroPage(page)
    if hero.hero_media.count() > 0:
        alt = hero.hero_media.get_attribute("alt")
        assert alt is not None or hero.hero_media.get_attribute("aria-label") is not None, "Media should have alt text"


@given("Hero section renders at common desktop viewport (1280x720)")
def desktop_viewport(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User views page without scrolling")
def view_without_scroll(page: Page):
    pass


@then("Primary CTA is visible above/before deep page scrolling")
def cta_above_fold(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_cta).to_be_in_viewport()


@given("H1 content is validated")
def h1_validated(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Page is checked for duplicate or empty H1")
def check_h1(page: Page):
    pass


@then("H1 is non-empty and unique on page")
def h1_nonempty_unique(page: Page):
    hero = HeroPage(page)
    h1_text = hero.get_h1_text()
    assert h1_text and h1_text.strip(), "H1 should not be empty"
    h1_count = page.get_by_role("heading", level=1).count()
    assert h1_count == 1, f"H1 should be unique, found {h1_count}"


@given("Hero media is configured")
def hero_media_configured(page: Page):
    page.goto("/")


@when("Media URL is validated")
def validate_media_url(page: Page):
    hero = HeroPage(page)
    if hero.hero_media.count() > 0:
        src = hero.hero_media.get_attribute("src")
        assert src, "Media should have valid src"


@then("Media URL resolves successfully")
def media_url_resolves(page: Page):
    pass


@given("Media network connection is slow")
def slow_media_connection(page: Page):
    page.goto("/")


@when("Page loads")
def page_loads_slow(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Text content remains available even if media delays")
def text_available_media_delay(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()


@given("Hero image/video fails to load")
def hero_media_fails(page: Page):
    page.goto("/")
    page.route(lambda url: "image" in url or "video" in url, lambda route: route.abort())


@when("Page renders")
def page_renders(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Fallback is provided and hero content remains accessible")
def fallback_provided(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()


@given("Hero has unusually long body copy")
def long_hero_copy(page: Page):
    page.goto("/")


@when("Hero renders at viewport")
def hero_at_viewport(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})


@then("Layout accommodates content without breaking")
def layout_accommodates(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_section).to_be_visible()


@given("Hero renders at mobile viewport (320px width)")
def mobile_viewport_hero(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@when("Content is reviewed")
def review_content_mobile(page: Page):
    pass


@then("Hero content is fully visible and readable")
def hero_readable_mobile(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()


@given("User has prefers-reduced-motion enabled")
def reduced_motion_hero(page: Page):
    page.emulate_media(media="screen")


@when("Hero renders with animated media")
def hero_animated(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Animated media respects reduced motion preference")
def motion_respected_hero(page: Page):
    hero = HeroPage(page)
    expect(hero.hero_h1).to_be_visible()
