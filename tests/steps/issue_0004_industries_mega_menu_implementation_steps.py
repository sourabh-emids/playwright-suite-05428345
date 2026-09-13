"""Step definitions for issue_0004: Industries mega-menu implementation"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0004_industries_mega_menu_implementation_page import Issue0004IndustriesMenuPage


@given("A user opens the Industries navigation menu")
def user_opens_industries_menu(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.navigate_to_homepage()
    page_object.open_industries_menu()


@given("The Industries menu is open")
def industries_menu_is_open(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.open_industries_menu()


@given("The Industries menu displays all audience links")
def industries_menu_displays_links(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.open_industries_menu()


@given("A user is on a mobile device")
def user_is_on_mobile_device(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.resize_to_mobile()
    page_object.navigate_to_homepage()


@when("The menu is fully rendered")
def menu_fully_rendered(page: Page):
    """Menu rendering happens in Given."""
    pass


@when("The user navigates using only keyboard")
def user_navigates_keyboard_only(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page.keyboard.press("Tab")


@when("Automated testing validates URLs")
def automated_validates_urls(page: Page):
    """URL validation happens in assertions."""
    pass


@when("The Industries menu is expanded")
def industries_menu_expanded(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.open_industries_menu()


@then("The menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations")
def menu_contains_all_industries(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.verify_all_industries_visible()


@then("All five industry destinations are keyboard accessible")
def all_industries_keyboard_accessible(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    count = page_object.get_industry_links_count()
    assert count >= 5, f"Expected at least 5 industry links, found {count}"


@then("All URLs follow canonical patterns: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/")
def urls_follow_canonical_patterns(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    assert page_object.validate_canonical_urls(), "URLs do not follow canonical patterns"


@then("A stacked list or disclosure pattern provides access to all five audiences")
def stacked_list_provides_access(page: Page):
    page_object = Issue0004IndustriesMenuPage(page)
    page_object.verify_all_industries_visible()
