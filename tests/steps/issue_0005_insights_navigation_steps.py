"""Step definitions for issue_0005 - Insights navigation group accessibility."""
from pytest_bdd import given, parsers, then, when

from pages.issue_0005_insights_page import Issue0005InsightsMenuPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0005InsightsMenuPage):
    """Navigate to the homepage."""
    page.click_insights_navigation()


@when("I click the Insights navigation item")
def click_insights_navigation(page: Issue0005InsightsMenuPage):
    """Click the Insights navigation item."""
    page.click_insights_navigation()


@then("the Insights mega-menu should appear")
def mega_menu_appears(page: Issue0005InsightsMenuPage):
    """Verify mega-menu appears."""
    page.mega_menu_should_appear()


@then(parsers.parse('the menu should display "{header}"'))
def menu_displays_header(page: Issue0005InsightsMenuPage, header: str):
    """Verify a header is displayed in the menu."""
    page.menu_should_display_header(header)


@then("the Insights Hub link should be present")
def insights_hub_link_present(page: Issue0005InsightsMenuPage):
    """Verify Insights Hub link is present."""
    page.insights_hub_link_should_be_present()


@then("the Case Studies link should be present")
def case_studies_link_present(page: Issue0005InsightsMenuPage):
    """Verify Case Studies link is present."""
    page.case_studies_link_should_be_present()


@then("the eBooks & Guides link should be present")
def ebooks_guides_link_present(page: Issue0005InsightsMenuPage):
    """Verify eBooks & Guides link is present."""
    page.ebooks_guides_link_should_be_present()


@then("the Webinars link should be present")
def webinars_link_present(page: Issue0005InsightsMenuPage):
    """Verify Webinars link is present."""
    page.webinars_link_should_be_present()
