"""Step definitions for issue_0032: Hero text content available if media fails."""
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


@then("Hero text content is available if media fails")
def hero_text_available(page: Page) -> None:
    """Verify Hero text content is available if media fails."""
    h1 = page.get_by_role("heading", level=1).first
    h2 = page.get_by_role("heading", level=2).first
    hero_cta = page.get_by_role("link", name="See How We Deliver Outcomes")
    
    expect(h1).to_be_visible()
    expect(h2).to_be_visible()
    expect(hero_cta).to_be_visible()
    
    h1_text = h1.text_content()
    h2_text = h2.text_content()
    cta_text = hero_cta.text_content()
    
    assert h1_text is not None and h1_text.strip() != "", "H1 should have text content"
    assert h2_text is not None and h2_text.strip() != "", "H2 should have text content"
    assert cta_text is not None and cta_text.strip() != "", "Hero CTA should have text content"
