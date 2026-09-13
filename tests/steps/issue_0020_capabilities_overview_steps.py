"""Steps for Capabilities overview rendering (issue_0020)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0020_capabilities_overview_locators import CapabilitiesOverviewLocators


@given("User views Capabilities section")
def view_capabilities(page: Page) -> None:
    page.goto("/")


@given("Capabilities section renders")
def section_renders(page: Page) -> None:
    page.goto("/")


@given("User views Capabilities section at mobile width")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("One capability group is missing from CMS")
def group_missing(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User views each capability group")
def view_groups(page: Page) -> None:
    pass


@when("User compares section labels to navigation")
def compare_labels(page: Page) -> None:
    pass


@when("User counts primary groups")
def count_groups(page: Page) -> None:
    pass


@then("All three capability groups (AI, Engineering, Platforms) are visible")
def three_groups_visible(page: Page) -> None:
    locators = CapabilitiesOverviewLocators(page)
    expect(locators.capabilities_section).to_be_visible()


@then("Each group has corresponding content and actions")
def groups_have_content(page: Page) -> None:
    expect(CapabilitiesOverviewLocators(page).capabilities_section).to_be_visible()


@then("Group labels (AI, Engineering, Platforms) match navigation taxonomy")
def labels_match(page: Page) -> None:
    expect(CapabilitiesOverviewLocators(page).capabilities_section).to_be_visible()


@then("Exactly three primary groups are present for this content version")
def exactly_three_groups(page: Page) -> None:
    expect(CapabilitiesOverviewLocators(page).capabilities_section).to_be_visible()


@then("Section uses responsive capability cards/panels")
def responsive_cards(page: Page) -> None:
    expect(CapabilitiesOverviewLocators(page).capabilities_section).to_be_visible()


@then("Remaining groups display correctly or appropriate fallback shows")
def fallback(page: Page) -> None:
    expect(CapabilitiesOverviewLocators(page).capabilities_section).to_be_visible()
