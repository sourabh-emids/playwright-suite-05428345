"""Test for issue_0036: Required content fields not empty in section."""
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


def test_how_we_deliver_fields_not_empty(page_ready: Page) -> None:
    """Test required content fields are not empty in How We Deliver section."""
    h2 = page_ready.get_by_role("heading", name="Embedded healthcare expertise")
    h3 = page_ready.get_by_role("heading", name="Forward-Deployed Context Engineering")
    paragraph = page_ready.locator("text=Forward-deployed context engineering turns ambition into measurable outcomes").first
    
    expect(h2).to_be_visible()
    expect(h3).to_be_visible()
    expect(paragraph).to_be_visible()
    
    h2_text = h2.text_content()
    h3_text = h3.text_content()
    paragraph_text = paragraph.text_content()
    
    assert h2_text is not None and h2_text.strip() != "", "H2 should have text"
    assert h3_text is not None and h3_text.strip() != "", "H3 should have text"
    assert paragraph_text is not None and paragraph_text.strip() != "", "Paragraph should have text"
