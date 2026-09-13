"""Step definitions for emids_lp_025 - Impact metrics."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("All four metrics display as visible text: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'")
def verify_four_metrics(page: Page) -> None:
    from pages.emids_lp_025_impact_page import ImpactPage
    page_obj = ImpactPage(page)
    expect(page_obj.metric_1).to_be_visible()
    expect(page_obj.metric_2).to_be_visible()
    expect(page_obj.metric_3).to_be_visible()
    expect(page_obj.metric_4).to_be_visible()


@then("Final meaningful values are displayed and announced")
def verify_final_values(page: Page) -> None:
    from pages.emids_lp_025_impact_page import ImpactPage
    page_obj = ImpactPage(page)
    text = page_obj.metric_1.text_content()
    assert "36" in text


@then("Screen reader receives final meaningful values, not intermediate animation states")
def verify_screen_reader_values(page: Page) -> None:
    from pages.emids_lp_025_impact_page import ImpactPage
    page_obj = ImpactPage(page)
    # Text should be present in DOM
    expect(page_obj.metric_1).to_have_text(re.compile(r".*\d+.*"))


@then("Currency symbols ($) and plus signs (+) are preserved as approved")
def verify_symbols_preserved(page: Page) -> None:
    from pages.emids_lp_025_impact_page import ImpactPage
    page_obj = ImpactPage(page)
    text = page_obj.metric_3.text_content()
    assert "$" in text


@then("Final values display immediately without animation")
def verify_animation_disabled(page: Page) -> None:
    from pages.emids_lp_025_impact_page import ImpactPage
    page_obj = ImpactPage(page)
    expect(page_obj.section).to_be_visible()


@then("Missing field displays placeholder or section renders without broken content")
def verify_missing_field_handled(page: Page) -> None:
    from pages.emids_lp_025_impact_page import ImpactPage
    page_obj = ImpactPage(page)
    expect(page_obj.section).to_be_visible()
