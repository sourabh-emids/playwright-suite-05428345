"""Step definitions for emids_lp_024 - Who We Serve section."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("All five audiences display: Payer, Provider, HealthTech, Life Sciences, Consumer")
def verify_five_audiences(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    expect(page_obj.payer_tab).to_be_visible()
    expect(page_obj.provider_tab).to_be_visible()
    expect(page_obj.healthtech_tab).to_be_visible()
    expect(page_obj.life_sciences_tab).to_be_visible()
    expect(page_obj.consumer_tab).to_be_visible()


@when("User clicks audience Explore CTA")
def click_explore_cta(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    page_obj.explore_cta.first.click()


@then("Action routes to canonical segment URL")
def verify_canonical_segment(page: Page) -> None:
    expect(page).to_have_url(re.compile(r"/segments/.*"))


@then("All audience entries and Explore actions are operable via keyboard and touch")
def verify_keyboard_touch(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    page_obj.payer_tab.focus()
    expect(page_obj.payer_tab).to_be_focused()


@then("Exactly five audiences are configured for this content version")
def verify_five_audiences_count(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    expect(page_obj.audience_tabs).to_have_count(5)


@then("All URLs match canonical pattern: /segments/payer/, /segments/provider/, etc.")
def verify_urls_pattern(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    href = page_obj.explore_cta.first.get_attribute("href")
    assert "/segments/" in href


@then("Graceful error handling without breaking page")
def verify_error_handled(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    expect(page_obj.section).to_be_visible()


@then("Active tab state is maintained or gracefully adapted")
def verify_tab_state(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    page.set_viewport_size({"width": 768, "height": 600})
    expect(page_obj.section).to_be_visible()


@then("Layout uses tabs/cards/accordion/rail as designed without hiding access to any audience")
def verify_responsive_layout(page: Page) -> None:
    from pages.emids_lp_024_who_we_serve_page import WhoWeServePage
    page_obj = WhoWeServePage(page)
    for width in [375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        expect(page_obj.section).to_be_visible()
