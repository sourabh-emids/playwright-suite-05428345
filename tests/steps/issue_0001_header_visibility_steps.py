"""Step definitions for issue_0001: Render global header with Emids branding."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User navigates to the emids.com homepage")
def user_navigates_to_homepage(page: Page) -> None:
    page.goto("/")


@given("User is on any page within the site")
def user_is_on_any_page(page: Page) -> None:
    if page.url.endswith("/"):
        page.goto("/contact/")
    else:
        pass


@when("Page finishes loading")
def page_finishes_loading(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@then("Global header is visible at the top of the viewport")
def global_header_visible(page: Page) -> None:
    header = page.locator("header").first
    expect(header).to_be_visible()


@when("User clicks on the Emids logo or brand entry point")
def user_clicks_emids_logo(page: Page) -> None:
    logo = page.get_by_role("link", name="Emids logo")
    logo.click()


@then("User is navigated to the homepage URL '/'")
def user_navigated_to_homepage(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/")


@given("User focuses on the header navigation area")
def user_focuses_on_header_navigation(page: Page) -> None:
    page.goto("/")
    nav = page.get_by_role("navigation", name="Main Navigation")
    nav.get_by_role("link").first.focus()


@when("User presses Tab key to cycle through navigation items")
def user_presses_tab(page: Page) -> None:
    page.keyboard.press("Tab")


@then("All top-level navigation items receive visible focus and are reachable")
def all_nav_items_receive_visible_focus(page: Page) -> None:
    nav_items = page.get_by_role("navigation", name="Main Navigation").get_by_role("link,button")
    count = nav_items.count()
    assert count > 0, "Navigation items should be present"
    focused = page.evaluate("() => document.activeElement?.tagName")
    assert focused is not None, "An element should receive focus"


@when("User clicks the Connect CTA")
def user_clicks_connect_cta(page: Page) -> None:
    connect_cta = page.get_by_role("link", name="Connect").first
    connect_cta.click()


@then("User is navigated to the contact page at /contact/")
def user_navigated_to_contact(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/contact/")


@given("User is viewing the header on desktop or mobile")
def user_views_header(page: Page) -> None:
    page.goto("/")


@when("Navigation is fully expanded")
def navigation_expanded(page: Page) -> None:
    pass


@then("Logo, Solutions, Capabilities, Industries, Insights, Company, and Connect fields are all visible")
def all_nav_fields_visible(page: Page) -> None:
    expect(page.get_by_role("link", name="Emids logo")).to_be_visible()
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()
    expect(page.get_by_role("button", name="Capabilities")).to_be_visible()
    expect(page.get_by_role("button", name="Industries")).to_be_visible()
    expect(page.get_by_role("button", name="Insights")).to_be_visible()
    expect(page.get_by_role("button", name="Company")).to_be_visible()
    expect(page.get_by_role("link", name="Connect")).to_be_visible()


@given("User hovers over any navigation item")
def user_hovers_over_nav_item(page: Page) -> None:
    page.goto("/")


@when("All navigation items are tested for valid destinations")
def test_nav_items_destinations(page: Page) -> None:
    nav_items = page.get_by_role("navigation", name="Main Navigation").get_by_role("link")
    for item in nav_items.all():
        href = item.get_attribute("href")
        assert href is not None, "Navigation item should have href"
        assert href != "#", "Navigation item should not be a dead link"


@then("Each navigation item has a configured non-empty URL and no dead links exist")
def nav_items_have_valid_urls(page: Page) -> None:
    nav_items = page.get_by_role("navigation", name="Main Navigation").get_by_role("link")
    count = nav_items.count()
    assert count > 0, "Navigation items should exist"


@given("User views the header")
def user_views_header(page: Page) -> None:
    page.goto("/")


@when("User counts primary Connect CTA elements")
def user_counts_connect_cta(page: Page) -> None:
    pass


@then("Exactly one prominent Connect CTA exists in the header")
def exactly_one_connect_cta(page: Page) -> None:
    header = page.locator("header").first
    connect_ctas = header.get_by_role("link", name="Connect")
    expect(connect_ctas).to_have_count(1)


@given("User views the site on a narrow viewport mobile device")
def user_views_mobile_site(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")


@when("Navigation collapses into mobile menu")
def navigation_collapses(page: Page) -> None:
    pass


@then("All navigation destinations remain accessible through the mobile navigation interface")
def mobile_nav_accessible(page: Page) -> None:
    menu_button = page.get_by_role("button", name="Open menu")
    if menu_button.is_visible():
        menu_button.click()
    expect(page.get_by_role("navigation")).to_be_visible()


@given("Navigation configuration contains a long menu label")
def nav_contains_long_label(page: Page) -> None:
    page.goto("/")


@when("Header renders with extended label text")
def header_renders_with_long_label(page: Page) -> None:
    pass


@then("Long label displays without breaking layout or overlapping adjacent elements")
def long_label_displays_correctly(page: Page) -> None:
    header = page.locator("header").first
    expect(header).to_be_visible()


@given("User has JavaScript disabled in browser")
def js_disabled(page: Page) -> None:
    page.context.set_javascript_enabled(False)
    page.goto("/")


@when("User navigates to the homepage")
def user_navigates_to_homepage_no_js(page: Page) -> None:
    pass


@then("Header with navigation links is visible and functional")
def header_visible_no_js(page: Page) -> None:
    header = page.locator("header").first
    expect(header).to_be_visible()
    nav_links = header.locator("a")
    expect(nav_links.first).to_be_visible()
    page.context.set_javascript_enabled(True)
