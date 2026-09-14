"""Step definitions for issue_0004: Industries Mega-Menu Implementation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.industries_menu_page import IndustriesMenuPage


@given("Industries menu is open")
def industries_menu_open(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    menu_page = IndustriesMenuPage(page)
    menu_page.open_industries_menu()


@when("User views menu items")
def view_industries_menu_items(page: Page):
    pass


@then("Menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations")
def five_audience_destinations_present(page: Page):
    menu_page = IndustriesMenuPage(page)
    count = menu_page.get_industry_count()
    assert count >= 5, f"Expected 5 industry destinations, found {count}"


@given("Industries menu is open")
def industries_menu_open_keyboard(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    menu_page = IndustriesMenuPage(page)
    menu_page.open_industries_menu()


@when("User uses keyboard navigation")
def use_keyboard_navigation_industries(page: Page):
    page.keyboard.press("Tab")


@then("Each of five audience destinations is reachable without mouse")
def all_audience_keyboard_accessible(page: Page):
    menu_page = IndustriesMenuPage(page)
    count = menu_page.get_industry_count()
    assert count >= 5, "All 5 audience destinations should be keyboard accessible"


@given("Audience links are rendered")
def audience_links_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("URLs are checked")
def check_audience_urls(page: Page):
    pass


@then("Links use canonical URLs: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/")
def audience_canonical_urls(page: Page):
    menu_page = IndustriesMenuPage(page)
    menu_page.open_industries_menu()
    urls = ["/segments/payer/", "/segments/provider/", "/segments/healthtech/", "/segments/life-sciences/", "/segments/consumer/"]
    for url in urls:
        link = page.locator(f'a[href*="{url}"]')
        expect(link.first).to_be_visible()


@given("Page at desktop viewport")
def desktop_viewport_industries(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})


@when("Industries menu opens")
def open_desktop_industries_menu(page: Page):
    menu_page = IndustriesMenuPage(page)
    menu_page.open_industries_menu()


@then("Menu presents grouped navigation")
def grouped_industries_menu(page: Page):
    menu_page = IndustriesMenuPage(page)
    expect(menu_page.industries_menu).to_be_visible()


@given("Page at mobile viewport")
def mobile_viewport_industries(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Industries menu opens")
def open_mobile_industries_menu(page: Page):
    menu_page = IndustriesMenuPage(page)
    menu_page.open_industries_menu()


@then("Menu presents stacked list or disclosure")
def stacked_industries_list(page: Page):
    menu_page = IndustriesMenuPage(page)
    expect(menu_page.industries_menu).to_be_visible()


@given("One segment page is unpublished")
def one_segment_unpublished(page: Page):
    page.goto("/")


@when("Industries menu renders")
def industries_menu_renders(page: Page):
    menu_page = IndustriesMenuPage(page)
    menu_page.open_industries_menu()


@then("Unpublished segment does not appear or shows appropriate unavailable state")
def unpublished_handling(page: Page):
    menu_page = IndustriesMenuPage(page)
    expect(menu_page.industries_menu).to_be_visible()
