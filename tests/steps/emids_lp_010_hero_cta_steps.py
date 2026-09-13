"""Step definitions for emids_lp_010 - Hero CTA routing."""
from playwright.sync_api import Page, expect
from pytest_bdd import when, then


@when("The user clicks or activates the hero CTA")
def user_activates_hero_cta(page: Page) -> None:
    from pages.emids_lp_010_hero_cta_page import HeroCTAPage
    hero_cta_page = HeroCTAPage(page)
    hero_cta_page.click_hero_cta()


@then("The CTA resolves to the canonical FDCE URL '/forward-deployed-context-engineering/'")
def verify_fdce_url(page: Page) -> None:
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("Standard browser navigation behavior is preserved (back button works, history updated)")
def verify_browser_navigation_behavior(page: Page) -> None:
    hero_cta_url = page.url
    page.go_back()
    page.go_forward()
    expect(page).to_have_url(hero_cta_url)


@then("The URL uses HTTPS protocol and is canonical")
def verify_cta_url_https_canonical(page: Page) -> None:
    from pages.emids_lp_010_hero_cta_page import HeroCTAPage
    hero_cta_page = HeroCTAPage(page)
    href = hero_cta_page.hero_cta.get_attribute("href")
    assert href.startswith("https://"), f"Not HTTPS: {href}"


@then("CTA behaves as a standard link or button per design specification")
def verify_cta_behavior(page: Page) -> None:
    from pages.emids_lp_010_hero_cta_page import HeroCTAPage
    hero_cta_page = HeroCTAPage(page)
    tag = hero_cta_page.hero_cta.evaluate("el => el.tagName")
    assert tag in ["A", "BUTTON"], f"CTA is neither anchor nor button: {tag}"


@when("The CTA opens in new tab")
def open_cta_new_tab(page: Page) -> None:
    from pages.emids_lp_010_hero_cta_page import HeroCTAPage
    hero_cta_page = HeroCTAPage(page)
    hero_cta_page.hero_cta.click(modifiers=["Control"])


@then("FDCE destination loads correctly in new tab")
def verify_fdce_new_tab(page: Page) -> None:
    # After clicking, new tab should have FDCE URL
    page.wait_for_url("**/forward-deployed-context-engineering/**")
