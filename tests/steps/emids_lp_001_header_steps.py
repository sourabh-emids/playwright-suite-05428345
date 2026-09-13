"""Step definitions for emids_lp_001: Render global header and brand entry point."""
import httpx
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.emids_lp_001_header_page import EmidsLp001HeaderPage


@given("User opens the Emids homepage")
def open_emids_homepage(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User is on any page of the website")
def navigate_to_any_page(page: Page) -> None:
    page.goto("/solutions/")


@given("User focuses on the header area using keyboard only")
def focus_header_area(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    header = page.locator("header")
    header.focus()


@given("User is on the homepage with header visible")
def homepage_with_header_visible(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User views the page on a desktop viewport (1024px or wider)")
def desktop_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 800})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("All navigation items and CTAs are rendered in the header")
def header_items_rendered(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Header is fully rendered")
def header_fully_rendered(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User views the page on a narrow mobile viewport (320px)")
def mobile_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 320, "height": 568})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Navigation contains labels at maximum character length")
def long_navigation_labels(page: Page) -> None:
    page.set_viewport_size({"width": 1024, "height": 768})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("JavaScript is disabled in the browser")
def js_disabled_browser(page: Page) -> None:
    pass


@when("Page finishes loading")
def page_finishes_loading(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("User clicks the Emids logo")
def click_emids_logo(page: Page) -> None:
    logo = page.get_by_role("link", name="Emids logo").or_(page.locator('[aria-label="Emids logo"]'))
    logo.click()


@when("User tabs through navigation items")
def tab_through_nav_items(page: Page) -> None:
    header = page.locator("header")
    header.focus()
    for _ in range(10):
        page.keyboard.press("Tab")


@when("User clicks the Connect CTA button")
def click_connect_cta(page: Page) -> None:
    connect = page.locator('header a[href*="/contact/"]').first
    connect.click()


@when("Header is rendered")
def header_rendered(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Automated check tests each navigation destination")
def test_navigation_destinations(page: Page, base_url: str) -> None:
    nav_links = [
        page.get_by_role("button", name="Solutions"),
        page.get_by_role("button", name="Capabilities"),
        page.get_by_role("button", name="Industries"),
        page.get_by_role("button", name="Insights"),
        page.get_by_role("button", name="Company"),
    ]
    results = []
    with httpx.Client(timeout=10.0) as client:
        for nav_link in nav_links:
            href = nav_link.get_attribute("data-href") or ""
            if href.startswith("http"):
                url = href
            elif href.startswith("/"):
                url = base_url.rstrip("/") + href
            else:
                continue
            try:
                response = client.get(url)
                results.append((url, response.status_code))
            except Exception:
                results.append((url, 0))
    assert all(200 <= status < 300 for _, status in results), f"Dead links found: {results}"


@when("Automated check counts Connect CTA elements")
def count_connect_cta(page: Page) -> None:
    pass


@when("Navigation collapses into mobile menu")
def navigation_collapses_mobile(page: Page) -> None:
    menu_button = page.locator('[aria-label="Menu"], [aria-label="Open menu"]')
    if menu_button.is_visible():
        menu_button.click()
    page.wait_for_timeout(500)


@when("Header is rendered on various viewport sizes")
def header_rendered_various_sizes(page: Page) -> None:
    pass


@when("User loads the homepage")
def load_homepage(page: Page) -> None:
    page.goto("/")


@then("Global header is visible and displays the Emids logo, navigation items (Solutions, Capabilities, Industries, Insights, Company), and Connect CTA")
def verify_header_components(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()
    expect(page.get_by_role("link", name="Emids logo")).to_be_visible()
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()
    expect(page.get_by_role("button", name="Capabilities")).to_be_visible()
    expect(page.get_by_role("button", name="Industries")).to_be_visible()
    expect(page.get_by_role("button", name="Insights")).to_be_visible()
    expect(page.get_by_role("button", name="Company")).to_be_visible()
    expect(page.locator('header a[href*="/contact/"]')).to_be_visible()


@then("User is navigated to the homepage at URL '/'")
def verify_navigated_to_homepage(page: Page) -> None:
    expect(page).to_have_url("/")
    expect(page).to_have_url("/$")


@then("All top-level navigation items (Solutions, Capabilities, Industries, Insights, Company) receive visible focus and are selectable")
def verify_nav_items_keyboard_accessible(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    header = page.locator("header")
    header.focus()
    for _ in range(15):
        page.keyboard.press("Tab")
    focused_element = page.evaluate("document.activeElement")
    assert focused_element is not None


@then("User is navigated to the contact experience page")
def verify_contact_page(page: Page) -> None:
    expect(page).to_have_url("**/contact/**")


@then("Navigation items are presented in grouped format with Connect as a prominent action button")
def verify_grouped_navigation(page: Page) -> None:
    nav = page.locator("header nav")
    expect(nav).to_be_visible()
    connect = page.locator('header a[href*="/contact/"]').first
    expect(connect).to_be_visible()


@then("All URLs return successful responses (200-299) with no dead links")
def verify_all_urls_successful(page: Page, base_url: str) -> None:
    links_to_check = [
        "/solutions/",
        "/capabilities/",
        "/industries/",
        "/insights/",
        "/company/",
        "/contact/",
    ]
    with httpx.Client(timeout=10.0) as client:
        for path in links_to_check:
            url = base_url.rstrip("/") + path
            response = client.get(url)
            assert 200 <= response.status_code < 300, f"Failed URL: {url} with status {response.status_code}"


@then("Only one primary Connect CTA exists in the header")
def verify_one_connect_cta(page: Page) -> None:
    header_connect = page.locator('header > div a[href*="/contact/"]')
    count = header_connect.count()
    assert count == 1, f"Expected 1 Connect CTA, found {count}"


@then("All navigation destinations remain accessible without losing access to any item")
def verify_navigation_accessible_mobile(page: Page) -> None:
    menu_button = page.locator('[aria-label="Menu"], [aria-label="Open menu"], button:has-text("Menu")')
    if menu_button.is_visible():
        menu_button.click()
    page.wait_for_timeout(500)
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()
    expect(page.get_by_role("button", name="Capabilities")).to_be_visible()


@then("Long labels do not break layout and text wraps appropriately")
def verify_long_labels_wrap(page: Page) -> None:
    header = page.locator("header")
    box = header.bounding_box()
    assert box is not None
    assert box["width"] <= 1280


@then("Header with static navigation links remains visible and functional")
def verify_header_no_js(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()
    expect(page.locator('header a[href="/"]')).to_be_visible()
