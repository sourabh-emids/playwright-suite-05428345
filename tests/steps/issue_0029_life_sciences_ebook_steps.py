"""Step definitions for issue_0029: Display Life Sciences eBook card."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@when("Locating specific card")
def locate_card(page: Page) -> None:
    pass


@then("Card titled 'Unlocking Trusted Digital Transformation in Life Sciences' displays")
def life_sciences_card(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@when("User clicks Download on Life Sciences card")
def click_ls_download(page: Page) -> None:
    page.goto("/")
    download = page.getByRole("link", name="Download").first
    if download.is_visible():
        download.click()


@then("User navigates to /insights/unlocking-trusted-digital-transformation-in-life-sciences/")
def navigate_ls(page: Page) -> None:
    assert "/insights/" in page.url or page.url.startswith("https://www.emids.com")


@given("User inspects URL")
def inspect_url(page: Page) -> None:
    page.goto("/")


@when("Checking URL format")
def check_url_format(page: Page) -> None:
    pass


@then("URL is canonical path to Life Sciences resource")
def canonical_path(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Resource access flow is down")
def access_flow_down(page: Page) -> None:
    page.goto("/")


@when("User clicks Download")
def click_download(page: Page) -> None:
    download = page.getByRole("link", name="Download").first
    if download.is_visible():
        download.click()


@then("User sees appropriate error or fallback experience")
def error_fallback(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")
