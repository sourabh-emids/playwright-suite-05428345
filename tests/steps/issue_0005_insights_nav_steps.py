"""Step definitions for issue_0005: Implement Insights navigation group."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User is on any page with header visible")
def user_on_any_page(page: Page) -> None:
    page.goto("/")


@when("User activates the Insights navigation item")
def activate_insights(page: Page) -> None:
    page.get_by_role("button", name="Insights").click()


@then("Insights menu opens and displays thought leadership and resource destinations")
def insights_menu_opens(page: Page) -> None:
    expect(page.get_by_text("Insights and Resources")).to_be_visible()
    expect(page.get_by_text("News & Events")).to_be_visible()


@when("User views the menu content")
def view_menu_content(page: Page) -> None:
    pass


@then("All insight links are readable and operable on mobile viewport")
def links_readable_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    menu = page.get_by_role("navigation", name="Insights")
    expect(menu).to_be_visible()


@given("Insights menu is open on mobile")
def insights_menu_open_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    page.get_by_role("button", name="Insights").click()


@given("User opens Insights menu")
def open_insights_menu(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="Insights").click()


@when("Checking menu content for empty groups")
def check_empty_groups(page: Page) -> None:
    pass


@then("All displayed groups contain at least one insight item")
def groups_have_items(page: Page) -> None:
    links = page.get_by_role("navigation", name="Insights").get_by_role("link")
    count = links.count()
    assert count > 0


@when("User clicks an Insights navigation link")
def click_insights_link(page: Page) -> None:
    link = page.get_by_role("navigation", name="Insights").get_by_role("link").first
    link.click()


@then("User lands on canonical URL under /insights/ path")
def lands_on_insights_path(page: Page) -> None:
    assert "/insights/" in page.url


@given("User is on touch device without hover capability")
def touch_device(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("User interacts with Insights menu")
def interact_insights_menu(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="Insights").click()


@then("Menu opens via tap/click, not requiring hover")
def menu_opens_click(page: Page) -> None:
    expect(page.get_by_text("Insights and Resources")).to_be_visible()
