"""Solutions mega-menu opens with all links selectable."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@when("I click the Solutions button in the header")
def click_solutions_button(page: Page) -> None:
    """Click the Solutions button."""
    page.get_by_role("button", name="Solutions").first.click()


@then("the Solutions mega-menu opens")
def solutions_menu_opens(page: Page) -> None:
    """Verify Solutions mega-menu opens."""
    menu = page.locator("[class*='solutions'], [aria-label*='Solutions']").first
    expect(menu).to_be_visible()


@then("all links in the menu are selectable")
def all_menu_links_selectable(page: Page) -> None:
    """Verify all links in Solutions menu are selectable."""
    expected_links = [
        "Modernization",
        "Interoperability",
        "Cloud Transformation",
        "Agentic AI",
        "Global Capability Center",
        "Payers",
        "Providers",
        "Health Tech",
        "Life Sciences",
    ]
    
    for link_text in expected_links:
        link = page.get_by_role("link", name=link_text).first
        expect(link).to_be_visible()
        href = link.get_attribute("href")
        assert href is not None and href != "", f"Link {link_text} should have valid href"
