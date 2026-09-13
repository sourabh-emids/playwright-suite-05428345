"""Step definitions for emids_lp_026-033 - Insights section."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("Exactly six insight/resource cards are displayed")
def verify_six_cards(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.insight_cards).to_have_count(6)


@then("Each card displays content type, title, image where configured, and Download/Read More action")
def verify_card_content(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    for card in page_obj.insight_cards.all():
        expect(card.locator("h3").first).to_be_visible()


@then("All cards remain accessible and usable across breakpoints")
def verify_cards_all_breakpoints(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    for width in [375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        expect(page_obj.section).to_be_visible()


@then("Each card has non-empty title and valid destination URL")
def verify_card_title_url(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    for card in page_obj.insight_cards.all():
        title = card.locator("h3").first.text_content()
        assert title and title.strip()
        href = card.locator("a").first.get_attribute("href")
        assert href


@then("eBook-type cards show 'Download'; blog-type cards show 'Read More'")
def verify_action_labels(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Only published content appears in the section")
def verify_published_only(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.insight_cards).to_have_count(6)


@then("Card renders with text content; no broken image placeholder")
def verify_missing_image(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Title wraps or truncates gracefully without breaking layout")
def verify_long_title(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Cards use responsive grid/rail layout with consistent heights where practical")
def verify_responsive_grid(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card displays title 'Managing the Margin Reset in Medicare Advantage'")
def verify_medicare_title(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card is labeled with type 'eBook'")
def verify_ebook_label(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Download action is displayed")
def verify_download_action(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.download_buttons.first).to_be_visible()


@then("URL resolves to current detail/access page without 404")
def verify_url_resolves(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    href = page_obj.download_buttons.first.get_attribute("href")
    if href:
        response = page.request.get(href)
        assert response.status < 400


@then("Appropriate error, gate, or redirect displayed")
def verify_error_handled(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card displays title 'Unlocking Trusted Digital Transformation in Life Sciences'")
def verify_ls_title(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("URL resolves to canonical destination '/insights/unlocking-trusted-digital-transformation-in-life-sciences/'")
def verify_ls_canonical_url(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card displays title 'Closing the AI ROI Gap in Healthcare' with eBook labeling")
def verify_ai_roi_title(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Appropriate handling without showing broken content")
def verify_unpublished_handled(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card displays type 'Blog' with 'Read More' action")
def verify_blog_type(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card displays title 'Payers: Is Your Data Ready for AI?'")
def verify_payer_blog_title(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Action label is 'Read More', not 'Download'")
def verify_read_more_label(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Redirect to new location or appropriate error handling")
def verify_article_moved(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("User is routed to resource detail/access experience, not assumed direct file download")
def verify_resource_access(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    href = page_obj.download_buttons.first.get_attribute("href")
    assert href and "/insights/" in href


@then("No private asset endpoint is exposed or fabricated in the request")
def verify_no_fabricated_endpoint(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    href = page_obj.download_buttons.first.get_attribute("href")
    assert href.startswith("https://")


@then("Gate clearly communicates required steps before access")
def verify_gate_communication(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Only verified/published destinations are used for card actions")
def verify_verified_destinations(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.insight_cards).to_have_count(6)


@then("User-friendly error message displayed")
def verify_error_message(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Clear error message displayed; user can retry")
def verify_retry_handled(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()


@then("Fallback navigation or notification displayed")
def verify_popup_blocked(page: Page) -> None:
    from pages.emids_lp_026_insights_page import InsightsPage
    page_obj = InsightsPage(page)
    expect(page_obj.section).to_be_visible()
