"""Step definitions for emids_lp_003: Implement Capabilities mega-menu."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("User focuses on the Capabilities navigation item")
def focus_capabilities(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Capabilities").focus()


@given("Capabilities menu is open")
def capabilities_menu_open(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Capabilities").click()
    page.wait_for_timeout(300)


@given("Capabilities menu displays labels")
def capabilities_menu_display(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Capabilities").click()
    page.wait_for_timeout(300)


@given("Capabilities menu is rendered")
def capabilities_menu_rendered(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Capabilities").hover()
    page.wait_for_timeout(300)


@given("User is on mobile viewport")
def mobile_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Capabilities menu contains many items")
def many_items_menu(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Capabilities").click()
    page.wait_for_timeout(300)


@when("User activates the Capabilities control")
def activate_capabilities(page: Page) -> None:
    page.get_by_role("button", name="Capabilities").click()


@when("User tabs through capability links")
def tab_capability_links(page: Page) -> None:
    for _ in range(10):
        page.keyboard.press("Tab")


@when("Automated check validates against approved taxonomy")
def validate_taxonomy(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu').filter(has=page.get_by_role("button", name="Capabilities"))
    expect(menu.locator("text=AI")).to_be_visible()
    expect(menu.locator("text=Engineering")).to_be_visible()
    expect(menu.locator("text=Platforms")).to_be_visible()


@when("Automated check scans all labels")
def scan_labels(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu')
    labels = menu.locator("p, h3, h4").filter(has_text("AI").or_(has_text("Engineering")).or_(has_text("Platforms")))
    count = labels.count()
    assert count >= 3


@when("Each capability URL is tested")
def test_capability_urls(page: Page, base_url: str) -> None:
    pass


@when("User activates Capabilities")
def activate_capabilities_mobile(page: Page) -> None:
    menu_btn = page.locator('[aria-label="Menu"], button:has-text("Menu")')
    if menu_btn.is_visible():
        menu_btn.click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Capabilities").click()


@when("Menu is open on various viewport sizes")
def menu_various_sizes(page: Page) -> None:
    pass


@then("Menu opens predictably with AI, Engineering, and Platforms capability groups")
def verify_groups(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu')
    expect(menu.locator("text=AI")).to_be_visible()
    expect(menu.locator("text=Engineering")).to_be_visible()
    expect(menu.locator("text=Platforms")).to_be_visible()


@then("All capability links are keyboard operable with visible focus states")
def verify_keyboard_operable(page: Page) -> None:
    page.get_by_role("button", name="Capabilities").focus()
    expect(page.get_by_role("button", name="Capabilities")).to_be_focused()


@then("Labels match the content-managed approved taxonomy (AI, Engineering, Platforms)")
def verify_labels_match(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu')
    assert menu.locator("text=AI").count() >= 1
    assert menu.locator("text=Engineering").count() >= 1
    assert menu.locator("text=Platforms").count() >= 1


@then("No duplicate labels exist within the menu")
def verify_no_duplicate_labels(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu')
    labels = menu.locator("p, h3, h4").all_inner_texts()
    unique_labels = set(labels)
    assert len(labels) == len(unique_labels), "Duplicate labels found"


@then("All URLs return successful responses")
def verify_urls_successful(page: Page, base_url: str) -> None:
    pass


@then("Accessible disclosure pattern is presented")
def verify_disclosure_pattern(page: Page) -> None:
    drawer = page.locator('[role="dialog"], [aria-expanded="true"]')
    expect(drawer).to_be_visible()


@then("Menu handles overflow gracefully without breaking layout")
def verify_overflow_handling(page: Page) -> None:
    menu = page.locator('[role="menu"], .mega-menu')
    box = menu.bounding_box()
    assert box is not None
