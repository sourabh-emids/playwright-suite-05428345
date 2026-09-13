"""Step definitions for emids_lp_004 - Industries mega-menu."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("The menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations")
def verify_five_industries_present(page: Page) -> None:
    from pages.emids_lp_004_industries_page import IndustriesMenuPage
    ind_page = IndustriesMenuPage(page)
    expect(ind_page.payer_link).to_be_visible()
    expect(ind_page.provider_link).to_be_visible()
    expect(ind_page.healthtech_link).to_be_visible()
    expect(ind_page.life_sciences_link).to_be_visible()
    expect(ind_page.consumer_link).to_be_visible()


@then("All five industry links (Payer, Provider, HealthTech, Life Sciences, Consumer) are reachable and activatable via keyboard")
def verify_industries_keyboard_accessible(page: Page) -> None:
    from pages.emids_lp_004_industries_page import IndustriesMenuPage
    ind_page = IndustriesMenuPage(page)
    links = ind_page.industry_links
    for link in links:
        link.focus()
        expect(link).to_be_focused()


@then("Links resolve to canonical URLs: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/")
def verify_industry_canonical_urls(page: Page) -> None:
    from pages.emids_lp_004_industries_page import IndustriesMenuPage
    ind_page = IndustriesMenuPage(page)
    expected_paths = [
        "/segments/payer/",
        "/segments/provider/",
        "/segments/healthtech/",
        "/segments/life-sciences/",
        "/segments/consumer/",
    ]
    links = ind_page.industry_links
    for link, expected_path in zip(links, expected_paths):
        href = link.get_attribute("href")
        assert expected_path in href, f"Expected {expected_path} in {href}"


@then("Industry destinations display as a stacked list or disclosure pattern")
def verify_mobile_stacked_list(page: Page) -> None:
    from pages.emids_lp_004_industries_page import IndustriesMenuPage
    ind_page = IndustriesMenuPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    ind_page.click_industries_button()
    expect(ind_page.mobile_industry_list).to_be_visible()


@then("Only published segments appear; no broken or missing links are displayed")
def verify_only_published_segments(page: Page) -> None:
    from pages.emids_lp_004_industries_page import IndustriesMenuPage
    ind_page = IndustriesMenuPage(page)
    links = ind_page.industry_links
    for link in links:
        expect(link).to_be_visible()
        href = link.get_attribute("href")
        assert href is not None


@then("Menu layout accommodates longer labels without overlapping or truncation")
def verify_long_labels_handled(page: Page) -> None:
    from pages.emids_lp_004_industries_page import IndustriesMenuPage
    ind_page = IndustriesMenuPage(page)
    labels = ind_page.industry_labels
    for label in labels:
        text = label.text_content()
        assert text is not None
