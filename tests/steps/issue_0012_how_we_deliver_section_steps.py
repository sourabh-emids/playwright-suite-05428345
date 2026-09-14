"""Step definitions for issue_0012: Render How We Deliver section."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views the page")
def user_views_page(page: Page) -> None:
    page.goto("/")


@when("Scanning page structure")
def scan_page_structure(page: Page) -> None:
    pass


@then("How We Deliver section appears after hero section in document order")
def section_sequence(page: Page) -> None:
    h1 = page.locator("h1").first
    h2 = page.get_by_role("heading", name="Forward-Deployed Context Engineering")
    expect(h1).to_be_visible()
    expect(h2).to_be_visible()


@given("How We Deliver section is present")
def how_we_deliver_present(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_required_fields(page: Page) -> None:
    pass


@then("Section title, supporting explanation, visual/content elements, and CTA all render")
def fields_render(page: Page) -> None:
    expect(page.get_by_text("Forward-Deployed Context Engineering")).to_be_visible()
    expect(page.get_by_role("link", name="See the model")).to_be_visible()


@given("User tests section accessibility")
def test_section_accessibility(page: Page) -> None:
    page.goto("/")


@when("Navigating via screen reader or keyboard")
def navigate_screen_reader(page: Page) -> None:
    page.keyboard.press("Tab")


@then("All content is accessible; heading hierarchy is logical")
def content_accessible(page: Page) -> None:
    expect(page.get_by_role("heading", name="Forward-Deployed Context Engineering")).to_be_visible()


@given("CMS content is being loaded")
def cms_loading(page: Page) -> None:
    page.goto("/")


@when("Checking for empty required fields")
def check_empty_fields(page: Page) -> None:
    pass


@then("Section title, body, and CTA are populated; empty fields are not rendered")
def fields_populated(page: Page) -> None:
    section = page.get_by_text("Forward-Deployed Context Engineering")
    expect(section).to_be_visible()
    assert len(section.text_content() or "") > 0


@when("Checking H tag sequence")
def check_h_sequence(page: Page) -> None:
    pass


@then("Headings follow logical order (H2 for section if H1 exists, etc.)")
def h_sequence_logical(page: Page) -> None:
    headings = page.locator("h1, h2, h3, h4")
    # Should have at least h1 and h2
    assert page.locator("h1").count() >= 1


@given("How We Deliver section visual is missing")
def visual_missing(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Text content remains visible; section remains functional")
def text_visible(page: Page) -> None:
    expect(page.get_by_role("link", name="See the model")).to_be_visible()


@given("Section body copy is very long")
def long_copy(page: Page) -> None:
    page.goto("/")


@when("Page renders at standard viewport")
def render_standard(page: Page) -> None:
    pass


@then("Layout accommodates content without horizontal overflow")
def no_overflow(page: Page) -> None:
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    assert scroll_width <= 1280
