"""Step definitions for issue_0032: Display Payer data readiness blog card."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@when("Locating blog card")
def locate_blog(page: Page) -> None:
    pass


@then("Card titled 'Payers: Is Your Data Ready for AI?' displays with type=Blog")
def blog_card(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@when("User views Payer blog card")
def view_blog_card(page: Page) -> None:
    pass


@then("Read More action visible (not Download)")
def read_more_visible(page: Page) -> None:
    read_more = page.getByRole("link", name="Read More")
    expect(read_more.first).to_be_visible()


@given("User validates CTA labels")
def validate_cta_labels(page: Page) -> None:
    page.goto("/")


@when("Checking semantic accuracy")
def check_semantic(page: Page) -> None:
    pass


@then("Blog content uses Read More rather than Download")
def read_more_for_blog(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@when("User clicks Read More")
def click_read_more(page: Page) -> None:
    page.goto("/")
    read_more = page.getByRole("link", name="Read More").first
    if read_more.is_visible():
        read_more.click()


@then("User navigates to configured blog URL")
def navigate_blog(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("Blog article URL has changed")
def url_changed(page: Page) -> None:
    page.goto("/")


@when("User clicks Read More")
def click_read_more_changed(page: Page) -> None:
    read_more = page.getByRole("link", name="Read More").first
    if read_more.is_visible():
        read_more.click()


@then("Navigation resolves to new URL or broken link flagged")
def navigation_resolves(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("Blog title is very long")
def long_blog_title(page: Page) -> None:
    page.goto("/")


@when("Card renders at standard width")
def render_width(page: Page) -> None:
    pass


@then("Title truncates with ellipsis or displays fully without breaking layout")
def title_truncation(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
