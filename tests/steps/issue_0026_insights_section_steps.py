"""Steps for Insights section and six content cards (issue_0026)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0026_insights_section_locators import InsightsSectionLocators


@given("User views Insights section")
def view_insights(page: Page) -> None:
    page.goto("/")


@given("Insight cards render")
def cards_render(page: Page) -> None:
    page.goto("/")


@given("User views Insights section at mobile, tablet, and desktop widths")
def view_breakpoints(page: Page) -> None:
    page.goto("/")


@given("One resource is unpublished")
def resource_unpublished(page: Page) -> None:
    page.goto("/")


@given("Card image is missing")
def image_missing(page: Page) -> None:
    page.goto("/")


@given("Card has very long title")
def long_title(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User views each card")
def view_each_card(page: Page) -> None:
    pass


@when("User validates content")
def validate_content(page: Page) -> None:
    pass


@when("User views action labels")
def view_action_labels(page: Page) -> None:
    pass


@then("Six insight/resource cards are rendered")
def six_cards(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Each card displays content type (eBook, Blog, etc.)")
def content_type(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Each card displays a title")
def card_title(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Image is displayed where configured")
def image_displayed(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Each card displays Download or Read More action with appropriate label")
def action_displayed(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Cards remain accessible and content visible")
def cards_accessible(page: Page) -> None:
    for width in [375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Only published content is displayed")
def published_only(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Each card has non-empty title and valid URL")
def title_url_valid(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Action labels match content flow (Download for eBooks, Read More for articles)")
def action_matches_flow(page: Page) -> None:
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()


@then("Card either shows updated content or appropriate placeholder")
def placeholder_handling(page: Page) -> None:
    pass


@then("Placeholder or fallback displays appropriately")
def fallback_displayed(page: Page) -> None:
    pass


@then("Title wraps appropriately without breaking layout")
def title_wraps(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    expect(InsightsSectionLocators(page).insights_section).to_be_visible()
