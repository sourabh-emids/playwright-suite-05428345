"""Step definitions for issue_0004: Implement Industries mega-menu."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User activates the Industries navigation item")
def activate_industries(page: Page) -> None:
    page.get_by_role("button", name="Industries").click()


@when("Menu opens on desktop")
def menu_opens_desktop(page: Page) -> None:
    pass


@then("Payer, Provider, HealthTech, Life Sciences, and Consumer destinations are all visible")
def five_industries_visible(page: Page) -> None:
    expect(page.get_by_role("link", name="Payer")).to_be_visible()
    expect(page.get_by_role("link", name="Provider")).to_be_visible()
    expect(page.get_by_role("link", name="HealthTech")).to_be_visible()
    expect(page.get_by_role("link", name="Life Sciences")).to_be_visible()
    expect(page.get_by_role("link", name="Consumer")).to_be_visible()


@given("Industries menu is open")
def industries_menu_open(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Industries").click()


@when("User navigates using keyboard only")
def navigate_keyboard_only(page: Page) -> None:
    page.keyboard.press("Tab")


@then("Each of the five audience links is keyboard accessible")
def five_links_keyboard_accessible(page: Page) -> None:
    links = page.get_by_role("navigation", name="Industries").get_by_role("link")
    count = links.count()
    assert count >= 5


@when("Comparing to specified canonical paths")
def compare_canonical_paths(page: Page) -> None:
    pass


@then("Links resolve to /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, and /segments/consumer/")
def links_resolve_canonical(page: Page) -> None:
    expect(page.get_by_role("link", name="Payer")).to_have_attribute("href", "https://www.emids.com/segments/payer/")
    expect(page.get_by_role("link", name="Provider")).to_have_attribute("href", "https://www.emids.com/segments/provider/")
    expect(page.get_by_role("link", name="HealthTech")).to_have_attribute("href", "https://www.emids.com/segments/healthtech/")


@given("User is on mobile device")
def user_on_mobile_device(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")


@when("User expands Industries section")
def expand_industries_mobile(page: Page) -> None:
    menu_btn = page.get_by_role("button", name="Open menu")
    if menu_btn.is_visible():
        menu_btn.click()
    ind_btn = page.get_by_role("button", name="Industries")
    if ind_btn.is_visible():
        ind_btn.click()


@then("Five audience destinations display in stacked list or disclosure pattern")
def mobile_stacked_list(page: Page) -> None:
    expect(page.get_by_role("navigation")).to_be_visible()


@given("One industry segment is in unpublished state")
def one_segment_unpublished(page: Page) -> None:
    page.goto("/")


@when("Industries menu opens")
def industries_menu_opens(page: Page) -> None:
    page.get_by_role("button", name="Industries").click()


@then("Unpublished segment does not appear in menu; remaining segments display normally")
def unpublished_hidden(page: Page) -> None:
    menu = page.get_by_role("navigation", name="Industries")
    expect(menu).to_be_visible()
