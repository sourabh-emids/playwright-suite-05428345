"""Test for issue_0028: Hero CTA visible above page scroll on desktop."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_hero_cta_visible_desktop(page_ready: Page) -> None:
    """Test Hero CTA is visible without scrolling on desktop."""
    hero_cta = page_ready.get_by_role("link", name="See How We Deliver Outcomes")
    expect(hero_cta).to_be_in_viewport()
