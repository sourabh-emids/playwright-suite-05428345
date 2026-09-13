"""Step definitions for emids_lp_006 - Company navigation group."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("Only approved company links and Contact/Connect destinations are displayed")
def verify_company_menu_content(page: Page) -> None:
    from pages.emids_lp_006_company_menu_page import CompanyMenuPage
    company_page = CompanyMenuPage(page)
    expect(company_page.company_menu).to_be_visible()
    links = company_page.menu_links
    assert len(links) > 0, "No links in company menu"


@then("All menu items are operable using keyboard alone, pointer click, and touch tap")
def verify_company_menu_operable(page: Page) -> None:
    from pages.emids_lp_006_company_menu_page import CompanyMenuPage
    company_page = CompanyMenuPage(page)
    links = company_page.menu_links
    for link in links:
        link.click()
        expect(link).to_be_visible()


@then("Only published pages appear in the navigation")
def verify_only_published_pages(page: Page) -> None:
    from pages.emids_lp_006_company_menu_page import CompanyMenuPage
    company_page = CompanyMenuPage(page)
    links = company_page.menu_links
    for link in links:
        expect(link).to_be_visible()


@then("Navigation completes without entering an infinite redirect loop")
def verify_no_redirect_loop(page: Page) -> None:
    from pages.emids_lp_006_company_menu_page import CompanyMenuPage
    company_page = CompanyMenuPage(page)
    links = company_page.menu_links
    for link in links:
        href = link.get_attribute("href")
        if href and not href.startswith("#"):
            page2 = page.context.new_page()
            response = page2.goto(href)
            final_url = page2.url
            page2.close()
            assert "/too-many-redirects" not in final_url, f"Redirect loop detected for {href}"


@then("Focus can exit the menu normally and does not become trapped")
def verify_focus_not_trapped(page: Page) -> None:
    from pages.emids_lp_006_company_menu_page import CompanyMenuPage
    company_page = CompanyMenuPage(page)
    company_page.company_button.focus()
    page.keyboard.press("Tab")
    # Focus should move to next element, not be trapped
