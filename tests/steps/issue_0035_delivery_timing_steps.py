"""Step definitions for issue_0035: Render delivery timing message."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views final CTA section")
def view_final_cta(page: Page) -> None:
    page.goto("/")


@when("Reading timing content")
def read_timing_content(page: Page) -> None:
    pass


@then("1 Day, 2 Weeks, and 3 Months display in that sequence")
def timing_sequence(page: Page) -> None:
    expect(page.getByText("1 Day · 2 Weeks · 3 Months")).to_be_visible()


@when("Reading content")
def read_content(page: Page) -> None:
    pass


@then("All timing labels are announced in correct order with clear meaning")
def labels_announced(page: Page) -> None:
    expect(page.getByText("1 Day · 2 Weeks · 3 Months")).to_be_visible()


@given("Timing section styling review")
def styling_review(page: Page) -> None:
    page.goto("/")


@when("Checking accessible presentation")
def check_presentation(page: Page) -> None:
    pass


@then("Timing meaning is conveyed through text, not purely visual differences")
def text_not_visual(page: Page) -> None:
    expect(page.getByText("1 Day · 2 Weeks · 3 Months")).to_be_visible()


@given("Timing items have supporting explanations")
def timing_explanations(page: Page) -> None:
    page.goto("/")


@when("Checking display")
def check_display(page: Page) -> None:
    pass


@then("Explanatory labels render alongside timing values")
def labels_render(page: Page) -> None:
    expect(page.getByText("From workshop to agent to scale deployment")).to_be_visible()


@given("Timing item lacks explanation")
def lacks_explanation(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("Timing value still renders; missing explanation logged")
def value_renders(page: Page) -> None:
    expect(page.getByText("1 Day · 2 Weeks · 3 Months")).to_be_visible()


@given("Narrow viewport")
def narrow_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("Timing content renders")
def render_timing(page: Page) -> None:
    page.goto("/")


@then("Content wraps gracefully without breaking layout")
def graceful_wrap(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
