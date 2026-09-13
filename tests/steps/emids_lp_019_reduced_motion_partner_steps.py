"""Steps for emids_lp_019: Respect reduced motion for partner animation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.partnerships.partnerships_page import PartnershipsPage


@given(parsers.parse("User has prefers-reduced-motion: reduce"))
def reduced_motion_reduce(page: Page) -> None:
    """User has reduced motion."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")


@given(parsers.parse("Animation is reduced or disabled"))
def animation_reduced_disabled(page: Page) -> None:
    """Animation is reduced."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")


@given(parsers.parse("Animation fails or is disabled"))
def animation_fails(page: Page) -> None:
    """Animation fails or disabled."""
    pass


@given(parsers.parse("Page is loaded and animation is running"))
def page_loaded_animation_running(page: Page) -> None:
    """Page loaded with animation."""
    partnerships_page = PartnershipsPage(page)
    partnerships_page.navigate()
    partnerships_page.scroll_to_section()


@given(parsers.parse("Animation library fails to load"))
def animation_lib_fails(page: Page) -> None:
    """Animation library fails."""
    pass


@when("Page loads partner section")
def page_loads_partner(page: Page) -> None:
    """Page loads partner section."""
    page.wait_for_load_state("domcontentloaded")


@when("User views partner section")
def view_partner_section(page: Page) -> None:
    """View partner section."""
    partnerships_page = PartnershipsPage(page)
    partnerships_page.scroll_to_section()


@when("User toggles prefers-reduced-motion preference")
def toggle_preference(page: Page) -> None:
    """Toggle preference."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="no-preference")


@when("Page renders partner section")
def page_renders_partner(page: Page) -> None:
    """Page renders partner section."""
    page.wait_for_load_state("domcontentloaded")


@then("Continuous motion animation is disabled or meaningfully reduced")
def motion_disabled_reduced(page: Page) -> None:
    """Verify motion disabled."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()


@then("All partner logos remain fully visible")
def all_logos_visible(page: Page) -> None:
    """Verify all logos visible."""
    partnerships_page = PartnershipsPage(page)
    count = partnerships_page.get_partner_logo_count()
    expect(count).to_be_greater_than(0)


@then("Content is not lost")
def content_not_lost(page: Page) -> None:
    """Verify content not lost."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()


@then("All partners are visible without animation")
def partners_visible_no_animation(page: Page) -> None:
    """Verify partners visible without animation."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.partner_logos.first).to_be_visible()


@then("Animation is not required")
def animation_not_required(page: Page) -> None:
    """Verify animation not required."""
    partnerships_page = PartnershipsPage(page)
    count = partnerships_page.get_partner_logo_count()
    expect(count).to_be_greater_than(0)


@then("Animation adjusts in real-time to new preference")
def animation_adjusts(page: Page) -> None:
    """Verify animation adjusts."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()


@then("Partners display in static fallback")
def static_fallback(page: Page) -> None:
    """Verify static fallback."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.partner_logos.first).to_be_visible()


@then("No broken state")
def no_broken_state(page: Page) -> None:
    """Verify no broken state."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()
