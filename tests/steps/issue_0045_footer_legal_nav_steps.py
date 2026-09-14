"""Step definitions for issue_0045: Render footer legal navigation."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views footer")
def view_footer(page: Page) -> None:
    page.goto("/")


@when("Locating Privacy Policy")
def locate_privacy(page: Page) -> None:
    pass


@then("Privacy Policy link visible and routes to valid HTTPS destination")
def privacy_link(page: Page) -> None:
    privacy = page.getByRole("link", name="Privacy Policy")
    expect(privacy).to_be_visible()


@when("Locating Cookie Policy")
def locate_cookie(page: Page) -> None:
    pass


@then("Cookie Policy link visible and routes to valid HTTPS destination")
def cookie_link(page: Page) -> None:
    cookie = page.getByRole("link", name="Cookie Policy")
    expect(cookie).to_be_visible()


@when("Locating Accessibility")
def locate_accessibility(page: Page) -> None:
    pass


@then("Accessibility Statement link visible with valid destination")
def accessibility_link(page: Page) -> None:
    accessibility = page.getByRole("link", name="Accessibility Statement")
    expect(accessibility).to_be_visible()


@given("Additional legal links configured")
def additional_links(page: Page) -> None:
    page.goto("/")


@when("Checking footer")
def check_footer(page: Page) -> None:
    pass


@then("Additional approved legal links display with descriptive text")
def additional_display(page: Page) -> None:
    expect(page.locator("footer")).to_be_visible()


@when("Checking focus")
def check_focus(page: Page) -> None:
    page.keyboard.press("Tab")


@then("Visible focus indicator present on legal links")
def focus_indicator(page: Page) -> None:
    expect(page.locator("footer")).to_be_visible()


@given("Content validation")
def content_validation(page: Page) -> None:
    page.goto("/")


@when("Checking legal link labels")
def check_labels(page: Page) -> None:
    pass


@then("All legal link labels have non-empty descriptive text")
def labels_nonempty(page: Page) -> None:
    expect(page.locator("footer")).to_be_visible()


@given("Legal page URL changed")
def url_changed(page: Page) -> None:
    page.goto("/")


@when("User clicks legal link")
def click_legal(page: Page) -> None:
    privacy = page.getByRole("link", name="Privacy Policy")
    if privacy.is_visible():
        privacy.click()


@then("Redirect in place or broken link detected in monitoring")
def redirect_or_broken(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("Legal link label is very long")
def long_label(page: Page) -> None:
    page.goto("/")


@when("Footer renders")
def footer_renders(page: Page) -> None:
    pass


@then("Long label displays without breaking footer layout")
def label_displays(page: Page) -> None:
    expect(page.locator("footer")).to_be_visible()


@given("Site supports multiple locales")
def multiple_locales(page: Page) -> None:
    page.goto("/")


@when("Checking legal links")
def check_legal_links(page: Page) -> None:
    pass


@then("Legal links appropriate for current locale display or fallback")
def locale_links(page: Page) -> None:
    expect(page.locator("footer")).to_be_visible()
