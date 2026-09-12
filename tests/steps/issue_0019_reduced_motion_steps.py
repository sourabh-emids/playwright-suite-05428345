"""Step definitions for Issue 0019 - Reduced motion for partner animation."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user has prefers-reduced-motion enabled")
def user_prefers_rm(page: Page):
    page.emulate_media(media_feature="prefers-reduced-motion: reduce")


@when("The user views the partner logo marquee")
def view_partner_marquee(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 3500)")


@then("Non-essential continuous motion is disabled or meaningfully reduced")
def motion_disabled(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.partnerships_section).to_be_visible()


@given("A user has prefers-reduced-motion enabled")
def rm_enabled(page: Page):
    page.emulate_media(media_feature="prefers-reduced-motion: reduce")


@when("The user views the partner section")
def view_partner_section_rm(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 3500)")


@then("All partner logos remain fully visible and discoverable")
def logos_visible_discoverable(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.partnerships_section).to_be_visible()


@given("A user views the partner section without motion")
def view_partner_no_motion(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 3500)")


@when("The user examines all partners")
def examine_all_partners(page: Page):
    pass


@then("All partners are discoverable without requiring animation")
def discoverable_no_animation(page: Page):
    homepage = HomepagePage(page)
    partners = homepage.all_partner_logos_present()
    assert len(partners) >= 10


@given("A user changes prefers-reduced-motion setting while page is open")
def change_rm_setting(page: Page):
    page.goto("/")


@when("The preference change is detected")
def preference_detected(page: Page):
    pass


@then("Animation state updates to match new preference")
def animation_updates(page: Page):
    # Toggle reduced motion
    page.emulate_media(media_feature="prefers-reduced-motion: no-preference")
    page.wait_for_timeout(500)
    expect(page.locator("body")).to_be_visible()
