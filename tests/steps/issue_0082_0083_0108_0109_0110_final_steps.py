"""Step definitions for media, resilience, and global requirements."""
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


@then("header main content footer readable when scripts fail")
def content_readable_scripts_fail(page: Page) -> None:
    """Verify header main content footer readable when scripts fail."""
    header = page.get_by_role("banner").first
    main = page.get_by_role("main").first
    footer = page.get_by_role("contentinfo").first
    
    expect(header).to_be_visible()
    expect(main).to_be_visible()
    expect(footer).to_be_visible()


@then("base homepage loads without unsolicited modal")
def no_unsolicited_modal(page: Page) -> None:
    """Verify base homepage loads without unsolicited modal."""
    h1 = page.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
    
    modals = page.locator('[role="dialog"], .modal, .popup').all()
    visible_modals = [m for m in modals if m.is_visible()]
    assert len(visible_modals) == 0
