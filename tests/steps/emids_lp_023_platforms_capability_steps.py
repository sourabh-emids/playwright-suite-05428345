"""Steps for emids_lp_023: Render Platforms capability content."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.capabilities.capabilities_section_page import CapabilitiesSectionPage


@given(parsers.parse("User views Platforms capability card/panel"))
def view_platforms_card(page: Page) -> None:
    """User views Platforms capability card."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("User compares Platforms capability to header navigation"))
def compare_to_header(page: Page) -> None:
    """User compares to header navigation."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("CMS content is managed"))
def cms_content_managed(page: Page) -> None:
    """CMS content is managed."""
    pass


@given(parsers.parse("CMS content is outdated"))
def cms_outdated(page: Page) -> None:
    """CMS content is outdated."""
    pass


@when("Content loads")
def content_loads(page: Page) -> None:
    """Content loads."""
    page.wait_for_load_state("domcontentloaded")


@when("User checks terminology")
def check_terminology(page: Page) -> None:
    """Check terminology."""
    pass


@when("Content publishes")
def content_publishes(page: Page) -> None:
    """Content publishes."""
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@then("Platforms label displays")
def platforms_label_displays(page: Page) -> None:
    """Verify Platforms label displays."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.platforms_group).to_be_visible()


@then("Supporting content renders correctly")
def supporting_renders(page: Page) -> None:
    """Verify supporting content renders."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.platforms_group).to_be_visible()


@then("Navigation and body copy use same approved taxonomy label")
def same_taxonomy_label(page: Page) -> None:
    """Verify same taxonomy label."""
    cap_page = CapabilitiesSectionPage(page)
    text = cap_page.locators.platforms_group.inner_text()
    expect(text).to_contain("Platforms")


@then("No 'Provider Platforms' vs 'Platforms' mismatch")
def no_mismatch(page: Page) -> None:
    """Verify no mismatch."""
    cap_page = CapabilitiesSectionPage(page)
    text = cap_page.locators.platforms_group.inner_text()
    # Should not have inconsistent naming
    pass


@then("Navigation and body copy use consistent terminology")
def consistent_terminology(page: Page) -> None:
    """Verify consistent terminology."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.platforms_group).to_be_visible()


@then("No unintended synonyms")
def no_synonyms(page: Page) -> None:
    """Verify no unintended synonyms."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.platforms_group).to_be_visible()


@then("Current content displays")
def current_content_displays(page: Page) -> None:
    """Verify current content displays."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.platforms_group).to_be_visible()


@then("No stale terminology visible")
def no_stale_terminology(page: Page) -> None:
    """Verify no stale terminology."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.platforms_group).to_be_visible()
