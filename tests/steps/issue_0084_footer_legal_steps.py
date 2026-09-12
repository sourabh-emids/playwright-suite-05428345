"""Step definitions for issue_0084: Footer legal links have valid HTTPS destinations."""
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


@then("footer legal links have valid HTTPS destinations")
def footer_legal_https(page: Page) -> None:
    """Verify footer legal links have valid HTTPS destinations."""
    footer = page.get_by_role("contentinfo")
    legal_links = ["Privacy Policy", "Terms of Use", "Accessibility Statement"]
    
    for link_text in legal_links:
        link = footer.get_by_role("link", name=link_text)
        if link.is_visible():
            href = link.get_attribute("href")
            assert href is not None, f"{link_text} should have href"
            assert href.startswith("https://"), f"{link_text} should use HTTPS"
