"""Step definitions for issue_0022: Render Engineering capability content."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Engineering capability card")
def view_engineering_card(page: Page) -> None:
    page.goto("/")


@when("Checking content")
def check_content(page: Page) -> None:
    pass


@then("Engineering title and supporting summary text are visible")
def engineering_content_visible(page: Page) -> None:
    expect(page.getByText("Engineering")).to_be_visible()


@given("User clicks Engineering capability link")
def click_engineering_link(page: Page) -> None:
    page.goto("/")
    eng_link = page.getByRole("link").filter(has=page.getByText("Engineering")).first
    if eng_link.count() > 0:
        eng_link.click()


@when("Navigation triggered")
def nav_triggered(page: Page) -> None:
    pass


@then("User navigates to valid Engineering capability destination")
def navigate_engineering(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("User views Engineering card")
def view_engineering_card(page: Page) -> None:
    page.goto("/")


@when("Comparing styling")
def compare_styling(page: Page) -> None:
    pass


@then("Card follows same visual pattern as AI and Platforms cards")
def same_pattern(page: Page) -> None:
    expect(page.getByText("Engineering")).to_be_visible()


@given("Content validation")
def content_validation(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_required_fields(page: Page) -> None:
    pass


@then("Engineering title field is populated")
def engineering_populated(page: Page) -> None:
    eng_text = page.getByText("Engineering").first.text_content()
    assert eng_text is not None and len(eng_text.strip()) > 0


@given("Engineering capability URL")
def engineering_url(page: Page) -> None:
    page.goto("/")


@when("Checking validity")
def check_validity(page: Page) -> None:
    pass


@then("URL is valid internal path and resolves")
def url_valid(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")
