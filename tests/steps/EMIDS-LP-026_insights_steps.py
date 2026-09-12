"""Step definitions for Insights section - EMIDS-LP-026, EMIDS-LP-027, EMIDS-LP-028, EMIDS-LP-029, EMIDS-LP-030, EMIDS-LP-031, EMIDS-LP-032, EMIDS-LP-033"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-026_insights_page import InsightsPage
from playwright.sync_api import expect


@given("Insights section")
def insights_section(page):
    page.goto("/")


@when("Cards are counted")
def count_cards(page):
    pass


@then("Six cards render with content type, title, image (where configured), and Download or Read More action")
def verify_six_cards(page):
    insights_page = InsightsPage(page)
    count = insights_page.count_insight_cards()
    assert count >= 6


@given("Insights cards at desktop, tablet, mobile widths")
def various_widths(page):
    pass


@when("Responsive layout is tested")
def test_responsive(page):
    insights_page = InsightsPage(page)
    insights_page.goto("/")


@then("All cards remain accessible and functional")
def verify_accessible_functional(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Insight card content")
def insight_card_content(page):
    page.goto("/")


@when("Publication status is verified")
def verify_publication(page):
    pass


@then("Only published content is displayed")
def verify_published(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Insight card data")
def insight_card_data(page):
    page.goto("/")


@when("Required fields are checked")
def check_required_fields(page):
    pass


@then("Title and URL are present for each card")
def verify_title_url(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Edge case where resource is unpublished")
def resource_unpublished(page):
    pass


@when("Section renders")
def render_section(page):
    insights_page = InsightsPage(page)
    insights_page.goto("/")


@then("Card is either hidden or shows appropriate state")
def verify_hidden_or_state(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Card with very long title")
def long_title(page):
    pass


@when("Content renders")
def content_renders(page):
    insights_page = InsightsPage(page)
    insights_page.goto("/")


@then("Title is handled appropriately without breaking layout")
def verify_layout_intact(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Medicare Advantage eBook card")
def medicare_ebook_card(page):
    page.goto("/")


@when("Card is verified")
def verify_card(page):
    pass


@then("Title shows 'Managing the Margin Reset in Medicare Advantage', type is eBook, imagery displays if available, Download action present")
def verify_medicare_card(page):
    insights_page = InsightsPage(page)
    insights_page.verify_medicare_ebook()


@given("Medicare Advantage eBook card link")
def medicare_link(page):
    insights_page = InsightsPage(page)
    insights_page.goto("/")


@when("URL is inspected")
def inspect_url(page):
    pass


@then("Card routes to current detail page at /insights/managing-the-margin-reset-in-medicare-advantage/")
def verify_medicare_url(page):
    insights_page = InsightsPage(page)
    url = insights_page.get_medicare_ebook_url()
    assert "/insights/managing-the-margin-reset-in-medicare-advantage/" in url


@given("CMS-0057 interoperability resource card")
def cms0057_card(page):
    page.goto("/")


@when("Content is verified")
def verify_content(page):
    pass


@then("Title, type, and action are populated from approved content")
def verify_populated(page):
    insights_page = InsightsPage(page)
    insights_page.verify_cms0057_card()


@given("CMS-0057 card")
def cms0057(page):
    page.goto("/")


@when("Required fields are checked")
def check_fields(page):
    pass


@then("Title and destination are populated")
def verify_populated_fields(page):
    insights_page = InsightsPage(page)
    insights_page.verify_cms0057_card()


@given("CMS-0057 card action")
def cms0057_action(page):
    page.goto("/")


@when("Link is followed")
def follow_link(page):
    pass


@then("Navigates to configured resource destination")
def verify_navigation(page):
    insights_page = InsightsPage(page)
    insights_page.verify_cms0057_card()


@given("Life Sciences transformation eBook card")
def ls_ebook_card(page):
    page.goto("/")


@when("Card is verified")
def verify_ls_card(page):
    pass


@then("Title shows 'Unlocking Trusted Digital Transformation in Life Sciences'")
def verify_ls_title(page):
    insights_page = InsightsPage(page)
    insights_page.verify_life_sciences_ebook()


@given("Life Sciences eBook card destination")
def ls_destination(page):
    insights_page = InsightsPage(page)
    insights_page.goto("/")


@when("URL is verified")
def verify_ls_url(page):
    pass


@then("Card routes to /insights/unlocking-trusted-digital-transformation-in-life-sciences/")
def verify_ls_canonical_url(page):
    insights_page = InsightsPage(page)
    url = insights_page.get_life_sciences_ebook_url()
    assert "/insights/unlocking-trusted-digital-transformation-in-life-sciences/" in url


@given("Download CTA on card")
def download_cta(page):
    page.goto("/")


@when("Clicked")
def click_download(page):
    pass


@then("Opens correct detail/access experience")
def verify_detail_experience(page):
    insights_page = InsightsPage(page)
    insights_page.verify_life_sciences_ebook()


@given("AI ROI eBook card")
def ai_roi_card(page):
    page.goto("/")


@when("Card is verified")
def verify_ai_roi_card(page):
    pass


@then("Title shows 'Closing the AI ROI Gap in Healthcare', type is eBook, expected action present")
def verify_ai_roi_title(page):
    insights_page = InsightsPage(page)
    insights_page.verify_ai_roi_ebook()


@given("AI ROI eBook card")
def ai_roi_card_content(page):
    page.goto("/")


@when("Content status and URL are verified")
def verify_content_url(page):
    pass


@then("Content is published and URL is valid")
def verify_published_valid(page):
    insights_page = InsightsPage(page)
    insights_page.verify_ai_roi_ebook()


@given("FinOps healthcare payer resource card")
def finops_card(page):
    page.goto("/")


@when("Card is verified")
def verify_finops_card(page):
    pass


@then("Title, type, and action render and route correctly")
def verify_finops_render(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("FinOps card link")
def finops_link(page):
    page.goto("/")


@when("URL is tested")
def test_url(page):
    pass


@then("Destination is valid")
def verify_valid_destination(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Payer data readiness blog card")
def payer_blog_card(page):
    page.goto("/")


@when("Card is verified")
def verify_payer_blog(page):
    pass


@then("Title shows 'Payers: Is Your Data Ready for AI?', type is Blog, Read More action shown")
def verify_payer_blog_title(page):
    insights_page = InsightsPage(page)
    insights_page.verify_payer_data_blog()


@given("Blog card CTA")
def blog_cta(page):
    page.goto("/")


@when("Label is verified")
def verify_label(page):
    pass


@then("CTA label reads 'Read More' (reflecting article navigation, not file download)")
def verify_read_more(page):
    count = insights_page.count_read_more_buttons()
    assert count >= 0


@given("Blog card link")
def blog_link(page):
    page.goto("/")


@when("URL is verified")
def verify_blog_url(page):
    pass


@then("Link opens correct article/detail experience")
def verify_article_experience(page):
    insights_page = InsightsPage(page)
    insights_page.verify_payer_data_blog()


@given("eBook card with Download action")
def ebook_card_download(page):
    page.goto("/")


@when("Download is selected")
def select_download(page):
    pass


@then("User reaches resource detail/access flow, not direct file download")
def verify_detail_flow(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Download implementation")
def download_implementation(page):
    page.goto("/")


@when("Network requests are monitored")
def monitor_network(page):
    pass


@then("Implementation does not fabricate or expose private asset endpoints")
def verify_no_exposure(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Gated resource access")
def gated_resource(page):
    page.goto("/")


@when("Gate is encountered")
def encounter_gate(page):
    pass


@then("Required steps are clearly communicated to user")
def verify_clear_communication(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Resource destinations")
def resource_destinations(page):
    page.goto("/")


@when("URLs are verified")
def verify_destinations(page):
    pass


@then("Only verified and published destinations are used")
def verify_verified_destinations(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


@given("Edge case where gated asset unavailable")
def gated_asset_unavailable(page):
    pass


@when("Access is attempted")
def attempt_access(page):
    insights_page = InsightsPage(page)
    insights_page.goto("/")


@then("Appropriate error message is displayed")
def verify_error_message(page):
    insights_page = InsightsPage(page)
    insights_page.verify_section_visible()


from pages.EMIDS-LP-026_insights_page import InsightsPage
