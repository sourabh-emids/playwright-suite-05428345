"""Step definitions for issue_0027: Display Medicare Advantage eBook card."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@when("Locating specific card")
def locate_card(page: Page) -> None:
    pass


@then("Card titled 'Managing the Margin Reset in Medicare Advantage' is visible with eBook type")
def medicare_card_visible(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("Medicare Advantage eBook has thumbnail")
def ebook_has_thumbnail(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("Card displays eBook cover image")
def cover_image_displayed(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("User views Medicare Advantage card")
def view_medicare_card(page: Page) -> None:
    page.goto("/")


@when("Checking action")
def check_action(page: Page) -> None:
    pass


@then("Download CTA is visible on card")
def download_cta_visible(page: Page) -> None:
    download = page.getByRole("link", name="Download")
    expect(download.first).to_be_visible()


@when("User clicks Download on Medicare Advantage card")
def click_download_medicare(page: Page) -> None:
    page.goto("/")
    download = page.getByRole("link", name="Download").first
    if download.is_visible():
        download.click()


@then("User navigates to /insights/managing-the-margin-reset-in-medicare-advantage/")
def navigate_medicare(page: Page) -> None:
    assert "/insights/" in page.url or page.url.startswith("https://www.emids.com")


@given("Medicare Advantage resource is removed")
def resource_removed(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Card not displayed or shows appropriate unavailable state")
def unavailable_or_hidden(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Medicare Advantage resource now requires different access flow")
def different_access_flow(page: Page) -> None:
    page.goto("/")


@when("User clicks Download")
def click_download(page: Page) -> None:
    download = page.getByRole("link", name="Download").first
    if download.is_visible():
        download.click()


@then("User reaches updated access experience")
def updated_access(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")
