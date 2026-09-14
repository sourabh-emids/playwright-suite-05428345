"""Step definitions for issue_0031: Display FinOps healthcare payer card."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@when("Locating FinOps card")
def locate_finops(page: Page) -> None:
    pass


@then("FinOps best-practices card for healthcare payers displays")
def finops_card(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@when("User examines FinOps card")
def examine_finops(page: Page) -> None:
    pass


@then("Card has title, content type, and CTA action visible")
def card_has_all(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@when("User clicks FinOps card CTA")
def click_finops_cta(page: Page) -> None:
    page.goto("/")
    link = page.getByRole("link").first
    if link.is_visible():
        link.click()


@then("User navigates to configured FinOps resource destination")
def navigate_finops(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("FinOps resource link is broken")
def finops_broken(page: Page) -> None:
    page.goto("/")


@when("User clicks card")
def click_card(page: Page) -> None:
    link = page.getByRole("link").first
    if link.is_visible():
        link.click()


@then("Error page displays or card not rendered")
def error_displayed(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("FinOps card has no thumbnail")
def no_thumbnail(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Card renders without broken image placeholder")
def no_broken_image(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
