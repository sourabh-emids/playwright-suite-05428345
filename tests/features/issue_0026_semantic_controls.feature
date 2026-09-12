"""Interactive controls are semantic buttons links."""
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


@then("interactive controls are semantic buttons or links")
def controls_are_semantic(page: Page) -> None:
    """Verify interactive controls are semantic buttons or links."""
    nav = page.get_by_role("navigation", name="Main Navigation")
    
    # Check buttons are actual button elements
    buttons = nav.get_by_role("button").all()
    for button in buttons:
        tag = button.evaluate("el => el.tagName")
        assert tag == "BUTTON", f"Button element should be a semantic <button>, got <{tag}>"
    
    # Check links are actual anchor elements
    links = nav.get_by_role("link").all()
    for link in links:
        tag = link.evaluate("el => el.tagName")
        assert tag == "A", f"Link element should be a semantic <a>, got <{tag}>"
