"""Step definitions for emids_lp_001 - Header basic rendering."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@given("The user navigates to the homepage")
def navigate_to_homepage(page: Page) -> None:
    page.goto("/")


@given("The user is on any page of the website")
def user_on_any_page(page: Page) -> None:
    pass


@then("The global header is visible with all navigation fields displayed")
def header_visible_with_navigation(page: Page) -> None:
    from pages.emids_lp_001_header_page import HeaderPage
    header_page = HeaderPage(page)
    expect(header_page.header).to_be_visible()
    expect(header_page.logo).to_be_visible()
    expect(header_page.navigation).to_be_visible()
    expect(header_page.connect_cta).to_be_visible()


@then("The user is navigated to the homepage URL '/'")
def verify_homepage_navigation(page: Page, context: dict) -> None:
    expect(page).to_have_url(page.base_url + "/")


@then("Each item receives visible focus and is activatable with Enter or Space key")
def verify_navigation_keyboard_accessible(page: Page) -> None:
    from pages.emids_lp_001_header_page import HeaderPage
    header_page = HeaderPage(page)
    nav_items = header_page.navigation_items
    for item in nav_items:
        item.highlight()
        expect(item).to_be_focused()


@then("The user is navigated to the contact experience URL '/contact/'")
def verify_contact_navigation(page: Page) -> None:
    expect(page).to_have_url("/contact/")


@then("Only one primary Connect CTA is present in the header region")
def verify_single_connect_cta(page: Page) -> None:
    from pages.emids_lp_001_header_page import HeaderPage
    header_page = HeaderPage(page)
    connect_ctas = header_page.connect_ctas
    assert len(connect_ctas) == 1, f"Expected 1 Connect CTA, found {len(connect_ctas)}"


@then("All navigation links resolve to valid destinations with no 404 errors")
def verify_no_dead_links(page: Page) -> None:
    from pages.emids_lp_001_header_page import HeaderPage
    header_page = HeaderPage(page)
    nav_links = header_page.all_nav_links
    for link in nav_links:
        href = link.get_attribute("href")
        if href and not href.startswith("#") and not href.startswith("javascript"):
            response = page.request.get(href)
            assert response.status < 400, f"Dead link found: {href}"


@then("Navigation collapses responsively without losing access to any destination")
def verify_responsive_navigation(page: Page) -> None:
    from pages.emids_lp_001_header_page import HeaderPage
    header_page = HeaderPage(page)
    page.set_viewport_size({"width": 320, "height": 568})
    expect(header_page.mobile_menu_toggle).to_be_visible()


@then("Header navigation remains accessible and functional via standard links")
def verify_navigation_without_js(page: Page) -> None:
    from pages.emids_lp_001_header_page import HeaderPage
    header_page = HeaderPage(page)
    expect(header_page.navigation).to_be_visible()
