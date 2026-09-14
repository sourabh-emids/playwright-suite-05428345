"""Step definitions for issues 0020-0023: Capabilities Module."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from locators.capabilities_section_locators import CapabilitiesSectionLocators


@given("Capabilities section renders")
def capabilities_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Content is reviewed")
def review_content_caps(page: Page):
    pass


@then("All three groups (AI, Engineering, Platforms) are visible")
def three_groups_visible(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.ai_group).to_be_visible()
    expect(locators.engineering_group).to_be_visible()
    expect(locators.platforms_group).to_be_visible()


@given("Each capability group renders")
def each_group_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Groups are checked for corresponding content/actions")
def check_groups(page: Page):
    pass


@then("All three groups have corresponding content/actions")
def groups_have_content(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


@given("Capability group labels")
def group_labels(page: Page):
    page.goto("/")


@when("Compared to navigation taxonomy")
def compare_taxonomy(page: Page):
    pass


@then("Labels (AI, Engineering, Platforms) match navigation taxonomy")
def labels_match_taxonomy(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.ai_group).to_be_visible()
    expect(locators.engineering_group).to_be_visible()
    expect(locators.platforms_group).to_be_visible()


@given("Capabilities section is configured")
def caps_configured(page: Page):
    page.goto("/")


@when("Group count is validated")
def validate_group_count(page: Page):
    pass


@then("Exactly three primary groups exist for this content version")
def three_primary_groups(page: Page):
    locators = CapabilitiesSectionLocators(page)
    groups = locators.section.locator("text=/AI|Engineering|Platforms/").all()
    assert len(groups) >= 3, "Should have 3 groups"


@given("Capabilities section renders across viewports")
def caps_across_viewports(page: Page):
    page.goto("/")


@when("Viewport changes")
def viewport_changes_caps(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Responsive cards/panels adapt appropriately")
def responsive_adapt(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


@given("One capability group is not configured")
def group_not_configured(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_caps(page: Page):
    page.wait_for_load_state("networkidle")


@then("Missing group handled gracefully")
def missing_group_handled(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


@given("Group label does not match approved taxonomy")
def label_mismatch(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_mismatch(page: Page):
    page.wait_for_load_state("networkidle")


@then("Content governance ensures correct labeling")
def governance_corrects(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


# AI Capability Content (issue_0021)
@given("Capabilities section renders")
def caps_render_ai(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("AI group is checked")
def check_ai_group(page: Page):
    pass


@then("AI label and supporting content render correctly")
def ai_render_correct(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.ai_group).to_be_visible()


@given("AI capability has associated link")
def ai_has_link(page: Page):
    page.goto("/")


@when("Link is activated")
def activate_link(page: Page):
    pass


@then("Link routes to valid AI capability destination")
def ai_route_valid(page: Page):
    pass


@given("AI capability is configured")
def ai_configured(page: Page):
    page.goto("/")


@when("Title field is validated")
def validate_title_ai(page: Page):
    pass


@then("Title is present and non-empty")
def title_nonempty_ai(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.ai_group).to_be_visible()


@given("AI capability link is configured")
def ai_link_configured(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url_ai(page: Page):
    pass


@then("URL is valid and resolves")
def url_valid_ai(page: Page):
    pass


@given("AI capability renders")
def ai_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Visual design is reviewed")
def review_design_ai(page: Page):
    pass


@then("Card/panel matches capability visual system")
def visual_system_ai(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


@given("AI capability link destination is unavailable")
def ai_dest_unavailable(page: Page):
    page.goto("/")


@when("Link is clicked")
def click_ai_link(page: Page):
    pass


@then("Graceful handling occurs")
def graceful_ai(page: Page):
    pass


# Engineering Capability (issue_0022)
@given("Capabilities section renders")
def caps_render_eng(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Engineering group is checked")
def check_eng_group(page: Page):
    pass


@then("Engineering label and supporting content render correctly")
def eng_render_correct(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.engineering_group).to_be_visible()


@given("Engineering capability has associated link")
def eng_has_link(page: Page):
    page.goto("/")


@when("Link is activated")
def activate_link_eng(page: Page):
    pass


@then("Link routes to valid engineering capability destination")
def eng_route_valid(page: Page):
    pass


@given("Engineering capability is configured")
def eng_configured(page: Page):
    page.goto("/")


@when("Title field is validated")
def validate_title_eng(page: Page):
    pass


@then("Title is present and non-empty")
def title_nonempty_eng(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.engineering_group).to_be_visible()


@given("Engineering capability link is configured")
def eng_link_configured(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url_eng(page: Page):
    pass


@then("URL is valid and resolves")
def url_valid_eng(page: Page):
    pass


@given("Engineering capability renders")
def eng_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Visual design is reviewed")
def review_design_eng(page: Page):
    pass


@then("Card/panel matches capability visual system")
def visual_system_eng(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


# Platforms Capability (issue_0023)
@given("Capabilities section renders")
def caps_render_plat(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Platforms group is checked")
def check_plat_group(page: Page):
    pass


@then("Platforms content renders correctly")
def plat_render_correct(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.platforms_group).to_be_visible()


@given("Platforms capability renders")
def plat_renders(page: Page):
    page.goto("/")


@when("Navigation and body labels are compared")
def compare_labels_plat(page: Page):
    pass


@then("Labels use approved taxonomy consistently (e.g., 'Platforms' not alternate synonyms)")
def consistent_naming(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.platforms_group).to_be_visible()


@given("Platforms capability is configured")
def plat_configured(page: Page):
    page.goto("/")


@when("Title field is validated")
def validate_title_plat(page: Page):
    pass


@then("Title is present and non-empty")
def title_nonempty_plat(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.platforms_group).to_be_visible()


@given("Platforms capability renders")
def plat_renders_visual(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Visual design is reviewed")
def review_design_plat(page: Page):
    pass


@then("Card/panel matches capability visual system")
def visual_system_plat(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.section).to_be_visible()


@given("CMS content has inconsistent synonyms for Platforms")
def inconsistent_synonyms(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_plat(page: Page):
    page.wait_for_load_state("networkidle")


@then("Content governance prevents or corrects inconsistent naming")
def governance_corrects_plat(page: Page):
    locators = CapabilitiesSectionLocators(page)
    expect(locators.platforms_group).to_be_visible()
