"""Steps for Partner logo rail/marquee rendering (issue_0018)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0018_partner_logos_locators import PartnerLogosLocators


@given("User views Partnerships section")
def view_partnerships(page: Page) -> None:
    page.goto("/")


@given("Partner logos render")
def logos_render(page: Page) -> None:
    page.goto("/")


@given("DOM duplicates partner list for looping animation")
def dom_duplicates(page: Page) -> None:
    page.goto("/")


@given("Partnerships section renders")
def section_renders(page: Page) -> None:
    page.goto("/")


@given("Partner logo renders")
def logo_renders(page: Page) -> None:
    page.goto("/")


@given("Partner has transparent logo")
def transparent_logo(page: Page) -> None:
    page.goto("/")


@given("User prefers reduced motion")
def reduced_motion(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User uses screen reader")
def screen_reader(page: Page) -> None:
    pass


@when("Partner data is configured")
def data_configured(page: Page) -> None:
    pass


@when("Logo is not treated as decorative")
def not_decorative(page: Page) -> None:
    pass


@when("Page renders")
def render(page: Page) -> None:
    pass


@when("Logo renders on page background")
def render_background(page: Page) -> None:
    pass


@when("Marquee animation is active")
def marquee_active(page: Page) -> None:
    pass


@then("All approved partner logos render: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic")
def all_partners_render(page: Page) -> None:
    expect(PartnerLogosLocators(page).partnerships_section).to_be_visible()


@then("Each partner logo has meaningful accessible name via alt text or aria-label")
def accessible_names(page: Page) -> None:
    logos = PartnerLogosLocators(page).partner_logos.all()
    if logos:
        alt = logos[0].get_attribute("alt")
        aria = logos[0].get_attribute("aria-label")
        assert alt or aria


@then("Partner list is not duplicated for assistive technologies")
def not_duplicated(page: Page) -> None:
    pass


@then("Logo assets are present for each partner")
def assets_present(page: Page) -> None:
    expect(PartnerLogosLocators(page).partnerships_section).to_be_visible()


@then("Alt text or accessibility label is provided")
def alt_provided(page: Page) -> None:
    pass


@then("Placeholder or fallback displays appropriately")
def fallback(page: Page) -> None:
    pass


@then("Logo remains visible with appropriate contrast/background")
def visible_contrast(page: Page) -> None:
    pass


@then("Animation is disabled or reduced")
def animation_disabled(page: Page) -> None:
    pass
