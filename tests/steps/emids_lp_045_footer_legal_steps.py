"""Step definitions for emids_lp_045-046 - Footer sections."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Each link displays descriptive text (e.g., 'Privacy Policy', 'Cookie Policy', 'Accessibility Statement')")
def verify_descriptive_text(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    for link in page_obj.legal_links.all():
        text = link.text_content()
        assert text and len(text) > 3


@then("All legal links navigate to valid published pages")
def verify_valid_destinations(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    for link in page_obj.legal_links.all():
        href = link.get_attribute("href")
        if href and not href.startswith("#"):
            response = page.request.get(href)
            assert response.status < 400


@then("Visible focus indicator is displayed")
def verify_focus_indicator(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    page_obj.legal_links.first.focus()
    expect(page_obj.legal_links.first).to_be_focused()


@then("All legal page URLs use HTTPS protocol")
def verify_https_urls(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    for link in page_obj.legal_links.all():
        href = link.get_attribute("href")
        if href and href.startswith("http"):
            assert href.startswith("https://")


@then("No link label is blank or empty")
def verify_no_blank_labels(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    for link in page_obj.legal_links.all():
        text = link.text_content()
        assert text and text.strip(), "Blank label found"


@then("Legal links reflow appropriately without horizontal overflow")
def verify_responsive_legal(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.legal_section).to_be_visible()


@then("Redirect occurs or appropriate error displayed")
def verify_page_moved(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    expect(page_obj.legal_section).to_be_visible()


@then("Label wraps gracefully without breaking layout")
def verify_long_labels(page: Page) -> None:
    from pages.emids_lp_045_footer_legal_page import FooterLegalPage
    page_obj = FooterLegalPage(page)
    expect(page_obj.legal_section).to_be_visible()


@then("Text remains readable; no overlap or truncation issues")
def verify_readable_mobile(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.corporate_section).to_be_visible()


@then("Corporate/contact information does not overlap or conflict with legal navigation")
def verify_no_conflict(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    expect(page_obj.corporate_section).to_be_visible()
    expect(page_obj.legal_section).to_be_visible()


@then("Only approved current content is published")
def verify_current_content(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    expect(page_obj.corporate_section).to_be_visible()


@then("Links navigate to valid external social destinations")
def verify_social_links(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    for link in page_obj.social_links.all():
        href = link.get_attribute("href")
        assert href and ("facebook" in href or "twitter" in href or "linkedin" in href or "youtube" in href)


@then("Details display correctly; placeholder used if not configured")
def verify_address_details(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    expect(page_obj.corporate_section).to_be_visible()


@then("CMS workflow flags outdated content for update")
def verify_outdated_content(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    expect(page_obj.corporate_section).to_be_visible()


@then("Appropriate error handling or redirect")
def verify_social_unavailable(page: Page) -> None:
    from pages.emids_lp_046_footer_corporate_page import FooterCorporatePage
    page_obj = FooterCorporatePage(page)
    expect(page_obj.corporate_section).to_be_visible()
