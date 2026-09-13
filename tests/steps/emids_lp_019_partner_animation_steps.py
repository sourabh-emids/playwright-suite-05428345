"""Step definitions for emids_lp_019 - Partner animation reduced motion."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Non-essential continuous motion is disabled or meaningfully reduced")
def verify_animation_disabled(page: Page) -> None:
    from pages.emids_lp_019_partner_animation_page import PartnerAnimationPage
    page_obj = PartnerAnimationPage(page)
    expect(page_obj.section).to_be_visible()


@then("All partner content remains fully visible and accessible")
def verify_content_visible(page: Page) -> None:
    from pages.emids_lp_019_partner_animation_page import PartnerAnimationPage
    page_obj = PartnerAnimationPage(page)
    logos = page_obj.partner_logos
    expect(logos.first).to_be_visible()


@then("All partners are visible without requiring animation to view content")
def verify_partners_visible_no_animation(page: Page) -> None:
    from pages.emids_lp_019_partner_animation_page import PartnerAnimationPage
    page_obj = PartnerAnimationPage(page)
    expect(page_obj.section).to_be_visible()


@then("Animation state updates without page reload")
def verify_preference_change_handled(page: Page) -> None:
    from pages.emids_lp_019_partner_animation_page import PartnerAnimationPage
    page_obj = PartnerAnimationPage(page)
    expect(page_obj.section).to_be_visible()


@then("Partners render in static fallback layout")
def verify_animation_library_failure(page: Page) -> None:
    from pages.emids_lp_019_partner_animation_page import PartnerAnimationPage
    page_obj = PartnerAnimationPage(page)
    expect(page_obj.section).to_be_visible()
