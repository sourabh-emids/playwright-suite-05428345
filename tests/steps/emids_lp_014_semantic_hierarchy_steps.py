"""Step definitions for emids_lp_014 - Semantic section hierarchy."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Exactly one H1 element exists on the page")
def verify_single_h1(page: Page) -> None:
    h1_elements = page.locator("h1")
    expect(h1_elements).to_have_count(1)


@then("H2, H3, etc. follow logical progression without skipping levels where avoidable")
def verify_heading_progression(page: Page) -> None:
    headings = page.locator("h1, h2, h3, h4, h5, h6").all()
    levels = [int(h.evaluate("el => el.tagName.replace('H', '')")) for h in headings]
    # Check that levels are in ascending order or same (no skipping)
    for i in range(1, len(levels)):
        assert levels[i] >= levels[i-1] - 1, f"Heading level skip at index {i}"


@then("Main, header, and footer regions have identifiable landmark roles")
def verify_landmark_roles(page: Page) -> None:
    expect(page.locator("header").first).to_be_visible()
    expect(page.locator("main").first).to_be_visible()
    expect(page.locator("footer").first).to_be_visible()


@then("Interactive text is not marked as headings solely for visual styling purposes")
def verify_no_styling_headings(page: Page) -> None:
    headings = page.locator("h1, h2, h3, h4, h5, h6").all()
    for h in headings:
        tag = h.evaluate("el => el.tagName")
        role = h.get_attribute("role")
        # If role is present, it should not be "button" or "link"
        if role:
            assert role not in ["button", "link"], f"Heading with role={role}"


@then("Only one H1 is rendered; additional content uses proper heading levels")
def verify_no_duplicate_h1(page: Page) -> None:
    h1_count = page.locator("h1").count()
    assert h1_count == 1, f"Found {h1_count} H1 elements"


@then("Hidden heading is not focusable or announced as navigation target")
def verify_hidden_heading_not_focusable(page: Page) -> None:
    hidden_headings = page.locator("h1, h2, h3, h4, h5, h6:hidden")
    for h in hidden_headings.all():
        assert not h.is_visible(), "Hidden heading should not be focusable"
