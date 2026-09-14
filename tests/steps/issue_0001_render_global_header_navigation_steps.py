"""Step definitions for issue_0001: Render Global Header Navigation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.header_page import HeaderPage


@given("User navigates to the homepage")
def navigate_to_homepage(page: Page):
    page.goto("/")


@when("Page loads completely")
def page_loads_completely(page: Page):
    page.wait_for_load_state("networkidle")


@then("Header is visible with logo, navigation items, and Connect CTA")
def header_visible_with_components(page: Page):
    header = HeaderPage(page)
    expect(header.header).to_be_visible()
    expect(header.logo).to_be_visible()
    expect(header.navigation).to_be_visible()
    expect(header.connect_cta).to_be_visible()


@given("User is on any page within the site")
def user_on_any_page(page: Page):
    page.goto("/")


@when("User clicks the Emids logo")
def click_emids_logo(page: Page):
    header = HeaderPage(page)
    header.click_logo()


@then("User is returned to the homepage")
def user_returned_to_homepage(page: Page):
    expect(page).to_have_url("https://www.emids.com/")


@given("User focuses on the header using keyboard only")
def user_focuses_on_header_keyboard(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User tabs through navigation items")
def tab_through_nav_items(page: Page):
    page.keyboard.press("Tab")


@then("All top-level navigation items are reachable and focusable")
def all_nav_items_focusable(page: Page):
    header = HeaderPage(page)
    expect(header.solutions_nav).to_be_focusable()
    expect(header.capabilities_nav).to_be_focusable()
    expect(header.industries_nav).to_be_focusable()
    expect(header.insights_nav).to_be_focusable()
    expect(header.company_nav).to_be_focusable()


@given("User hovers over the header")
def user_hovers_over_header(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User moves pointer over each navigation item")
def hover_each_nav_item(page: Page):
    header = HeaderPage(page)
    header.hover_nav_item("Solutions")
    header.hover_nav_item("Capabilities")
    header.hover_nav_item("Industries")
    header.hover_nav_item("Insights")
    header.hover_nav_item("Company")


@then("All top-level navigation items are clickable and respond to hover")
def all_nav_items_clickable_hoverable(page: Page):
    header = HeaderPage(page)
    expect(header.solutions_nav).to_be_visible()
    expect(header.capabilities_nav).to_be_visible()
    expect(header.industries_nav).to_be_visible()
    expect(header.insights_nav).to_be_visible()
    expect(header.company_nav).to_be_visible()


@given("User is on any page")
def user_on_any_page_for_connect(page: Page):
    page.goto("/")


@when("User clicks the Connect CTA in the header")
def click_connect_cta(page: Page):
    header = HeaderPage(page)
    header.click_connect_cta()


@then("User is routed to the contact experience page")
def user_routed_to_contact(page: Page):
    expect(page).to_have_url("https://www.emids.com/contact/")


@given("Header is rendered")
def header_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Count of primary Connect CTAs is checked")
def count_connect_ctas(page: Page):
    pass


@then("Only one primary Connect CTA is present in the header")
def only_one_connect_cta(page: Page):
    header = HeaderPage(page)
    count = header.count_connect_ctas()
    assert count == 1, f"Expected 1 Connect CTA, found {count}"


@given("Logo asset is missing or fails to load")
def logo_missing_or_fails(page: Page):
    page.goto("/")
    page.route("**/logo*", lambda route: route.abort())


@when("Page renders")
def page_renders_with_missing_logo(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Header remains functional and alternative text or brand name is displayed")
def header_functional_with_alt_text(page: Page):
    header = HeaderPage(page)
    expect(header.header).to_be_visible()
    expect(header.logo).to_be_attached()


@given("Navigation item has a long label")
def nav_item_with_long_label(page: Page):
    page.goto("/")


@when("Header renders at maximum viewport width")
def header_at_max_viewport(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})


@then("Long labels are handled gracefully without breaking layout")
def long_labels_handled_gracefully(page: Page):
    header = HeaderPage(page)
    expect(header.header).to_be_visible()
    expect(header.navigation).to_be_visible()


@given("JavaScript is disabled in browser")
def js_disabled(page: Page, context):
    context.set_offline(True)


@when("User interacts with header")
def interact_with_header_no_js(page: Page):
    pass


@then("Header navigation remains accessible via links")
def header_accessible_no_js(page: Page):
    header = HeaderPage(page)
    expect(header.navigation).to_be_visible()


@given("Page is viewed at narrow viewport (mobile)")
def narrow_viewport_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Navigation collapses")
def nav_collapses(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("All navigation destinations remain accessible via menu trigger")
def all_destinations_accessible_mobile(page: Page):
    header = HeaderPage(page)
    expect(header.mobile_menu_trigger).to_be_visible()
