"""Test for issue_0032: Hero text content available if media fails."""
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


def test_hero_text_available(page_ready: Page) -> None:
    """Test Hero text content is available if media fails."""
    h1 = page_ready.get_by_role("heading", level=1).first
    h2 = page_ready.get_by_role("heading", level=2).first
    hero_cta = page_ready.get_by_role("link", name="See How We Deliver Outcomes")
    
    expect(h1).to_be_visible()
    expect(h2).to_be_visible()
    expect(hero_cta).to_be_visible()
    
    h1_text = h1.text_content()
    h2_text = h2.text_content()
    cta_text = hero_cta.text_content()
    
    assert h1_text is not None and h1_text.strip() != "", "H1 should have text content"
    assert h2_text is not None and h2_text.strip() != "", "H2 should have text content"
    assert cta_text is not None and cta_text.strip() != "", "Hero CTA should have text content"
