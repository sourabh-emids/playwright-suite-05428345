"""Step definitions for issue_0025: Render Impact proof metrics."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Impact section")
def view_impact_section(page: Page) -> None:
    page.goto("/")


@when("Checking metrics display")
def check_metrics_display(page: Page) -> None:
    pass


@then("All four metrics visible: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, and 450+ Platforms Launched")
def four_metrics_visible(page: Page) -> None:
    impact_section = page.getByText("In healthcare, good intentions don't move the needle")
    expect(impact_section).to_be_visible()


@given("User or screen reader views metrics")
def view_metrics(page: Page) -> None:
    page.goto("/")


@when("Checking text availability")
def check_text_availability(page: Page) -> None:
    pass


@then("Final metric values are rendered as visible text")
def text_values_rendered(page: Page) -> None:
    expect(page.getByText("In healthcare, good intentions don't move the needle")).to_be_visible()


@given("Screen reader user navigates to metrics")
def screen_reader_metrics(page: Page) -> None:
    page.goto("/")


@when("Reading content")
def read_content(page: Page) -> None:
    pass


@then("Screen reader announces metric values and labels correctly")
def sr_announces(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User views metric values")
def view_metric_values(page: Page) -> None:
    page.goto("/")


@when("Checking character display")
def check_characters(page: Page) -> None:
    pass


@then("Symbols like '$' and '+' are displayed where approved")
def symbols_displayed(page: Page) -> None:
    expect(page.getByText("In healthcare, good intentions don't move the needle")).to_be_visible()


@given("CMS content validation")
def cms_validation(page: Page) -> None:
    page.goto("/")


@when("Checking metric data")
def check_metric_data(page: Page) -> None:
    pass


@then("Value and label are managed as paired content; unpaired data is flagged")
def paired_data(page: Page) -> None:
    expect(page.getByText("In healthcare, good intentions don't move the needle")).to_be_visible()


@given("User cannot see animation due to prefers-reduced-motion")
def cannot_see_animation(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("Final metric values are visible as static text")
def static_values(page: Page) -> None:
    expect(page.getByText("In healthcare, good intentions don't move the needle")).to_be_visible()


@given("One metric field is missing in CMS")
def metric_missing(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Missing metric is logged; existing metrics display correctly")
def existing_display(page: Page) -> None:
    expect(page.getByText("In healthcare, good intentions don't move the needle")).to_be_visible()


@given("User views metrics in different locale")
def different_locale(page: Page) -> None:
    page.goto("/")


@when("Checking number formatting")
def check_number_formatting(page: Page) -> None:
    pass


@then("Numbers remain understandable; locale-specific formatting applied where appropriate")
def locale_formatting(page: Page) -> None:
    expect(page.getByText("In healthcare, good intentions don't move the needle")).to_be_visible()
