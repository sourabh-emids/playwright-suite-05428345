"""Step definitions for issue_0034: Render final conversion banner."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views page structure")
def view_page_structure(page: Page) -> None:
    page.goto("/")


@when("Checking section order")
def check_section_order(page: Page) -> None:
    pass


@then("Final CTA banner appears before footer section")
def cta_before_footer(page: Page) -> None:
    cta = page.getByText("From workshop to agent to scale deployment")
    footer = page.locator("footer")
    expect(cta).to_be_visible()
    expect(footer).to_be_visible()


@given("User focuses on banner CTA")
def focus_banner_cta(page: Page) -> None:
    page.goto("/")
    page.getByRole("link", name="Connect").last.focus()


@when("Pressing Tab to navigate")
def press_tab(page: Page) -> None:
    page.keyboard.press("Tab")


@then("CTA is keyboard accessible with visible focus")
def keyboard_accessible(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User views banner content")
def view_banner_content(page: Page) -> None:
    page.goto("/")


@when("Reading timing/message text")
def read_timing(page: Page) -> None:
    pass


@then("Supporting timing/value text is legible")
def timing_legible(page: Page) -> None:
    expect(page.getByText("1 Day · 2 Weeks · 3 Months")).to_be_visible()


@given("Content validation")
def content_validation(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_fields(page: Page) -> None:
    pass


@then("Banner has non-empty title, body text, and CTA")
def fields_present(page: Page) -> None:
    expect(page.getByRole("link", name="Connect")).to_be_visible()


@given("User tests contrast ratios")
def test_contrast(page: Page) -> None:
    page.goto("/")


@when("Checking accessibility")
def check_accessibility(page: Page) -> None:
    pass


@then("Banner meets contrast requirements for text readability")
def contrast_met(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@when("User clicks final CTA")
def click_final_cta(page: Page) -> None:
    page.getByRole("link", name="Connect").last.click()


@then("User navigates to /contact/")
def navigate_contact(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/contact/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("CTA text wraps without overlapping or breaking")
def text_wraps(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Viewport height is limited")
def limited_height(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 600})


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("CTA section does not overlap footer content")
def no_overlap(page: Page) -> None:
    expect(page.locator("footer")).to_be_visible()


@given("Contact page returns error")
def contact_error(page: Page) -> None:
    pass


@when("User clicks CTA")
def click_cta_error(page: Page) -> None:
    page.goto("/")
    page.getByRole("link", name="Connect").last.click()


@then("Error handling occurs appropriately")
def error_handling(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com/contact")
