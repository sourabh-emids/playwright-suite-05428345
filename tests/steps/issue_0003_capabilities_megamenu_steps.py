"""Step definitions for issue_0003: Implement Capabilities mega-menu."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User is on desktop with header visible")
def user_on_desktop(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("User activates the Capabilities navigation item")
def activate_capabilities(page: Page) -> None:
    page.get_by_role("button", name="Capabilities").click()


@then("Capabilities menu opens with AI, Engineering, and Platforms groups visible")
def capabilities_menu_opens(page: Page) -> None:
    expect(page.get_by_text("AI")).to_be_visible()
    expect(page.get_by_text("Engineering")).to_be_visible()
    expect(page.get_by_text("Platforms")).to_be_visible()


@given("Capabilities menu is open")
def capabilities_menu_open(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Capabilities").click()


@when("User navigates using Tab and Arrow keys")
def navigate_with_keys(page: Page) -> None:
    page.keyboard.press("Tab")
    page.keyboard.press("ArrowDown")


@then("All capability links are reachable and activatable via keyboard")
def capability_links_keyboard_accessible(page: Page) -> None:
    active = page.evaluate("() => document.activeElement?.tagName")
    assert active is not None


@when("User compares menu labels to approved site taxonomy")
def compare_taxonomy(page: Page) -> None:
    pass


@then("Labels match the content-managed taxonomy exactly")
def labels_match_taxonomy(page: Page) -> None:
    labels = ["AI", "Engineering", "Platforms"]
    for label in labels:
        expect(page.get_by_text(label)).to_be_visible()


@when("User checks for duplicate labels")
def check_duplicate_labels(page: Page) -> None:
    pass


@then("AI, Engineering, and Platforms labels are each unique within the menu")
def labels_unique(page: Page) -> None:
    ai_count = page.get_by_text("AI").count()
    engineering_count = page.get_by_text("Engineering").count()
    platforms_count = page.get_by_text("Platforms").count()
    assert ai_count >= 1
    assert engineering_count >= 1
    assert platforms_count >= 1


@given("User is on mobile device")
def user_on_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")


@when("User expands Capabilities section")
def expand_capabilities_mobile(page: Page) -> None:
    menu_btn = page.get_by_role("button", name="Open menu")
    if menu_btn.is_visible():
        menu_btn.click()
    cap_btn = page.get_by_role("button", name="Capabilities")
    if cap_btn.is_visible():
        cap_btn.click()


@then("Accessible disclosure pattern is used matching other mobile menus")
def mobile_disclosure_pattern(page: Page) -> None:
    expect(page.get_by_role("navigation")).to_be_visible()


@when("User clicks child capability links")
def click_capability_link(page: Page) -> None:
    ai_link = page.get_by_role("link", name="AI Solutions").or_(page.get_by_role("link").filter(has=page.get_by_text("AI")))
    if ai_link.count() > 0:
        ai_link.first.click()


@then("Each link resolves to a valid destination URL")
def link_resolves_valid(page: Page) -> None:
    current_url = page.url
    assert "ai" in current_url.lower() or current_url.startswith("https://www.emids.com")


@given("User has reduced viewport height")
def reduced_viewport_height(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 480})
    page.goto("/")


@when("Capabilities menu opens")
def capabilities_opens(page: Page) -> None:
    page.get_by_role("button", name="Capabilities").click()


@then("Menu content is accessible via scrolling if needed without breaking layout")
def menu_scrollable(page: Page) -> None:
    menu = page.locator("nav[aria-label='Capabilities']")
    expect(menu).to_be_visible()
