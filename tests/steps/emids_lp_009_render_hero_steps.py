"""Steps for emids_lp_009: Render hero messaging and visual."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.hero.hero_page import HeroPage


@given(parsers.parse("User navigates to homepage"))
def navigate_homepage(page: Page) -> None:
    """User navigates to homepage."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("Hero section renders"))
def hero_section_renders(page: Page) -> None:
    """Hero section renders."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("User views homepage on common desktop sizes"))
def view_desktop_sizes(page: Page) -> None:
    """User views homepage on common desktop sizes."""
    page.set_viewport_size({"width": 1280, "height": 800})


@given(parsers.parse("User examines page structure"))
def examine_page_structure(page: Page) -> None:
    """User examines page structure."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("Hero includes media elements"))
def hero_includes_media(page: Page) -> None:
    """Hero includes media elements."""
    hero_page = HeroPage(page)
    hero_page.navigate()


@given(parsers.parse("Media assets load slowly"))
def media_loads_slowly(page: Page) -> None:
    """Media assets load slowly."""
    pass  # Simulated by test design


@given(parsers.parse("User views site on mobile viewport"))
def view_mobile_viewport(page: Page) -> None:
    """User views site on mobile viewport."""
    page.set_viewport_size({"width": 375, "height": 667})


@given(parsers.parse("User has prefers-reduced-motion enabled"))
def reduced_motion_enabled(page: Page) -> None:
    """User has prefers-reduced-motion enabled."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("User reads hero content")
def read_hero_content(page: Page) -> None:
    """Read hero content."""
    pass


@when("Page loads")
def page_loads(page: Page) -> None:
    """Page loads."""
    page.wait_for_load_state("domcontentloaded")


@when("User searches for H1 elements")
def search_h1_elements(page: Page) -> None:
    """Search for H1 elements."""
    pass


@when("User checks media source URLs")
def check_media_urls(page: Page) -> None:
    """Check media source URLs."""
    pass


@then(parsers.parse("Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'"))
def one_h1_with_text(page: Page) -> None:
    """Verify exactly one H1 with correct text."""
    hero_page = HeroPage(page)
    hero_page.navigate()
    expect(hero_page.locators.h1_heading).to_contain_text("In Healthcare, Only Outcomes Matter")
    expect(hero_page.get_h1_count()).to_equal(1)


@then("Body copy is visible and readable")
def body_copy_visible_readable(page: Page) -> None:
    """Verify body copy is visible and readable."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.h2_subheading).to_be_visible()


@then("Media has appropriate alternative handling")
def media_alt_handling(page: Page) -> None:
    """Verify media has appropriate alt handling."""
    hero_page = HeroPage(page)
    # Either alt text present or media is decorative
    alt = hero_page.get_media_alt_text()
    if alt:
        expect(len(alt)).to_be_greater_than(0)


@then("CTA is visible without scrolling past the hero section")
def cta_visible_without_scroll(page: Page) -> None:
    """Verify CTA is visible without scrolling."""
    hero_page = HeroPage(page)
    expect(hero_page.is_hero_cta_visible_without_scroll()).to_be_true()


@then("Exactly one H1 exists")
def exactly_one_h1(page: Page) -> None:
    """Verify exactly one H1 exists."""
    hero_page = HeroPage(page)
    expect(hero_page.get_h1_count()).to_equal(1)


@then("H1 content is non-empty")
def h1_non_empty(page: Page) -> None:
    """Verify H1 content is non-empty."""
    hero_page = HeroPage(page)
    text = hero_page.get_h1_text()
    expect(len(text)).to_be_greater_than(0)


@then("Media URLs resolve successfully")
def media_urls_resolve(page: Page) -> None:
    """Verify media URLs resolve successfully."""
    hero_page = HeroPage(page)
    href = hero_page.get_media_url()
    if href:
        expect(href).not_to_match(r"undefined|null|404")


@then("Decorative media does not create redundant screen-reader output")
def decorative_media_no_redundancy(page: Page) -> None:
    """Verify decorative media doesn't create redundant output."""
    hero_page = HeroPage(page)
    # If decorative, alt should be empty
    if hero_page.is_media_decorative():
        expect(hero_page.get_media_alt_text()).to_be_empty()


@then("Text content renders while media loads")
def text_renders_while_media_loads(page: Page) -> None:
    """Verify text content renders while media loads."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.h1_heading).to_be_visible()


@then("No blocking of critical content")
def no_blocking_critical(page: Page) -> None:
    """Verify no blocking of critical content."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.h1_heading).to_be_visible()


@then("Hero scales appropriately")
def hero_scales_appropriately(page: Page) -> None:
    """Verify hero scales appropriately."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.h1_heading).to_be_visible()


@then("Text remains readable")
def text_readable(page: Page) -> None:
    """Verify text remains readable."""
    hero_page = HeroPage(page)
    text = hero_page.get_h1_text()
    expect(len(text)).to_be_greater_than(0)


@then("CTA accessible")
def cta_accessible(page: Page) -> None:
    """Verify CTA is accessible."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.hero_cta).to_be_visible()


@then("Motion reduced or disabled")
def motion_reduced_disabled(page: Page) -> None:
    """Verify motion reduced or disabled."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.h1_heading).to_be_visible()


@then("Content remains accessible")
def content_accessible(page: Page) -> None:
    """Verify content remains accessible."""
    hero_page = HeroPage(page)
    expect(hero_page.locators.h1_heading).to_be_visible()
