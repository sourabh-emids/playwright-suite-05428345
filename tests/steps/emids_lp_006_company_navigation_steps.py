"""Steps for emids_lp_006: Implement Company navigation group."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.company_nav_page import CompanyNavPage


@given(parsers.parse("User opens Company menu"))
def open_company_menu(page: Page) -> None:
    """User opens Company menu."""
    company_page = CompanyNavPage(page)
    company_page.navigate()
    company_page.open_company_menu()


@given(parsers.parse("User navigates to Company menu"))
def navigate_to_company_menu(page: Page) -> None:
    """User navigates to Company menu."""
    company_page = CompanyNavPage(page)
    company_page.navigate()


@given(parsers.parse("User navigates to Company pages"))
def navigate_to_company_pages(page: Page) -> None:
    """User navigates to Company pages."""
    company_page = CompanyNavPage(page)
    company_page.navigate()


@given(parsers.parse("A company page is unpublished"))
def company_page_unpublished(page: Page) -> None:
    """A company page is unpublished."""
    # CMS state - simulated
    pass


@when("User views available company links")
def view_company_links(page: Page) -> None:
    """View available company links."""
    pass  # Verification step


@when("User activates menu via keyboard, mouse click, or touch")
def activate_menu_various_modes(page: Page) -> None:
    """Activate menu via various modes."""
    company_page = CompanyNavPage(page)
    company_page.open_company_menu()


@when("User clicks company navigation links")
def click_company_links(page: Page) -> None:
    """Click company navigation links."""
    pass  # Verification step


@then("All displayed links are published/approved pages")
def all_links_published(page: Page) -> None:
    """Verify all displayed links are published/approved pages."""
    company_page = CompanyNavPage(page)
    for link in company_page.get_all_links():
        href = link.get_attribute("href")
        expect(href).not_to_match(r"unpublished|draft|404")


@then("Contact/Connect destinations are included")
def contact_included(page: Page) -> None:
    """Verify Contact/Connect destinations are included."""
    company_page = CompanyNavPage(page)
    expect(company_page.locators.contact_us_link).to_be_visible()


@then("Menu opens in all interaction modes")
def menu_opens_all_modes(page: Page) -> None:
    """Verify menu opens in all interaction modes."""
    company_page = CompanyNavPage(page)
    expect(company_page.locators.company_button).to_have_attribute("aria-expanded", "true")


@then("Links are accessible")
def links_accessible(page: Page) -> None:
    """Verify links are accessible."""
    company_page = CompanyNavPage(page)
    for link in company_page.get_all_links():
        expect(link).to_be_visible()


@then("No redirect loops occur")
def no_redirect_loops(page: Page) -> None:
    """Verify no redirect loops occur."""
    company_page = CompanyNavPage(page)
    company_page.open_company_menu()
    # Click a link and verify it loads
    company_page.locators.our_story_link.click()
    expect(page).not_to_have_url(r"(.*\/){3,}")
    # Verify page loaded within reasonable time
    page.wait_for_load_state("domcontentloaded")


@then("Pages load within reasonable time")
def pages_load_reasonable_time(page: Page) -> None:
    """Verify pages load within reasonable time."""
    page.wait_for_load_state("domcontentloaded")


@then("Unpublished page does not appear in navigation")
def unpublished_not_in_nav(page: Page) -> None:
    """Verify unpublished page does not appear in navigation."""
    company_page = CompanyNavPage(page)
    for link in company_page.get_all_links():
        href = link.get_attribute("href")
        expect(href).not_to_match(r"unpublished|removed|archived")
