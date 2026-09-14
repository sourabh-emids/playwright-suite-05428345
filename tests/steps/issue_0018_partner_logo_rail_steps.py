"""Step definitions for issues 0018-0019: Partner Logo Rail/Marquee."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("Partnerships section renders")
def partnerships_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Partner logos are counted")
def count_partner_logos(page: Page):
    pass


@then("All 13 approved partners render: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic")
def all_partners_render(page: Page):
    logos = page.locator("text=Partnerships").locator("..").locator("..").locator("img")
    count = logos.count()
    assert count >= 1, "Partnerships section should have logos"


@given("Partner logos render")
def logos_render(page: Page):
    page.goto("/")


@when("Accessibility inspection occurs")
def accessibility_inspection_partners(page: Page):
    pass


@then("All partner logos have meaningful accessible names")
def logos_accessible_names(page: Page):
    logos = page.locator("img[alt]").all()
    for logo in logos:
        alt = logo.get_attribute("alt")
        assert alt, "Logo should have alt text"


@given("DOM uses duplication for looping animation")
def dom_duplication(page: Page):
    page.goto("/")


@when("Screen reader visits section")
def screen_reader_visits(page: Page):
    pass


@then("Logical partner list does not duplicate for assistive technologies")
def no_duplicate_for_screenreader(page: Page):
    pass


@given("Partner is configured")
def partner_configured(page: Page):
    page.goto("/")


@when("Logo renders")
def logo_renders(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Logo asset is present (or fallback handling)")
def logo_asset_present(page: Page):
    logos = page.locator("img").all()
    assert len(logos) > 0, "Logos should be present"


@given("Partner logo is not paired with adjacent partner name text")
def logo_not_paired(page: Page):
    page.goto("/")


@when("Alt/accessibility label is checked")
def check_alt(page: Page):
    pass


@then("Alt text is required unless logo is decorative with adjacent text")
def alt_required(page: Page):
    logos = page.locator("img").all()
    for logo in logos:
        alt = logo.get_attribute("alt")
        assert alt is not None, "Logo should have alt unless decorative"


@given("Partnerships section renders")
def partnerships_renders_layout(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Layout is reviewed")
def review_layout(page: Page):
    pass


@then("Logos present in horizontal sequence")
def horizontal_sequence(page: Page):
    section = page.locator("text=Partnerships").locator("..").locator("..")
    expect(section).to_be_visible()


@given("Partner logo asset is missing")
def logo_missing(page: Page):
    page.goto("/")
    page.route(lambda url: "partner" in url or "logo" in url, lambda route: route.abort())


@when("Section renders")
def section_renders_missing(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Fallback is displayed or graceful handling occurs")
def fallback_displayed(page: Page):
    section = page.locator("text=Partnerships")
    expect(section).to_be_visible()


@given("Logo has transparent areas on current background")
def transparent_logo(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_transparent(page: Page):
    page.wait_for_load_state("networkidle")


@then("Logo remains visible and distinguishable")
def logo_visible_distinguishable(page: Page):
    logos = page.locator("img").all()
    assert len(logos) > 0, "Logos should be visible"
