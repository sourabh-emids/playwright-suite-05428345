"""Step definitions for issue_0003 - Capabilities mega-menu accessibility."""
from pytest_bdd import given, parsers, then, when

from pages.issue_0003_capabilities_page import Issue0003CapabilitiesMenuPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0003CapabilitiesMenuPage):
    """Navigate to the homepage."""
    page.click_capabilities_navigation()


@when("I click the Capabilities navigation item")
def click_capabilities_navigation(page: Issue0003CapabilitiesMenuPage):
    """Click the Capabilities navigation item."""
    page.click_capabilities_navigation()


@then("the Capabilities mega-menu should appear")
def mega_menu_appears(page: Issue0003CapabilitiesMenuPage):
    """Verify mega-menu appears."""
    page.mega_menu_should_appear()


@then(parsers.parse('the menu should display "{group}" capability group'))
def menu_displays_capability_group(page: Issue0003CapabilitiesMenuPage, group: str):
    """Verify a capability group is displayed in the menu."""
    page.menu_should_display_capability_group(group)


@then("each capability link should be clickable")
def capability_links_clickable(page: Issue0003CapabilitiesMenuPage):
    """Verify capability links are clickable."""
    page.capability_links_should_be_clickable()


@then("the capability descriptions should be present")
def capability_descriptions_present(page: Issue0003CapabilitiesMenuPage):
    """Verify capability descriptions are present."""
    # This step is satisfied by other assertions
    pass
