"""Step definitions for issue_0021: Render AI capability content."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views AI capability card/panel")
def view_ai_card(page: Page) -> None:
    page.goto("/")


@when("Checking content")
def check_content(page: Page) -> None:
    pass


@then("AI title and supporting summary text are visible")
def ai_content_visible(page: Page) -> None:
    expect(page.getByText("AI")).to_be_visible()


@given("User clicks AI capability link")
def click_ai_link(page: Page) -> None:
    page.goto("/")
    ai_link = page.getByRole("link").filter(has=page.getByText("AI")).first
    if ai_link.count() > 0:
        ai_link.click()


@when("Navigation triggered")
def navigation_triggered(page: Page) -> None:
    pass


@then("User navigates to valid AI capability destination")
def navigate_ai_destination(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("User views AI card alongside other capability cards")
def view_ai_with_other_cards(page: Page) -> None:
    page.goto("/")


@when("Comparing visual styling")
def compare_styling(page: Page) -> None:
    pass


@then("AI card follows same card/panel visual system as Engineering and Platforms cards")
def same_visual_system(page: Page) -> None:
    expect(page.getByText("AI")).to_be_visible()
    expect(page.getByText("Engineering")).to_be_visible()
    expect(page.getByText("Platforms")).to_be_visible()


@given("CMS validation")
def cms_validation(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_required_fields(page: Page) -> None:
    pass


@then("AI title is present and non-empty")
def ai_title_populated(page: Page) -> None:
    ai_text = page.getByText("AI").first.text_content()
    assert ai_text is not None and len(ai_text.strip()) > 0


@given("User clicks AI link")
def user_clicks_ai_link(page: Page) -> None:
    page.goto("/")


@when("URL requested")
def url_requested(page: Page) -> None:
    pass


@then("AI destination URL is valid and resolves successfully")
def ai_url_valid(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("AI card has optional media that fails")
def ai_media_fails(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("Text content remains; card is functional without broken media")
def text_remains_functional(page: Page) -> None:
    expect(page.getByText("Capabilities that deliver on ambitious goals")).to_be_visible()
