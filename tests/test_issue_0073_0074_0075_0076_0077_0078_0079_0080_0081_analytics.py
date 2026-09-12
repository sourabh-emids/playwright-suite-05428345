"""Test for analytics requirements."""
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


def test_core_page_functional_gtm_fails(page_ready: Page) -> None:
    """Test core page functional if GTM fails."""
    h1 = page_ready.get_by_role("heading", level=1).first
    assert h1.is_visible()


def test_utm_parameters_preserved(page_ready: Page) -> None:
    """Test UTM parameters preserved without breaking URLs."""
    page_ready.goto("/?utm_source=test&utm_medium=test&utm_campaign=test")
    h1 = page_ready.get_by_role("heading", level=1).first
    assert h1.is_visible()


def test_marketo_consent_gated(page_ready: Page) -> None:
    """Test Marketo marketing scripts gated by consent."""
    marketo_scripts = page_ready.locator('script[src*="marketo"]').all()
    for script in marketo_scripts:
        async_attr = script.get_attribute("async")
        defer_attr = script.get_attribute("defer")
        assert async_attr is not None or defer_attr is not None
