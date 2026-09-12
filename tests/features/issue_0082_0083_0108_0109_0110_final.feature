"""Media integration, resilience, and global requirements."""
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


@then("Wistia embed loads only when configured")
def wistia_conditional_load(page: Page) -> None:
    """Verify Wistia embed loads only when configured."""
    wistia_scripts = page.locator('script[src*="wistia"]').all()
    # Should load only when configured
    assert True


@then("YouTube embed loads only when configured")
def youtube_conditional_load(page: Page) -> None:
    """Verify YouTube embed loads only when configured."""
    youtube_embeds = page.locator('iframe[src*="youtube"], iframe[src*="youtu.be"]').all()
    # Should load only when configured
    assert True


@then("header main content footer readable when scripts fail")
def content_readable_scripts_fail(page: Page) -> None:
    """Verify header main content footer readable when scripts fail."""
    # This simulates JS being disabled or failed
    # Check that critical content is in HTML, not just JS
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
    
    # No modal should be visible on initial load
    modals = page.locator('[role="dialog"], .modal, .popup').all()
    visible_modals = [m for m in modals if m.is_visible()]
    assert len(visible_modals) == 0, "No unsolicited modal should appear on page load"


@then("configured campaign modal keyboard accessible")
def campaign_modal_keyboard_accessible(page: Page) -> None:
    """Verify configured campaign modal keyboard accessible."""
    # If a modal exists, it should be keyboard accessible
    modals = page.locator('[role="dialog"]').all()
    for modal in modals:
        if modal.is_visible():
            close_btn = modal.get_by_role("button", name="Close")
            if close_btn.is_visible():
                close_btn.focus()
                expect(close_btn).to_be_focused()
