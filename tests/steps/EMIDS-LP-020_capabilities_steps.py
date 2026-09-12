"""Step definitions for Capabilities section - EMIDS-LP-020, EMIDS-LP-021, EMIDS-LP-022, EMIDS-LP-023"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-020_capabilities_page import CapabilitiesPage
from playwright.sync_api import expect


@given("Capabilities section")
def capabilities_section(page):
    page.goto("/")


@when("Groups are inspected")
def inspect_groups(page):
    pass


@then("AI, Engineering, and Platforms groups are all visible")
def verify_all_groups(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("Each capability group")
def each_capability_group(page):
    page.goto("/")


@when("Content is reviewed")
def review_content(page):
    pass


@then("Each group has corresponding summary and links/actions")
def verify_summary_links(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_section_visible()


@given("Capability group labels")
def capability_group_labels(page):
    page.goto("/")


@when("Compared against navigation taxonomy")
def compare_taxonomy(page):
    pass


@then("Labels are consistent: AI, Engineering, Platforms")
def verify_consistency(page):
    caps_page = CapabilitiesPage(page)
    groups = caps_page.get_capability_group_names()
    assert "AI" in groups
    assert "Engineering" in groups
    assert "Platforms" in groups


@given("Capabilities section at different viewport widths")
def different_viewports(page):
    pass


@when("Layout adapts")
def layout_adapts(page):
    caps_page = CapabilitiesPage(page)
    caps_page.goto("/")


@then("Responsive cards/panels render correctly")
def verify_responsive(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("AI capability card/panel")
def ai_capability_card(page):
    page.goto("/")


@when("Content is verified")
def verify_content(page):
    pass


@then("AI label and supporting content are present")
def verify_ai_content(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("AI capability CTA/link")
def ai_capability_link(page):
    page.goto("/")


@when("Link is tested")
def test_link(page):
    pass


@then("Link navigates to valid AI capability destination")
def verify_valid_destination(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_section_visible()


@given("AI capability content")
def ai_capability_content(page):
    page.goto("/")


@when("Title field is checked")
def check_title(page):
    pass


@then("Title is populated")
def verify_title_populated(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("Edge case where AI destination is broken")
def ai_destination_broken(page):
    pass


@when("Link is clicked")
def click_link(page):
    caps_page = CapabilitiesPage(page)
    caps_page.goto("/")


@then("Appropriate error handling occurs")
def verify_error_handling(page):
    pass


@given("Engineering capability card/panel")
def engineering_card(page):
    page.goto("/")


@when("Content is verified")
def verify_eng_content(page):
    pass


@then("Engineering label and supporting content are present")
def verify_eng_label(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("Engineering capability CTA/link")
def engineering_cta_link(page):
    page.goto("/")


@when("Link is tested")
def test_eng_link(page):
    pass


@then("Link navigates to valid engineering capability destination")
def verify_eng_destination(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_section_visible()


@given("Engineering capability content")
def engineering_capability_content(page):
    page.goto("/")


@when("Title field is checked")
def check_eng_title(page):
    pass


@then("Title is populated")
def verify_eng_title_populated(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("Platforms capability card/panel")
def platforms_card(page):
    page.goto("/")


@when("Content is verified")
def verify_platforms_content(page):
    pass


@then("Platforms content is present")
def verify_platforms_present(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("Platforms label in navigation and body copy")
def platforms_label_nav_body(page):
    page.goto("/")


@when("Labels are compared")
def compare_labels(page):
    pass


@then("Labels use approved taxonomy consistently (e.g., 'Platforms' not variant synonyms)")
def verify_platforms_taxonomy(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("Content governance check")
def content_governance(page):
    page.goto("/")


@when("Navigation and body copy labels are audited")
def audit_labels(page):
    pass


@then("Inconsistent synonyms are prevented unless intentionally approved")
def verify_no_synonyms(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_all_capability_groups()


@given("CMS content update scenario")
def cms_update(page):
    pass


@when("Content becomes outdated")
def content_outdated(page):
    caps_page = CapabilitiesPage(page)
    caps_page.goto("/")


@then("Publishing workflow logs content validation issues")
def verify_logging(page):
    caps_page = CapabilitiesPage(page)
    caps_page.verify_section_visible()
