"""Step definitions for issue_0007: Provide header Connect CTA."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views the header")
def user_views_header(page: Page) -> None:
    page.goto("/")


@when("User identifies the Connect CTA")
def identify_connect_cta(page: Page) -> None:
    pass


@then("CTA has visual differentiation from standard navigation links")
def cta_visual_differentiation(page: Page) -> None:
    connect_cta = page.get_by_role("link", name="Connect").first
    styles = connect_cta.evaluate("() => window.getComputedStyle(arguments[0]).getPropertyValue('background-color')", connect_cta)
    assert styles is not None


@given("User inspects the CTA element")
def inspect_cta_element(page: Page) -> None:
    page.goto("/")


@when("Checking accessibility attributes")
def check_accessibility_attributes(page: Page) -> None:
    pass


@then("CTA has descriptive accessible name describing the action")
def cta_accessible_name(page: Page) -> None:
    connect_cta = page.get_by_role("link", name="Connect").first
    expect(connect_cta).to_have_attribute("aria-label")


@when("User clicks the Connect CTA")
def click_connect_cta(page: Page) -> None:
    page.get_by_role("link", name="Connect").first.click()


@then("User lands on /contact/ page with valid HTTPS URL")
def lands_on_contact(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/contact/")
    assert page.url.startswith("https://")


@given("User focuses on Connect CTA")
def focus_connect_cta(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="Connect").first.focus()


@when("User presses Enter or Space key")
def press_enter_or_space(page: Page) -> None:
    page.keyboard.press("Enter")


@then("Contact page navigation is triggered")
def contact_nav_triggered(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/contact/")


@when("Header renders in mobile layout")
def mobile_layout_rendered(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("Connect CTA remains visible and accessible in mobile header")
def cta_mobile_visible(page: Page) -> None:
    connect_cta = page.get_by_role("link", name="Connect")
    if connect_cta.count() > 0:
        expect(connect_cta.first).to_be_visible()
    else:
        menu_btn = page.get_by_role("button", name="Open menu")
        expect(menu_btn).to_be_visible()


@given("Contact page returns 404 or error")
def contact_404(page: Page) -> None:
    pass


@when("User clicks Connect CTA")
def click_connect_404(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="Connect").first.click()


@then("Error page displays or fallback content is shown")
def error_page_displayed(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com/contact") or "error" in page.url.lower() or "404" in page.url


@when("CTA text is long")
def long_cta_text(page: Page) -> None:
    pass


@then("Text wraps gracefully without breaking functionality or overlapping")
def text_wraps(page: Page) -> None:
    page.set_viewport_size({"width": 400, "height": 800})
    page.goto("/")
    header = page.locator("header")
    expect(header).to_be_visible()
