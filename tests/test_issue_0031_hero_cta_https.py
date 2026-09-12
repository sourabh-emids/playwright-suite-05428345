"""Test for issue_0031: Hero CTA uses HTTPS canonical URL."""
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


def test_hero_cta_uses_https(page_ready: Page) -> None:
    """Test Hero CTA uses HTTPS canonical URL."""
    hero_cta = page_ready.get_by_role("link", name="See How We Deliver Outcomes")
    href = hero_cta.get_attribute("href")
    assert href is not None, "Hero CTA should have href"
    assert href.startswith("https://"), f"Hero CTA should use HTTPS: {href}"
