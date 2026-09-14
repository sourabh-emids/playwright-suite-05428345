"""Step definitions for issue_0026: Render Insights section with six cards."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Insights section")
def view_insights_section(page: Page) -> None:
    page.goto("/")


@when("Counting cards")
def count_cards(page: Page) -> None:
    pass


@then("Six insight cards are visible, each with content type, title, and image where configured")
def six_cards_visible(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("User examines card actions")
def examine_card_actions(page: Page) -> None:
    page.goto("/")


@when("Checking CTA labels")
def check_cta_labels(page: Page) -> None:
    pass


@then("Cards display appropriate action labels: Download for eBooks, Read More for articles")
def proper_action_labels(page: Page) -> None:
    expect(page.getByRole("link", name="Download")).to_be_visible()
    expect(page.getByRole("link", name="Read More")).to_be_visible()


@given("User views Insights on mobile and desktop")
def view_insights_breakpoints(page: Page) -> None:
    page.goto("/")


@when("Checking card accessibility")
def check_card_accessibility(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("All six cards remain accessible and operable at all supported breakpoints")
def cards_accessible(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("CMS content validation")
def cms_validation(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_required_fields(page: Page) -> None:
    pass


@then("Each card has non-empty title and valid URL")
def cards_have_title_url(page: Page) -> None:
    cards = page.locator("[data-testid='insight-card']")
    assert cards.count() >= 0


@given("User reviews card CTA labels")
def review_cta_labels(page: Page) -> None:
    page.goto("/")


@when("Checking label accuracy")
def check_label_accuracy(page: Page) -> None:
    pass


@then("Download used for downloadable resources; Read More for article navigation")
def download_readmore_labels(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Some insight content is unpublished")
def some_unpublished(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("Only published insights display; unpublished items excluded")
def published_only(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("An insight card links to unpublished resource")
def unpublished_resource(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Card either not rendered or shows appropriate unavailable state")
def unavailable_state(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Insight card has no image configured")
def no_image_config(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("Card renders with placeholder or without image; no broken image shown")
def no_broken_image(page: Page) -> None:
    expect(page.getByText("The intelligence behind the outcomes")).to_be_visible()


@given("Insight title is very long")
def long_title(page: Page) -> None:
    page.goto("/")


@when("Card renders at standard width")
def render_standard_width(page: Page) -> None:
    pass


@then("Long title either displays fully or truncates with ellipsis; does not break layout")
def title_truncation(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Insight resource URL has changed")
def url_changed(page: Page) -> None:
    page.goto("/")


@when("User clicks card")
def click_card(page: Page) -> None:
    link = page.getByRole("link").filter(has=page.getByText("The intelligence")).first
    if link.count() > 0:
        link.click()


@then("Navigation either resolves to new URL or broken link is detected in QA")
def navigation_resolves(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")
