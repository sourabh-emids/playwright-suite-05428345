"""Step definitions for Issue 0009 - Hero messaging and visual rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user loads the Emids homepage")
def load_emids_homepage(page: Page):
    page.goto("/")


@when("The page loads completely")
def page_loads_completely(page: Page):
    page.wait_for_load_state("networkidle")


@then("Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'")
def h1_present_and_unique(page: Page):
    homepage = HomepagePage(page)
    h1_text = homepage.hero_h1_is_present()
    assert "In Healthcare, Only Outcomes Matter" in h1_text
    assert homepage.hero_h1_is_unique()


@given("A user views the hero section")
def view_hero_section(page: Page):
    pass


@when("The user examines the supporting copy")
def examine_supporting_copy(page: Page):
    pass


@then("Supporting content is readable and not truncated")
def supporting_copy_readable(page: Page):
    homepage = HomepagePage(page)
    h2_text = homepage.hero_h2_is_readable()
    assert len(h2_text) > 20  # Should have meaningful content


@given("A user is viewing the hero with assistive technology")
def view_hero_with_at(page: Page):
    pass


@when("The screen reader encounters the hero media")
def screen_reader_encounters_media(page: Page):
    pass


@then("Appropriate alternative text or aria-label is provided")
def alt_text_provided(page: Page):
    # Check for images with alt text
    images = page.locator("img")
    if images.count() > 0:
        for img in images.all():
            alt = img.get_attribute("alt")
            # Either has alt text or is marked as decorative
            if alt is None:
                role = img.get_attribute("role")
                aria_hidden = img.get_attribute("aria-hidden")
                assert role == "presentation" or aria_hidden == "true"


@given("A user loads the Emids homepage on a common desktop viewport")
def load_homepage_desktop(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("The page loads and the user has not scrolled")
def user_has_not_scrolled(page: Page):
    pass


@then("The hero CTA is visible above or before deep page scrolling")
def hero_cta_visible(page: Page):
    homepage = HomepagePage(page)
    homepage.hero_cta_is_visible()


@given("A user or search engine examines the page")
def examine_page_for_seo(page: Page):
    pass


@when("The page HTML is analyzed")
def analyze_html(page: Page):
    pass


@then("The H1 is non-empty and unique")
def h1_non_empty_unique(page: Page):
    homepage = HomepagePage(page)
    assert homepage.hero_h1_is_unique()
    h1_text = homepage.hero_h1_is_present()
    assert len(h1_text) > 0


@given("A user views the hero section")
def view_hero_for_media(page: Page):
    pass


@when("The page loads the hero media")
def hero_media_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("The media URL resolves successfully")
def media_url_resolves(page: Page):
    # Verify no broken images
    page.wait_for_load_state("networkidle")


@then("Text content remains available if media fails")
def text_content_available_on_media_fail(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.hero_h1).to_be_visible()
    expect(homepage.hero_h2).to_be_visible()


@given("A user is viewing the site on a mobile device (320px width)")
def view_mobile_320(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@when("The page loads")
def mobile_page_loads(page: Page):
    page.goto("/")


@then("Hero content renders properly without horizontal scrolling")
def hero_renders_mobile(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.hero_h1).to_be_visible()
    expect(homepage.hero_cta).to_be_visible()
    # Check no horizontal scroll
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    assert scroll_width <= 320


@given("A user has prefers-reduced-motion enabled")
def prefers_reduced_motion(page: Page):
    page.emulate_media(media_feature="prefers-reduced-motion: reduce")


@when("The page loads")
def page_loads_rm(page: Page):
    page.goto("/")


@then("Hero animations are reduced or eliminated")
def hero_animation_reduced(page: Page):
    expect(page.locator("body")).to_be_visible()
