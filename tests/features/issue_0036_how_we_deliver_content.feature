"""Required content fields not empty in section."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("required content fields are not empty in How We Deliver section")
def how_we_deliver_fields_not_empty(page: Page) -> None:
    """Verify required content fields are not empty in How We Deliver section."""
    h2 = page.get_by_role("heading", name="Embedded healthcare expertise")
    h3 = page.get_by_role("heading", name="Forward-Deployed Context Engineering")
    paragraph = page.locator("text=Forward-deployed context engineering turns ambition into measurable outcomes").first
    
    expect(h2).to_be_visible()
    expect(h3).to_be_visible()
    expect(paragraph).to_be_visible()
    
    h2_text = h2.text_content()
    h3_text = h3.text_content()
    paragraph_text = paragraph.text_content()
    
    assert h2_text is not None and h2_text.strip() != "", "H2 should have text"
    assert h3_text is not None and h3_text.strip() != "", "H3 should have text"
    assert paragraph_text is not None and paragraph_text.strip() != "", "Paragraph should have text"
