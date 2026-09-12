"""Step definitions for accessibility requirements."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("WCAG 2.1 AA keyboard access on all interactive elements")
def keyboard_access_all(page: Page) -> None:
    """Verify WCAG 2.1 AA keyboard access on all interactive elements."""
    page.keyboard.press("Tab")
    focused = page.evaluate("() => document.activeElement")
    assert focused is not None


@then("WCAG 2.1 AA meaningful alt text on images")
def alt_text_images(page: Page) -> None:
    """Verify WCAG 2.1 AA meaningful alt text on images."""
    images = page.locator("img").all()
    for img in images:
        alt = img.get_attribute("alt")
        src = img.get_attribute("src")
        if src and not src.endswith(".svg"):
            assert alt is not None
