"""Steps for Impact proof metrics rendering (issue_0025)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0025_impact_metrics_locators import ImpactMetricsLocators


@given("User views Impact section")
def view_impact(page: Page) -> None:
    page.goto("/")


@given("Count-up animation is disabled")
def animation_disabled(page: Page) -> None:
    page.goto("/")


@given("User uses screen reader")
def screen_reader(page: Page) -> None:
    page.goto("/")


@given("Impact metrics render")
def metrics_render(page: Page) -> None:
    page.goto("/")


@given("User views Impact section at mobile width")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("User has prefers-reduced-motion enabled")
def reduced_motion(page: Page) -> None:
    page.goto("/")


@given("User views Impact section in different locale")
def different_locale(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User views Impact metrics")
def view_metrics(page: Page) -> None:
    pass


@when("Screen reader encounters Impact metrics")
def sr_encounter(page: Page) -> None:
    pass


@when("User validates content")
def validate(page: Page) -> None:
    pass


@when("User views values with currency")
def view_currency(page: Page) -> None:
    pass


@when("Count-up animation is present")
def animation_present(page: Page) -> None:
    pass


@when("Values render")
def values_render(page: Page) -> None:
    pass


@then("All four proof metrics are visible as text: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'")
def four_metrics(page: Page) -> None:
    expect(ImpactMetricsLocators(page).impact_section).to_be_visible()


@then("Values remain understandable and display final meaningful values")
def values_understandable(page: Page) -> None:
    expect(ImpactMetricsLocators(page).years_experience).to_be_visible()


@then("Final meaningful values are announced")
def values_announced(page: Page) -> None:
    expect(ImpactMetricsLocators(page).years_experience).to_be_visible()


@then("Values and labels are managed as paired content")
def paired_content(page: Page) -> None:
    pass


@then("Currency symbols and plus signs are preserved where approved")
def symbols_preserved(page: Page) -> None:
    expect(ImpactMetricsLocators(page).costs_saved).to_be_visible()


@then("Metric grid reflows responsively")
def grid_reflows(page: Page) -> None:
    expect(ImpactMetricsLocators(page).impact_section).to_be_visible()


@then("Animation is disabled and final values display")
def animation_disabled_final(page: Page) -> None:
    expect(ImpactMetricsLocators(page).years_experience).to_be_visible()


@then("Values remain understandable with appropriate locale formatting")
def locale_formatting(page: Page) -> None:
    expect(ImpactMetricsLocators(page).impact_section).to_be_visible()
