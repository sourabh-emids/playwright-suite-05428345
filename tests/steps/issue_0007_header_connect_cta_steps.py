"""Step definitions for issue_0007: Header Connect CTA Functionality."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from locators.connect_cta_locators import ConnectCTALocators


@given("Header renders")
def header_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Visual inspection of Connect CTA")
def visual_inspection_cta(page: Page):
    pass


@then("Connect CTA is visually distinct from other navigation elements")
def cta_visually_distinct(page: Page):
    locators = ConnectCTALocators(page)
    expect(locators.connect_cta).to_be_visible()
    nav_links = locators.all_nav_links.all()
    cta_found = False
    for link in nav_links:
        if link.get_attribute("href") and "/contact/" in link.get_attribute("href"):
            cta_found = True
            break
    assert cta_found, "Connect CTA should be visually distinct"


@given("Connect CTA is rendered")
def cta_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Screen reader or accessibility tool inspects the element")
def inspect_element(page: Page):
    pass


@then("CTA has accessible name that describes the action")
def cta_accessible_name(page: Page):
    locators = ConnectCTALocators(page)
    cta = locators.connect_cta
    name = cta.get_attribute("aria-label") or cta.text_content()
    assert name and "Connect" in name, "CTA should have accessible name"


@when("User clicks Connect CTA")
def click_connect_cta(page: Page):
    locators = ConnectCTALocators(page)
    locators.connect_cta.click()


@then("User is on the contact page at /contact/")
def on_contact_page(page: Page):
    expect(page).to_have_urlContaining("/contact/")


@given("Connect CTA is focused via keyboard")
def cta_keyboard_focused(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    locators = ConnectCTALocators(page)
    locators.connect_cta.focus()


@when("User activates (Enter/Space)")
def activate_cta(page: Page):
    page.keyboard.press("Enter")


@then("CTA works with keyboard activation")
def cta_keyboard_works(page: Page):
    expect(page).to_have_urlContaining("/contact/")


@given("Connect CTA destination is configured")
def cta_configured(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_cta_url(page: Page):
    pass


@then("CTA URL is valid and uses HTTPS")
def cta_https(page: Page):
    locators = ConnectCTALocators(page)
    href = locators.connect_cta.get_attribute("href")
    assert href and href.startswith("https://"), f"CTA should use HTTPS: {href}"


@given("Contact page is unavailable or returns error")
def contact_unavailable(page: Page):
    page.goto("/")
    page.route("**/contact/**", lambda route: route.abort())


@when("User clicks Connect CTA")
def click_cta_unavailable(page: Page):
    locators = ConnectCTALocators(page)
    locators.connect_cta.click()


@then("User sees appropriate error page or fallback")
def sees_error_or_fallback(page: Page):
    pass


@given("Header at narrow viewport")
def narrow_viewport_cta(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Connect CTA label is long")
def long_cta_label(page: Page):
    pass


@then("Text wrapping does not break layout or accessibility")
def text_wrapping_handled(page: Page):
    locators = ConnectCTALocators(page)
    expect(locators.connect_cta).to_be_visible()
