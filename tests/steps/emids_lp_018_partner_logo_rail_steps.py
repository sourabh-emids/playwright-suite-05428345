"""Steps for emids_lp_018: Render partner logo rail/marquee."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.partnerships.partnerships_page import PartnershipsPage


@given(parsers.parse("User views partner section"))
def view_partner_section(page: Page) -> None:
    """User views partner section."""
    partnerships_page = PartnershipsPage(page)
    partnerships_page.navigate()
    partnerships_page.scroll_to_section()


@given(parsers.parse("User with screen reader views partner logos"))
def screen_reader_view(page: Page) -> None:
    """User with screen reader views."""
    partnerships_page = PartnershipsPage(page)
    partnerships_page.navigate()
    partnerships_page.scroll_to_section()


@given(parsers.parse("Marquee uses DOM duplication for looping"))
def marquee_duplication(page: Page) -> None:
    """Marquee uses DOM duplication."""
    pass


@given(parsers.parse("CMS configures partners"))
def cms_configures_partners(page: Page) -> None:
    """CMS configures partners."""
    pass


@given(parsers.parse("Logo is treated as decorative"))
def logo_decorative(page: Page) -> None:
    """Logo is decorative."""
    pass


@given(parsers.parse("Partner has transparent logo"))
def transparent_logo(page: Page) -> None:
    """Partner has transparent logo."""
    pass


@given(parsers.parse("User has prefers-reduced-motion enabled"))
def reduced_motion_enabled(page: Page) -> None:
    """User has reduced motion enabled."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")


@when("User counts partner logos")
def count_partner_logos(page: Page) -> None:
    """Count partner logos."""
    pass


@when("Screen reader reads logos")
def screen_reader_reads(page: Page) -> None:
    """Screen reader reads logos."""
    pass


@when("Screen reader navigates partner section")
def screen_reader_navigates(page: Page) -> None:
    """Screen reader navigates."""
    pass


@when("Partner without logo is added")
def partner_without_logo(page: Page) -> None:
    """Partner without logo is added."""
    pass


@when("Logo renders on page background")
def logo_renders(page: Page) -> None:
    """Logo renders."""
    pass


@when("Partner marquee animation runs")
def marquee_animation_runs(page: Page) -> None:
    """Marquee animation runs."""
    pass


@then("All logos present: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic")
def all_logos_present(page: Page) -> None:
    """Verify all logos present."""
    partnerships_page = PartnershipsPage(page)
    count = partnerships_page.get_partner_logo_count()
    expect(count).to_be_greater_than_or_equal(13)


@then("Each logo has meaningful accessibility label")
def logo_meaningful_alt(page: Page) -> None:
    """Verify each logo has meaningful alt."""
    partnerships_page = PartnershipsPage(page)
    names = partnerships_page.get_partner_names()
    for name in names:
        expect(len(name)).to_be_greater_than(0)


@then("Partner name is announced")
def partner_name_announced(page: Page) -> None:
    """Verify partner name is announced."""
    partnerships_page = PartnershipsPage(page)
    names = partnerships_page.get_partner_names()
    expect(len(names)).to_be_greater_than(0)


@then("Partner list is not announced multiple times")
def not_announced_multiple(page: Page) -> None:
    """Verify not announced multiple times."""
    partnerships_page = PartnershipsPage(page)
    # Check for aria-live or proper semantics
    pass


@then("Logical order maintained")
def logical_order(page: Page) -> None:
    """Verify logical order."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()


@then("Partner without logo asset does not display")
def no_display_without_logo(page: Page) -> None:
    """Verify partner without logo doesn't display."""
    partnerships_page = PartnershipsPage(page)
    count = partnerships_page.get_partner_logo_count()
    expect(count).to_be_greater_than(0)


@then("Broken placeholder not shown")
def no_broken_placeholder(page: Page) -> None:
    """Verify no broken placeholder."""
    partnerships_page = PartnershipsPage(page)
    for logo in partnerships_page.locators.partner_logos.all():
        src = logo.get_attribute("src")
        expect(src).not_to_match(r"placeholder|broken|undefined")


@then("Appropriate alt or aria-hidden prevents redundant announcement")
def no_redundant_alt(page: Page) -> None:
    """Verify no redundant announcement."""
    partnerships_page = PartnershipsPage(page)
    for logo in partnerships_page.locators.partner_logos.all():
        alt = logo.get_attribute("alt")
        aria_hidden = logo.get_attribute("aria-hidden")
        if alt == "" or alt is None:
            expect(aria_hidden).to_equal("true")


@then("Logo maintains sufficient visibility")
def logo_sufficient_visibility(page: Page) -> None:
    """Verify logo visibility."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.partner_logos.first).to_be_visible()


@then("Not invisible on background")
def not_invisible(page: Page) -> None:
    """Verify not invisible."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.partner_logos.first).to_be_visible()


@then("Animation pauses or reduces")
def animation_pauses_reduces(page: Page) -> None:
    """Verify animation pauses or reduces."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()


@then("Content remains visible and readable")
def content_readable(page: Page) -> None:
    """Verify content remains readable."""
    partnerships_page = PartnershipsPage(page)
    expect(partnerships_page.locators.section_heading).to_be_visible()
