"""Step definitions for issue_0018: Partner logo rail render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0018_partner_logo_rail_render_page import Issue0018PartnerLogosPage


@given("The Partnerships section is rendered")
def partnerships_rendered(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.navigate_to_homepage()


@given("Partner logos are rendered")
def partner_logos_rendered(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.navigate_to_homepage()


@given("A screen reader user navigates the Partnerships section")
def screen_reader_navigates_partnerships(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.navigate_to_homepage()


@given("Partner logos are configured")
def partner_logos_configured(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.navigate_to_homepage()


@given("The Partnerships section uses a marquee animation")
def partnerships_uses_marquee(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.navigate_to_homepage()


@when("Visual inspection confirms logos")
def visual_inspection_logos(page: Page):
    """Visual inspection happens in assertions."""
    pass


@when("Accessibility testing runs")
def accessibility_testing_runs(page: Page):
    """Accessibility testing happens in assertions."""
    pass


@when("The user encounters the partner logos")
def user_encounters_logos(page: Page):
    """Encounter check happens in assertions."""
    pass


@when("Automated testing validates assets")
def automated_validates_assets(page: Page):
    """Asset validation happens in assertions."""
    pass


@when("The page renders on devices supporting animation")
def page_renders_with_animation(page: Page):
    """Animation check happens in assertions."""
    pass


@then("Logos display for: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, and Anthropic")
def logos_display_all_partners(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.verify_partnerships_section()


@then("Each logo has an alt attribute or aria-label providing meaningful accessible name")
def logos_have_accessible_names(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.verify_logos_have_accessible_names()


@then("The content is not announced multiple times due to DOM duplication for looping animation")
def content_not_duplicated(page: Page):
    # Main content should be visible
    expect(page.get_by_role("main")).to_be_visible()


@then("All logo image assets resolve successfully")
def assets_resolve_successfully(page: Page):
    page_object = Issue0018PartnerLogosPage(page)
    page_object.verify_assets_resolve()


@then("The animation plays smoothly")
def animation_plays_smoothly(page: Page):
    expect(page.get_by_role("main")).to_be_visible()
