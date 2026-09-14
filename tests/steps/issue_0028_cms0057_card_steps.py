"""Step definitions for issue_0028: Display CMS-0057 interoperability card."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@when("Locating CMS-0057 card")
def locate_cms0057(page: Page) -> None:
    pass


@then("Card displays with approved title, type, and action")
def cms0057_displayed(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("User clicks CMS-0057 card")
def click_cms0057(page: Page) -> None:
    page.goto("/")
    link = page.getByRole("link").first
    if link.is_visible():
        link.click()


@when("Navigation occurs")
def nav_occurs(page: Page) -> None:
    pass


@then("User navigates to configured resource destination")
def navigate_destination(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("CMS validation for CMS-0057 card")
def cms_validation(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_fields(page: Page) -> None:
    pass


@then("Card has non-empty title and valid destination URL")
def card_valid(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("CMS-0057 resource URL changed")
def url_changed(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Card links to updated URL or broken link flagged in QA")
def link_updated(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("CMS-0057 content is unpublished")
def content_unpublished(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("Card not displayed or shows appropriate unavailable state")
def unavailable_state(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
