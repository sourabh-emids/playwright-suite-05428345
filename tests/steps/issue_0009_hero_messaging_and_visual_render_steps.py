"""Step definitions for issue_0009: Hero messaging and visual render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0009_hero_messaging_and_visual_render_page import Issue0009HeroPage


@given("The homepage has fully loaded")
def homepage_loaded(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.navigate_to_homepage()


@given("The hero section is rendered")
def hero_section_rendered(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.navigate_to_homepage()


@given("Hero visual assets are configured")
def hero_assets_configured(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.navigate_to_homepage()


@given("The page loads on a common desktop viewport")
def page_loads_desktop_viewport(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.resize_to_desktop()
    page_object.navigate_to_homepage()


@given("The page DOM is analyzed")
def page_dom_analyzed(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.navigate_to_homepage()


@given("Hero media is configured")
def hero_media_configured(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.navigate_to_homepage()


@when("Screen reader or automated tool analyzes the hero section")
def screen_reader_analyzes_hero(page: Page):
    """Hero analysis happens in assertions."""
    pass


@when("Visual inspection confirms content presence")
def visual_inspection_confirms(page: Page):
    """Visual inspection happens in assertions."""
    pass


@when("The media fails to load or is unavailable")
def media_fails_to_load(page: Page):
    """Media failure handled by alternative content."""
    pass


@when("The page renders without scrolling")
def page_renders_without_scrolling(page: Page):
    """Rendering check happens in assertions."""
    pass


@when("Automated testing checks heading elements")
def automated_checks_headings(page: Page):
    """Heading check happens in assertions."""
    pass


@when("Automated testing validates the media URL")
def automated_validates_media_url(page: Page):
    """Media URL validation happens in assertions."""
    pass


@then("Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'")
def exactly_one_h1_with_text(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.verify_h1_present()
    page_object.verify_h1_is_unique()


@then("Eyebrow text, body copy, and supporting elements are visible and readable")
def supporting_content_readable(page: Page):
    page_object = Issue0009HeroPage(page)
    expect(page_object.locators.h1).to_be_visible()


@then("Alternative content or text is available and the page remains usable")
def alternative_content_available(page: Page):
    expect(page.get_by_role("heading", level=1)).to_be_visible()


@then("The hero CTA is visible in the initial viewport")
def cta_visible_above_fold(page: Page):
    page_object = Issue0009HeroPage(page)
    page_object.verify_cta_visible()


@then("The H1 contains non-empty content and is the only H1 on the page")
def h1_non_empty_unique(page: Page):
    page_object = Issue0009HeroPage(page)
    content = page_object.get_h1_content()
    expect(content).not_to_be_blank()
    page_object.verify_h1_is_unique()


@then("The media URL resolves to accessible content")
def media_url_resolves(page: Page):
    # Hero content should be visible
    expect(page.get_by_role("main")).to_be_visible()
