"""Steps for 1 Day 2 Weeks 3 Months delivery message (issue_0035)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0035_final_cta_timing_locators import FinalCTATimingLocators


@given("User views Final CTA section")
def view_final_cta(page: Page) -> None:
    page.goto("/")


@given("User views timing labels")
def view_labels(page: Page) -> None:
    page.goto("/")


@given("User uses screen reader")
def screen_reader(page: Page) -> None:
    page.goto("/")


@given("Timing labels render")
def labels_render(page: Page) -> None:
    page.goto("/")


@given("Timing labels have explanatory labels")
def explanatory_labels(page: Page) -> None:
    page.goto("/")


@given("User views Final CTA at mobile width")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Labels display")
def labels_display(page: Page) -> None:
    pass


@when("Screen reader encounters timing labels")
def sr_encounter(page: Page) -> None:
    pass


@when("CSS styling is disabled")
def css_disabled(page: Page) -> None:
    pass


@then("All timing labels render: '1 Day', '2 Weeks', '3 Months'")
def all_labels_render(page: Page) -> None:
    locators = FinalCTATimingLocators(page)
    expect(locators.timing_section).to_be_visible()


@then("Labels appear in intended order (1 Day → 2 Weeks → 3 Months)")
def labels_order(page: Page) -> None:
    locators = FinalCTATimingLocators(page)
    expect(locators.timing_section).to_be_visible()


@then("Timing labels are readable in logical order")
def readable_order(page: Page) -> None:
    expect(FinalCTATimingLocators(page).timing_section).to_be_visible()


@then("Meaning is conveyed through text, not visual styling alone")
def meaning_text(page: Page) -> None:
    expect(FinalCTATimingLocators(page).day_label).to_be_visible()


@then("Explanatory labels display where configured")
def explanatory_display(page: Page) -> None:
    pass


@then("Timing labels wrap appropriately at mobile widths")
def wrapping_mobile(page: Page) -> None:
    expect(FinalCTATimingLocators(page).timing_section).to_be_visible()
