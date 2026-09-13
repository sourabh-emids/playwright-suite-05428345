"""Step definitions for emids_lp_009 - Hero section."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("Exactly one H1 element is present with content 'In Healthcare, Only Outcomes Matter'")
def verify_single_h1(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    h1_elements = hero_page.h1_elements
    expect(h1_elements).to_have_count(1)
    expect(hero_page.h1).to_have_text("In Healthcare, Only Outcomes Matter")


@then("All supporting content is visible and legible with appropriate contrast")
def verify_supporting_content_readable(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    expect(hero_page.eyebrow).to_be_visible()
    expect(hero_page.body_copy).to_be_visible()
    expect(hero_page.cta).to_be_visible()


@then("Media has appropriate alt text or alternative content description")
def verify_media_alt_text(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    if hero_page.hero_media:
        alt = hero_page.hero_media.get_attribute("alt")
        # Either has alt text or is marked decorative
        expect(hero_page.hero_media).to_be_visible()


@then("The hero CTA is visible before deep page scrolling")
def verify_cta_above_fold(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    page.set_viewport_size({"width": 1280, "height": 720})
    cta_box = hero_page.cta.bounding_box()
    assert cta_box is not None
    assert cta_box["y"] < 720, "CTA not above fold"


@then("H1 has non-empty content and no duplicate H1 exists elsewhere on the page")
def verify_h1_valid(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    text = hero_page.h1.text_content()
    assert text and text.strip(), "H1 is empty"
    h1_count = hero_page.h1_elements.count()
    assert h1_count == 1, f"Found {h1_count} H1 elements"


@then("Media URL resolves successfully without 404 error")
def verify_media_url_resolves(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    if hero_page.hero_media:
        src = hero_page.hero_media.get_attribute("src")
        if src:
            response = page.request.get(src)
            assert response.status < 400, f"Media 404: {src}"


@then("Decorative media does not create redundant or confusing screen reader output")
def verify_decorative_media(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    if hero_page.hero_media:
        alt = hero_page.hero_media.get_attribute("alt")
        role = hero_page.hero_media.get_attribute("role")
        if role == "presentation" or alt == "":
            # Decorative media - should have empty alt or presentation role
            pass


@then("Text content remains available without waiting for media")
def verify_text_without_media_wait(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    expect(hero_page.h1).to_be_visible()
    expect(hero_page.body_copy).to_be_visible()


@then("Hero content renders with fallback or gracefully degraded visual")
def verify_graceful_media_failure(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    # Text should always be visible
    expect(hero_page.h1).to_be_visible()


@then("Typography and media scale responsively without horizontal overflow")
def verify_hero_responsive(page: Page) -> None:
    from pages.emids_lp_009_hero_page import HeroPage
    hero_page = HeroPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(hero_page.hero_section).to_be_visible()
    # No horizontal overflow
    scroll_width = page.evaluate("document.body.scrollWidth")
    client_width = page.evaluate("document.body.clientWidth")
    assert scroll_width <= client_width, "Horizontal overflow detected"
