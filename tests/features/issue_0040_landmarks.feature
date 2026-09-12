"""Semantic landmarks main header footer identifiable."""
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


@then("main header footer landmarks are identifiable")
def landmarks_identifiable(page: Page) -> None:
    """Verify main, header, and footer landmarks are identifiable."""
    header = page.get_by_role("banner").first
    main = page.get_by_role("main").first
    footer = page.get_by_role("contentinfo").first
    
    expect(header).to_be_visible()
    expect(main).to_be_visible()
    expect(footer).to_be_visible()
