"""Step definitions for issue_0039: Exactly one H1 on page with logical heading hierarchy."""
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


@then("there is exactly one H1 on the page")
def exactly_one_h1(page: Page) -> None:
    """Verify exactly one H1 on the page."""
    h1_elements = page.get_by_role("heading", level=1).all()
    assert len(h1_elements) == 1, f"Should have exactly one H1, found {len(h1_elements)}"


@then("heading hierarchy is logical")
def heading_hierarchy_logical(page: Page) -> None:
    """Verify heading hierarchy is logical (H2 follows H1, etc.)."""
    h1_elements = page.get_by_role("heading", level=1).all()
    h2_elements = page.get_by_role("heading", level=2).all()
    h3_elements = page.get_by_role("heading", level=3).all()
    
    assert len(h1_elements) >= 1, "Should have at least one H1"
    if len(h3_elements) > 0:
        assert len(h2_elements) >= 1, "H3 elements should have H2 parents"
