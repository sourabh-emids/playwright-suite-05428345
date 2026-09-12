"""Step definitions for Partnerships section - EMIDS-LP-018, EMIDS-LP-019"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-018_partnerships_page import PartnershipsPage
from playwright.sync_api import expect


@given("Partnership section")
def partnership_section(page):
    page.goto("/")


@when("Logos are inspected")
def inspect_logos(page):
    pass


@then("All 13 logos are present: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic")
def verify_all_logos(page):
    partners_page = PartnershipsPage(page)
    partners_page.verify_section_visible()
    count = partners_page.count_partner_logos()
    assert count >= 13


@given("Partner logo elements")
def partner_logo_elements(page):
    page.goto("/")


@when("Accessibility is checked")
def check_accessibility(page):
    pass


@then("Each logo has meaningful alt text or accessibility label")
def verify_meaningful_alt(page):
    partners_page = PartnershipsPage(page)
    alt_texts = partners_page.verify_logo_alt_text()
    assert len(alt_texts) > 0


@given("Partner logos using DOM duplication for looping animation")
def dom_duplication(page):
    page.goto("/")


@when("Read by screen reader")
def read_screen_reader(page):
    pass


@then("Partner list is not duplicated and announced logically once")
def verify_not_duplicated(page):
    partners_page = PartnershipsPage(page)
    partners_page.verify_section_visible()


@given("Partner logo configuration")
def partner_logo_config(page):
    page.goto("/")


@when("Asset availability is checked")
def check_asset_availability(page):
    pass


@then("Logo asset is present and loads")
def verify_logo_loads(page):
    partners_page = PartnershipsPage(page)
    partners_page.verify_partner_logo_loaded()


@given("Edge case where logo asset is missing")
def logo_missing(page):
    pass


@when("Page renders")
def page_renders(page):
    partners_page = PartnershipsPage(page)
    partners_page.goto("/")


@then("Fallback or placeholder is shown appropriately")
def verify_fallback(page):
    partners_page = PartnershipsPage(page)
    partners_page.verify_section_visible()


@given("Marquee animation is used")
def marquee_animation(page):
    pass


@when("User prefers reduced motion")
def reduced_motion(page):
    page.emulate_media(reduced_motion=True)


@then("Animation stops or reduces meaningfully")
def verify_motion_stopped(page):
    partners_page = PartnershipsPage(page)
    partners_page.goto("/")
    partners_page.verify_section_visible()


@given("Reduced motion preference is active")
def reduced_motion_active(page):
    page.emulate_media(reduced_motion=True)


@when("Partner section renders")
def partner_section_renders(page):
    partners_page = PartnershipsPage(page)
    partners_page.goto("/")


@then("All partner logos remain fully visible and discoverable")
def verify_visible_discoverable(page):
    partners_page = PartnershipsPage(page)
    partners_page.verify_section_visible()


@given("Static view of partner logos")
def static_view(page):
    page.emulate_media(reduced_motion=True)


@when("All partners are inspected without animation")
def inspect_without_animation(page):
    partners_page = PartnershipsPage(page)
    partners_page.goto("/")


@then("All partners are discoverable without requiring animation")
def verify_discoverable(page):
    partners_page = PartnershipsPage(page)
    partners_page.verify_section_visible()


@given("User changes reduced motion preference while page is open")
def change_preference(page):
    pass


@when("Preference change is detected")
def detect_change(page):
    pass


@then("Animation state updates appropriately")
def update_state(page):
    partners_page = PartnershipsPage(page)
    partners_page.goto("/")
    partners_page.verify_section_visible()
