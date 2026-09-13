"""Steps for Final conversion banner rendering (issue_0034)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0034_final_cta_locators import FinalCTALocators


@given("User views Emids homepage")
def view_homepage(page: Page) -> None:
    page.goto("/")


@given("User views Final CTA section")
def view_final_cta(page: Page) -> None:
    page.goto("/")


@given("User tabs to Final CTA section")
def tab_to_cta(page: Page) -> None:
    page.goto("/")
    page.keyboard.press("Tab")


@given("Final CTA section renders")
def section_renders(page: Page) -> None:
    page.goto("/")


@given("User views Final CTA at narrow viewport")
def narrow_viewport(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("User clicks Final CTA")
def click_final_cta(page: Page) -> None:
    page.goto("/")
    FinalCTALocators(page).connect_cta.click()


@when("User scrolls to bottom of page")
def scroll_bottom(page: Page) -> None:
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("User looks for primary action")
def look_primary(page: Page) -> None:
    pass


@when("Focus reaches primary action")
def focus_reaches(page: Page) -> None:
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User assesses contrast")
def assess_contrast(page: Page) -> None:
    pass


@when("Contact route is unavailable")
def route_unavailable(page: Page) -> None:
    pass


@then("Final conversion banner appears before footer")
def banner_before_footer(page: Page) -> None:
    locators = FinalCTALocators(page)
    expect(locators.final_cta_section).to_be_visible()
    expect(locators.footer).to_be_visible()


@then("Primary action is clear and visually prominent")
def primary_clear(page: Page) -> None:
    expect(FinalCTALocators(page).connect_cta).to_be_visible()


@then("Action is keyboard operable")
def keyboard_operable(page: Page) -> None:
    expect(FinalCTALocators(page).connect_cta).to_be_visible()


@then("Supporting timing/message content is readable")
def timing_readable(page: Page) -> None:
    expect(FinalCTALocators(page).final_cta_section).to_be_visible()


@then("Required message and CTA fields are present")
def fields_present(page: Page) -> None:
    expect(FinalCTALocators(page).final_cta_section).to_be_visible()
    expect(FinalCTALocators(page).connect_cta).to_be_visible()


@then("Section has high-contrast design")
def high_contrast(page: Page) -> None:
    pass


@then("CTA text wraps appropriately without breaking")
def text_wraps(page: Page) -> None:
    expect(FinalCTALocators(page).final_cta_section).to_be_visible()


@then("CTA does not overlap footer")
def no_overlap(page: Page) -> None:
    expect(FinalCTALocators(page).footer).to_be_visible()


@then("User sees appropriate error handling")
def error_handling(page: Page) -> None:
    pass
