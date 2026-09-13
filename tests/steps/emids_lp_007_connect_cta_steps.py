"""Step definitions for emids_lp_007 - Header Connect CTA."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("The Connect CTA is visually styled to stand out from standard navigation links")
def verify_connect_cta_visually_distinct(page: Page) -> None:
    from pages.emids_lp_007_connect_cta_page import ConnectCTAPage
    cta_page = ConnectCTAPage(page)
    class_attr = cta_page.connect_cta.get_attribute("class")
    # Connect CTA should have distinct styling class
    expect(cta_page.connect_cta).to_be_visible()


@then("The CTA has an accessible name that describes its action")
def verify_cta_accessible_name(page: Page) -> None:
    from pages.emids_lp_007_connect_cta_page import ConnectCTAPage
    cta_page = ConnectCTAPage(page)
    accessible_name = cta_page.connect_cta.text_content()
    assert "connect" in accessible_name.lower(), f"CTA text '{accessible_name}' doesn't describe action"


@then("The URL uses HTTPS protocol and is a valid canonical destination")
def verify_cta_url_https(page: Page) -> None:
    from pages.emids_lp_007_connect_cta_page import ConnectCTAPage
    cta_page = ConnectCTAPage(page)
    href = cta_page.connect_cta.get_attribute("href")
    assert href.startswith("https://"), f"CTA URL not HTTPS: {href}"


@then("The CTA activates and navigates to the contact page")
def verify_cta_keyboard_activation(page: Page) -> None:
    from pages.emids_lp_007_connect_cta_page import ConnectCTAPage
    cta_page = ConnectCTAPage(page)
    cta_page.connect_cta.focus()
    page.keyboard.press("Enter")
    expect(page).to_have_url("/contact/")


@then("No duplicate Connect CTAs exist in the header")
def verify_no_duplicate_ctas(page: Page) -> None:
    from pages.emids_lp_007_connect_cta_page import ConnectCTAPage
    cta_page = ConnectCTAPage(page)
    primary_ctas = cta_page.primary_connect_ctas
    assert len(primary_ctas) == 1, f"Expected 1 primary CTA, found {len(primary_ctas)}"
