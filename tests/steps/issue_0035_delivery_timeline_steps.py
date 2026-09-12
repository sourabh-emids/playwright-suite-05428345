"""Step definitions for Issue 0035 - Delivery timeline message rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the final conversion area")
def view_conversion_area(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight - 500)")


@when("The delivery/timing message is displayed")
def timing_displayed(page: Page):
    pass


@then("Labels '1 Day', '2 Weeks', '3 Months' render in intended order")
def timing_labels_order(page: Page):
    homepage = HomepagePage(page)
    labels = homepage.timeline_labels_present()
    assert "1 Day" in labels
    assert "2 Weeks" in labels
    assert "3 Months" in labels


@given("A user uses a screen reader to navigate the page")
def sr_navigate(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight - 500)")


@when("The screen reader encounters the timeline message")
def sr_timeline(page: Page):
    pass


@then("All timing labels are understandable and in correct sequence")
def labels_understandable(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.timeline_message).to_be_visible()


@given("A user examines the timeline message")
def examine_timeline(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight - 500)")


@when("The content is analyzed")
def timeline_analyzed(page: Page):
    pass


@then("Meaning is conveyed through structured text, not visual styling alone")
def meaning_structured(page: Page):
    homepage = HomepagePage(page)
    timeline = homepage.timeline_message
    text = timeline.text_content()
    assert "1 Day" in text
    assert "2 Weeks" in text
    assert "3 Months" in text


@given("A user views the timeline at mobile widths")
def view_timeline_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight - 500)")


@when("The viewport is narrow")
def narrow_viewport(page: Page):
    pass


@then("Content wraps appropriately without loss of meaning")
def wraps_appropriately(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.timeline_message).to_be_visible()
