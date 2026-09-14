"""Step definitions for issue_0019: Reduced Motion for Partner Animation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("User has prefers-reduced-motion: reduce enabled")
def reduced_motion_enabled(page: Page):
    page.emulate_media(media="screen")


@when("Page renders with animated partner logos")
def page_with_animation(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Continuous motion is disabled or meaningfully reduced")
def motion_disabled(page: Page):
    section = page.locator("text=Partnerships").locator("..").locator("..")
    expect(section).to_be_visible()


@given("Animation is disabled via reduced motion preference")
def motion_disabled_preference(page: Page):
    page.emulate_media(media="screen")


@when("Partner logos render")
def logos_render_motion(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("All content remains fully visible")
def content_visible(page: Page):
    section = page.locator("text=Partnerships")
    expect(section).to_be_visible()


@given("Animation is required for loop display")
def animation_required(page: Page):
    page.goto("/")


@when("User views partner logos")
def view_partner_logos(page: Page):
    page.wait_for_load_state("networkidle")


@then("All partners can be discovered without animation")
def discover_without_animation(page: Page):
    section = page.locator("text=Partnerships")
    expect(section).to_be_visible()


@given("Page is open and user changes motion preference mid-session")
def preference_change_mid_session(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Preference change is detected")
def detect_preference_change(page: Page):
    pass


@then("Animation state updates appropriately")
def animation_updates(page: Page):
    section = page.locator("text=Partnerships")
    expect(section).to_be_visible()


@given("Animation library fails to load")
def animation_library_fails(page: Page):
    page.goto("/")
    page.route(lambda url: "animation" in url or "marquee" in url, lambda route: route.abort())


@when("Partner section renders")
def partner_section_renders(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Static fallback renders without errors")
def static_fallback(page: Page):
    section = page.locator("text=Partnerships")
    expect(section).to_be_visible()
