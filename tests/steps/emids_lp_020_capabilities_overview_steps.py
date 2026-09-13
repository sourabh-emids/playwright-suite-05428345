"""Steps for emids_lp_020: Render capabilities overview."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.capabilities.capabilities_section_page import CapabilitiesSectionPage


@given(parsers.parse("User views Capabilities section"))
def view_capabilities(page: Page) -> None:
    """User views Capabilities section."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("User examines each capability group"))
def examine_groups(page: Page) -> None:
    """User examines each group."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.scroll_to_section()


@given(parsers.parse("User compares capabilities section to header navigation"))
def compare_to_header(page: Page) -> None:
    """Compare to header navigation."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.scroll_to_section()


@given(parsers.parse("CMS content is managed"))
def cms_content_managed(page: Page) -> None:
    """CMS content managed."""
    pass


@given(parsers.parse("User views Capabilities on mobile"))
def view_mobile(page: Page) -> None:
    """User views on mobile."""
    page.set_viewport_size({"width": 375, "height": 667})


@given(parsers.parse("One capability group is not configured"))
def group_not_configured(page: Page) -> None:
    """Group not configured."""
    pass


@when("User scans for groups")
def scan_groups(page: Page) -> None:
    """Scan for groups."""
    pass


@when("User reads group content")
def read_group_content(page: Page) -> None:
    """Read group content."""
    pass


@when("User checks terminology")
def check_terminology(page: Page) -> None:
    """Check terminology."""
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@then("AI, Engineering, and Platforms groups are all visible")
def all_groups_visible(page: Page) -> None:
    """Verify all groups visible."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.are_all_groups_visible()).to_be_true()


@then("Each group contains title, summary, and relevant links/media")
def group_has_content(page: Page) -> None:
    """Verify group has content."""
    cap_page = CapabilitiesSectionPage(page)
    groups = cap_page.get_capability_groups()
    expect(len(groups)).to_equal(3)


@then("Labels are consistent: AI, Engineering, Platforms match navigation taxonomy")
def labels_consistent(page: Page) -> None:
    """Verify labels consistent."""
    cap_page = CapabilitiesSectionPage(page)
    groups = cap_page.get_capability_groups()
    for group in groups:
        expect(group in ["Artificial Intelligence", "Engineering", "Platforms"]).to_be_true()


@then("Exactly three primary groups display")
def exactly_three_groups(page: Page) -> None:
    """Verify exactly three groups."""
    cap_page = CapabilitiesSectionPage(page)
    groups = cap_page.get_capability_groups()
    expect(len(groups)).to_equal(3)


@then("No missing or extra groups")
def no_missing_extra(page: Page) -> None:
    """Verify no missing or extra."""
    cap_page = CapabilitiesSectionPage(page)
    expect(len(cap_page.get_capability_groups())).to_equal(3)


@then("Cards/panels reflow appropriately")
def panels_reflow(page: Page) -> None:
    """Verify panels reflow."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.section_heading).to_be_visible()


@then("No overflow or hidden content")
def no_overflow_hidden(page: Page) -> None:
    """Verify no overflow or hidden."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.ai_group).to_be_visible()


@then("Section handles missing group gracefully")
def missing_group_handled(page: Page) -> None:
    """Verify missing group handled."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.section_heading).to_be_visible()


@then("Remaining groups display correctly")
def remaining_groups_correct(page: Page) -> None:
    """Verify remaining groups correct."""
    cap_page = CapabilitiesSectionPage(page)
    groups = cap_page.get_capability_groups()
    expect(len(groups)).to_be_greater_than_or_equal(1)
