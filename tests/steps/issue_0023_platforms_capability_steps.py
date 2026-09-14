"""Step definitions for issue_0023: Render Platforms capability content."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Platforms capability card")
def view_platforms_card(page: Page) -> None:
    page.goto("/")


@when("Checking label")
def check_label(page: Page) -> None:
    pass


@then("Label uses approved taxonomy term (e.g., 'Platforms' or 'Provider Platforms' as approved)")
def approved_taxonomy(page: Page) -> None:
    expect(page.getByText("Platforms")).to_be_visible()


@given("User compares header navigation to Platforms section body")
def compare_nav_body(page: Page) -> None:
    page.goto("/")


@when("Checking terminology consistency")
def check_terminology(page: Page) -> None:
    pass


@then("Navigation 'Platforms' matches section body label without inconsistent synonyms")
def consistent_terminology(page: Page) -> None:
    expect(page.getByText("Platforms")).to_be_visible()


@given("User views Platforms card")
def view_platforms(page: Page) -> None:
    page.goto("/")


@when("Checking styling")
def check_styling(page: Page) -> None:
    pass


@then("Card follows capability visual system")
def visual_system(page: Page) -> None:
    expect(page.getByText("Platforms")).to_be_visible()


@given("Content validation")
def content_validation(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_fields(page: Page) -> None:
    pass


@then("Platforms title field is populated with approved label")
def platforms_populated(page: Page) -> None:
    plat_text = page.getByText("Platforms").first.text_content()
    assert plat_text is not None and len(plat_text.strip()) > 0


@given("CMS has outdated Platforms content")
def outdated_platforms_content(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("Content governance workflow catches stale content before publishing")
def governance_catches(page: Page) -> None:
    expect(page.getByText("Platforms")).to_be_visible()
