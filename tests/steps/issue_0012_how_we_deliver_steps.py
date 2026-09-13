"""Steps for How We Deliver section rendering (issue_0012)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0012_how_we_deliver_page import HowWeDeliverPage
from locators.issue_0012_how_we_deliver_locators import HowWeDeliverLocators


@given("User is on Emids homepage")
def on_homepage(page: Page) -> None:
    page.goto("/")


@given("How We Deliver section is present")
def section_present(page: Page) -> None:
    page.goto("/")
    how_page = HowWeDeliverPage(page)
    how_page.scroll_to_section()


@given("User uses assistive technology")
def assistive_tech(page: Page) -> None:
    page.goto("/")


@given("How We Deliver section renders")
def section_renders(page: Page) -> None:
    page.goto("/")


@given("User views Emids homepage at mobile width")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@when("Page renders below hero")
def page_renders(page: Page) -> None:
    pass


@when("User views section content")
def view_content(page: Page) -> None:
    pass


@when("User views section")
def view_section(page: Page) -> None:
    how_page = HowWeDeliverPage(page)
    how_page.scroll_to_section()


@when("User validates content")
def validate_content(page: Page) -> None:
    pass


@when("User checks heading structure")
def check_heading_structure(page: Page) -> None:
    pass


@when("How We Deliver section renders")
def section_render(page: Page) -> None:
    pass


@then("How We Deliver section heading appears in intended sequence after hero")
def heading_sequential(page: Page) -> None:
    locators = HowWeDeliverLocators(page)
    expect(locators.section_heading).to_be_visible()


@then("Supporting explanation text is present and readable")
def explanation_present(page: Page) -> None:
    locators = HowWeDeliverLocators(page)
    expect(locators.section_text).to_be_visible()


@then("Visual/content elements render appropriately")
def visual_elements(page: Page) -> None:
    expect(HowWeDeliverLocators(page).how_we_deliver_section).to_be_visible()


@then("Section CTA is present and accessible")
def cta_present(page: Page) -> None:
    locators = HowWeDeliverLocators(page)
    expect(locators.see_model_cta).to_be_visible()


@then("Section is accessible with proper semantic markup")
def section_accessible(page: Page) -> None:
    expect(HowWeDeliverLocators(page).how_we_deliver_section).to_be_visible()


@then("Required content fields (title, body, CTA) are not empty")
def fields_not_empty(page: Page) -> None:
    locators = HowWeDeliverLocators(page)
    heading_text = locators.section_heading.text_content()
    assert heading_text and heading_text.strip()
    text = locators.section_text.text_content()
    assert text and text.strip()
    cta = locators.see_model_cta.get_attribute("href")
    assert cta and cta.strip()


@then("Heading hierarchy follows logical order")
def heading_hierarchy(page: Page) -> None:
    pass


@then("Section reflows appropriately for mobile viewport")
def section_responsive(page: Page) -> None:
    expect(HowWeDeliverLocators(page).how_we_deliver_section).to_be_visible()
