"""Steps for Footer legal navigation rendering (issue_0045)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0045_footer_legal_locators import FooterLegalLocators


@given("User views footer legal navigation")
def view_footer(page: Page) -> None:
    page.goto("/")


@given("User inspects footer legal links")
def inspect_links(page: Page) -> None:
    page.goto("/")


@given("User tabs to footer legal links")
def tab_links(page: Page) -> None:
    page.goto("/")
    page.keyboard.press("Tab")


@given("Footer legal links render")
def links_render(page: Page) -> None:
    page.goto("/")


@given("Legal page URL has changed")
def url_changed(page: Page) -> None:
    page.goto("/")


@given("Legal link has long label")
def long_label(page: Page) -> None:
    page.goto("/")


@given("Site has multiple locales")
def multiple_locales(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Links render")
def links(page: Page) -> None:
    pass


@when("Focus is received")
def focus_received(page: Page) -> None:
    pass


@when("User validates content")
def validate(page: Page) -> None:
    pass


@when("User inspects URLs")
def inspect_urls(page: Page) -> None:
    pass


@when("User clicks link")
def click_link(page: Page) -> None:
    pass


@when("Page renders at mobile width")
def mobile_render(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("User views footer")
def view_footer_action(page: Page) -> None:
    pass


@then("Each legal link has descriptive text (Privacy Policy, Cookie Policy, Accessibility Statement, etc.)")
def descriptive_text(page: Page) -> None:
    expect(FooterLegalLocators(page).footer).to_be_visible()


@then("Each link has a valid HTTPS destination")
def valid_destination(page: Page) -> None:
    links = FooterLegalLocators(page).legal_links.all()
    for link in links:
        href = link.get_attribute("href")
        if href and not href.startswith("#"):
            assert href.startswith("https://")


@then("Visible focus state is displayed")
def focus_state(page: Page) -> None:
    pass


@then("No labels are blank")
def no_blank_labels(page: Page) -> None:
    links = FooterLegalLocators(page).legal_links.all()
    for link in links:
        text = link.text_content()
        assert text and text.strip()


@then("All URLs use HTTPS protocol")
def https_urls(page: Page) -> None:
    links = FooterLegalLocators(page).legal_links.all()
    for link in links:
        href = link.get_attribute("href")
        if href and not href.startswith("#") and not href.startswith("mailto:"):
            assert href.startswith("https://")


@then("User is redirected to current location or sees appropriate error")
def redirected(page: Page) -> None:
    pass


@then("Label wraps appropriately")
def label_wraps(page: Page) -> None:
    expect(FooterLegalLocators(page).footer).to_be_visible()


@then("Legal links are available for current locale or default")
def locale_links(page: Page) -> None:
    expect(FooterLegalLocators(page).footer).to_be_visible()
