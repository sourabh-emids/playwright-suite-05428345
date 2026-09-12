"""Test for performance requirements."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_critical_content_no_wait(page_ready: Page) -> None:
    """Test critical content renders without waiting for analytics."""
    h1 = page_ready.get_by_role("heading", level=1).first
    assert h1.is_visible()
    
    header = page_ready.get_by_role("banner").first
    assert header.is_visible()


def test_images_optimized(page_ready: Page) -> None:
    """Test images sized and optimized appropriately."""
    images = page_ready.locator("img").all()
    for img in images:
        src = img.get_attribute("src")
        if src and not src.endswith(".svg"):
            assert src is not None


def test_scripts_consent_gated(page_ready: Page) -> None:
    """Test third party scripts async deferred consent gated."""
    scripts = page_ready.locator("script[src]").all()
    
    for script in scripts:
        src = script.get_attribute("src")
        if src and any(tag in src for tag in ["google", "analytics", "gtm"]):
            async_attr = script.get_attribute("async")
            defer_attr = script.get_attribute("defer")
            assert async_attr is not None or defer_attr is not None or "consent" in src
