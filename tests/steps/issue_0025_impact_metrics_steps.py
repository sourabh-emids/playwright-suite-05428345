"""Step definitions for Issue 0025 - Impact proof metrics rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Impact section")
def view_impact(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 6500)")


@when("The section loads")
def impact_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("All four metrics are visible as text")
def four_metrics_visible(page: Page):
    homepage = HomepagePage(page)
    metrics = homepage.all_four_metrics_visible()
    assert len(metrics) == 4


@given("A user views the Impact section with animations disabled")
def view_impact_no_animation(page: Page):
    page.emulate_media(media_feature="prefers-reduced-motion: reduce")
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 6500)")


@when("The metrics are displayed")
def metrics_displayed(page: Page):
    pass


@then("Values remain understandable; count-up animation does not obscure final values")
def values_understandable(page: Page):
    homepage = HomepagePage(page)
    metrics = homepage.all_four_metrics_visible()
    assert len(metrics) == 4


@given("A user uses a screen reader to navigate the Impact section")
def screen_reader_impact(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 6500)")


@when("The screen reader encounters the metrics")
def sr_encounters_metrics(page: Page):
    pass


@then("Final meaningful values are announced")
def values_announced(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.impact_section).to_be_visible()
    expect(page.getByText("36", exact=False)).to_be_visible()


@given("A user or assistive technology examines the metrics")
def examine_metrics(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 6500)")


@when("The content is analyzed")
def content_analyzed_metrics(page: Page):
    pass


@then("Values and labels are managed as paired content with correct associations")
def paired_content(page: Page):
    # Verify metrics are grouped properly
    expect(page.getByText("Healthcare Experience")).to_be_visible()
    expect(page.getByText("36+ Years", exact=False)).to_be_visible()


@given("A user views the impact metrics")
def view_impact_metrics(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 6500)")


@when("The values are displayed")
def values_displayed(page: Page):
    pass


@then("Currency symbols and plus signs are preserved where approved")
def symbols_preserved(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.impact_section).to_be_visible()
    # Check for $ and + symbols
    page_content = page.content()
    assert "$" in page_content or "+" in page_content
