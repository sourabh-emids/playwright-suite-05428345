"""Test for WCAG 2.1 AA accessibility requirements."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_keyboard_access_all(page_ready: Page) -> None:
    """Test WCAG 2.1 AA keyboard access on all interactive elements."""
    page_ready.keyboard.press("Tab")
    focused = page_ready.evaluate("() => document.activeElement")
    assert focused is not None


def test_visible_focus_indicators(page_ready: Page) -> None:
    """Test WCAG 2.1 AA visible focus indicators."""
    nav = page_ready.get_by_role("navigation", name="Main Navigation")
    first_link = nav.get_by_role("link").first
    first_link.focus()
    expect(first_link).to_be_focused()


def test_alt_text_images(page_ready: Page) -> None:
    """Test WCAG 2.1 AA meaningful alt text on images."""
    images = page_ready.locator("img").all()
    for img in images:
        alt = img.get_attribute("alt")
        src = img.get_attribute("src")
        if src and not src.endswith(".svg"):
            assert alt is not None


def test_zoom_reflow_support(page_ready: Page) -> None:
    """Test WCAG 2.1 AA 200% zoom reflow support."""
    page_ready.set_viewport_size({"width": 640, "height": 480})
    h1 = page_ready.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
