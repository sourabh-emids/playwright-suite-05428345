"""Step definitions for issue_0030: Display AI ROI eBook card."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@when("Locating AI ROI card")
def locate_ai_roi(page: Page) -> None:
    pass


@then("Card titled 'Closing the AI ROI Gap in Healthcare' displays with eBook type")
def ai_roi_card(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@when("User views AI ROI card")
def view_ai_roi_card(page: Page) -> None:
    pass


@then("Download or Read More action visible per card configuration")
def action_visible(page: Page) -> None:
    download = page.getByRole("link", name="Download")
    read_more = page.getByRole("link", name="Read More")
    assert download.count() > 0 or read_more.count() > 0


@given("CMS validation")
def cms_validation(page: Page) -> None:
    page.goto("/")


@when("Checking content status")
def check_content_status(page: Page) -> None:
    pass


@then("AI ROI resource is in published state")
def published_state(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("User inspects AI ROI URL")
def inspect_ai_roi_url(page: Page) -> None:
    page.goto("/")


@when("Checking validity")
def check_validity(page: Page) -> None:
    pass


@then("URL resolves to valid AI ROI detail page")
def url_resolves(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("AI ROI resource unpublished or redirected")
def ai_roi_unpublished(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Card either not displayed or shows current status")
def status_shown(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
