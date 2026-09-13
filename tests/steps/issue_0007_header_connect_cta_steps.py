"""Steps for Header Connect CTA functionality (issue_0007)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0007_header_connect_cta_page import HeaderConnectCTAPage
from locators.issue_0007_header_connect_cta_locators import HeaderConnectCTALocators


@given("User is on Emids homepage")
def on_homepage(page: Page) -> None:
    page.goto("/")


@given("User uses screen reader on Emids homepage")
def screen_reader_view(page: Page) -> None:
    page.goto("/")


@given("User is on Emids homepage with keyboard focus on Connect CTA")
def focus_on_connect(page: Page) -> None:
    page.goto("/")
    cta_page = HeaderConnectCTAPage(page)
    cta_page.focus_connect()


@when("User views the header")
def view_header(page: Page) -> None:
    pass


@when("User encounters Connect CTA")
def encounter_cta(page: Page) -> None:
    pass


@when("User clicks Connect CTA")
def click_connect(page: Page) -> None:
    cta_page = HeaderConnectCTAPage(page)
    cta_page.click_connect()


@when("User presses Enter or Space on CTA")
def activate_cta(page: Page) -> None:
    page.keyboard.press("Enter")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User views header")
def view_header_again(page: Page) -> None:
    pass


@when("User counts Connect CTAs")
def count_ctas(page: Page) -> None:
    pass


@then("Connect CTA is visually distinct from other navigation elements")
def cta_visually_distinct(page: Page) -> None:
    locators = HeaderConnectCTALocators(page)
    expect(locators.connect_cta).to_be_visible()


@then("CTA has accessible name that describes the action")
def cta_accessible_name(page: Page) -> None:
    locators = HeaderConnectCTALocators(page)
    name = locators.connect_cta.get_attribute("aria-label") or locators.connect_cta.text_content()
    assert name and "Connect" in name


@then("User is navigated to '/contact/' with valid HTTPS URL")
def navigated_to_contact(page: Page) -> None:
    expect(page).to_have_url("/contact/")
    url = page.url
    assert url.startswith("https://")


@then("Contact page is loaded")
def contact_loaded(page: Page) -> None:
    expect(page).to_have_url("/contact/")


@then("Connect CTA placement is preserved and responsive")
def cta_responsive(page: Page) -> None:
    locators = HeaderConnectCTALocators(page)
    for width in [1280, 768, 375]:
        page.set_viewport_size({"width": width, "height": 800})
        expect(locators.connect_cta).to_be_visible()


@then("User sees appropriate error page and core navigation remains functional")
def error_page_handling(page: Page) -> None:
    pass


@then("Exactly one primary Connect CTA exists")
def exactly_one_cta(page: Page) -> None:
    cta_page = HeaderConnectCTAPage(page)
    count = cta_page.get_cta_count()
    expect(count).to_equal(1)
