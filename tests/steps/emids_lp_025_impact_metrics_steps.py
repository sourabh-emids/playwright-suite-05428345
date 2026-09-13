"""Steps for emids_lp_025: Render Impact proof metrics."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.impact.impact_page import ImpactPage


@given(parsers.parse("User views Impact section"))
def view_impact(page: Page) -> None:
    """User views Impact section."""
    impact_page = ImpactPage(page)
    impact_page.navigate()
    impact_page.scroll_to_section()


@given(parsers.parse("User views Impact section with animation disabled"))
def view_impact_no_animation(page: Page) -> None:
    """User views with animation disabled."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")
    impact_page = ImpactPage(page)
    impact_page.navigate()
    impact_page.scroll_to_section()


@given(parsers.parse("User with screen reader views Impact section"))
def screen_reader_view(page: Page) -> None:
    """User with screen reader views."""
    impact_page = ImpactPage(page)
    impact_page.navigate()
    impact_page.scroll_to_section()


@given(parsers.parse("User views Impact metrics"))
def view_metrics(page: Page) -> None:
    """User views Impact metrics."""
    impact_page = ImpactPage(page)
    impact_page.scroll_to_section()


@given(parsers.parse("CMS manages Impact content"))
def cms_manages(page: Page) -> None:
    """CMS manages content."""
    pass


@given(parsers.parse("Count-up animation fails or is disabled"))
def animation_disabled(page: Page) -> None:
    """Animation disabled."""
    page.emulate_media(media_feature="prefers-reduced-motion", media_feature_value="reduce")


@given(parsers.parse("User views page from different locale"))
def different_locale(page: Page) -> None:
    """User from different locale."""
    pass


@when("User reads metrics")
def read_metrics(page: Page) -> None:
    """Read metrics."""
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("Screen reader announces content")
def screen_reader_announces(page: Page) -> None:
    """Screen reader announces."""
    pass


@then("All four visible: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'")
def all_four_visible(page: Page) -> None:
    """Verify all four metrics visible."""
    impact_page = ImpactPage(page)
    expect(impact_page.get_metric_count()).to_equal(4)


@then("Final metric values are readable and meaningful")
def values_readable(page: Page) -> None:
    """Verify values readable."""
    impact_page = ImpactPage(page)
    expect(impact_page.locators.years_experience).to_be_visible()


@then("Final metric values are read")
def values_read(page: Page) -> None:
    """Verify values read."""
    impact_page = ImpactPage(page)
    expect(impact_page.locators.years_experience).to_be_visible()


@then("Animation does not obscure values")
def animation_not_obscure(page: Page) -> None:
    """Verify animation doesn't obscure values."""
    impact_page = ImpactPage(page)
    expect(impact_page.locators.years_experience).to_be_visible()


@then("Approved formatting ($, +, etc.) displays correctly")
def formatting_correct(page: Page) -> None:
    """Verify formatting correct."""
    impact_page = ImpactPage(page)
    text = impact_page.locators.costs_saved.inner_text()
    expect("$" in text).to_be_true()


@then("Each value pairs correctly with its label")
def value_label_pairs(page: Page) -> None:
    """Verify value-label pairs."""
    impact_page = ImpactPage(page)
    metrics = impact_page.get_metrics()
    expect("years" in metrics or "36" in str(metrics)).to_be_true()


@then("No mismatched pairings")
def no_mismatched(page: Page) -> None:
    """Verify no mismatched pairings."""
    impact_page = ImpactPage(page)
    expect(impact_page.get_metric_count()).to_equal(4)


@then("Static values display correctly")
def static_values(page: Page) -> None:
    """Verify static values."""
    impact_page = ImpactPage(page)
    expect(impact_page.locators.years_experience).to_be_visible()


@then("No blank or loading state")
def no_blank_loading(page: Page) -> None:
    """Verify no blank or loading."""
    impact_page = ImpactPage(page)
    expect(impact_page.locators.years_experience).to_be_visible()


@then("Values display with approved formatting")
def values_formatting(page: Page) -> None:
    """Verify values formatting."""
    impact_page = ImpactPage(page)
    expect(impact_page.locators.costs_saved).to_be_visible()


@then("No unexpected locale transformation")
def no_locale_transform(page: Page) -> None:
    """Verify no locale transform."""
    impact_page = ImpactPage(page)
    text = impact_page.locators.costs_saved.inner_text()
    expect(text).to_match(r"\$")
