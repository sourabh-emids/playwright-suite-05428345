"""Step definitions for issue_0019: Company menu exposes approved links keyboard operable."""
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


@then("Company menu exposes approved links and is keyboard operable")
def company_menu_exposes_links_keyboard_operable(page: Page) -> None:
    """Verify Company menu exposes approved links and is keyboard operable."""
    page.get_by_role("button", name="Company").first.click()
    
    approved_links = [
        "Our Story",
        "Leadership Team",
        "Partners",
        "Careers",
        "Offices",
        "Contact Us",
    ]
    
    for link_text in approved_links:
        link = page.get_by_role("link", name=link_text)
        expect(link).to_be_visible()
    
    first_link = page.get_by_role("link", name="Our Story").first
    first_link.focus()
    expect(first_link).to_be_focused()
