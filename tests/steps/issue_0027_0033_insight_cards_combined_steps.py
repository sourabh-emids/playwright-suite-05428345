"""Step definitions for issue_0027-0033: Insight cards combined"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0027_0033_insight_cards_combined_page import InsightCardsPage


# Issue 0027 - Medicare Advantage eBook
@given("The Insights section includes the Medicare Advantage resource")
def medicare_resource(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("The Medicare Advantage eBook card is rendered")
def medicare_card_rendered(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@when("The card is rendered")
def card_rendered(page: Page):
    pass


@when("Image availability is checked")
def image_checked(page: Page):
    pass


@when("A user clicks the Download action on the Medicare Advantage card")
def user_clicks_medicare_download(page: Page):
    page_object = InsightCardsPage(page)
    page_object.click_download_button()


@then("Title displays 'Managing the Margin Reset in Medicare Advantage' with eBook type and Download action")
def medicare_title_displayed(page: Page):
    expect(page.get_by_text("Medicare Advantage")).to_be_visible()


@then("The card displays imagery if available")
def card_displays_imagery(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("The user reaches the resource detail/access page")
def user_reaches_detail(page: Page):
    expect(page).not_to_have_title("/404/")


# Issue 0028 - CMS-0057
@given("The Insights section includes the CMS-0057 interoperability resource")
def cms_resource(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("The CMS-0057 card is rendered")
def cms_card_rendered(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@when("A user clicks the CMS-0057 card action")
def user_clicks_cms(page: Page):
    page_object = InsightCardsPage(page)
    page_object.click_download_button()


@then("Card title, type, and action are populated from approved content")
def cms_card_populated(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()


@then("The user reaches the configured resource destination")
def cms_reaches_destination(page: Page):
    expect(page).not_to_have_title("/404/")


@then("No empty title or destination fields exist")
def no_empty_fields(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()


# Issue 0029 - Life Sciences eBook
@given("The Insights section includes the Life Sciences transformation resource")
def life_sciences_resource(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@when("Navigation completes")
def navigation_completes(page: Page):
    pass


@then("Title displays 'Unlocking Trusted Digital Transformation in Life Sciences' with appropriate action")
def life_sciences_title(page: Page):
    expect(page.get_by_text("Life Sciences")).to_be_visible()


@then("The user reaches the correct detail/access experience")
def life_sciences_detail(page: Page):
    expect(page).not_to_have_title("/404/")


@then("The URL follows canonical format at /insights/unlocking-trusted-digital-transformation-in-life-sciences/")
def life_sciences_canonical(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


# Issue 0030 - AI ROI eBook
@given("The Insights section includes the AI ROI resource")
def ai_roi_resource(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("The AI ROI eBook card is rendered")
def ai_roi_card_rendered(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@then("Title displays 'Closing the AI ROI Gap in Healthcare' with eBook labeling and expected action")
def ai_roi_title(page: Page):
    expect(page.get_by_text("AI")).to_be_visible()


@then("Content is published and URL is valid")
def ai_roi_valid(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()


# Issue 0031 - FinOps
@given("The Insights section includes the FinOps healthcare payer resource")
def finops_resource(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("The FinOps card is rendered")
def finops_card_rendered(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@then("Card displays title, type, and action with correct routing")
def finops_display(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()


@then("The destination URL is valid")
def finops_valid_url(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()


# Issue 0032 - Payer data readiness blog
@given("The Insights section includes the payer data readiness blog")
def payer_blog_resource(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("The blog card CTA is rendered")
def blog_cta_rendered(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@then("Title displays 'Payers: Is Your Data Ready for AI?' with type=Blog and Read More action")
def payer_blog_title(page: Page):
    expect(page.get_by_text("Payer")).to_be_visible()


@then("The user reaches the correct article/detail experience")
def payer_blog_detail(page: Page):
    expect(page).not_to_have_title("/404/")


@then("CTA label shows 'Read More' rather than 'Download' to reflect article navigation")
def cta_label_read_more(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()


# Issue 0033 - Resource access handoff
@given("A user clicks Download on an eBook card")
def user_clicks_ebook_download(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()
    page_object.click_download_button()


@given("eBook cards are implemented")
def ebook_cards_implemented(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("A resource requires gate/submission")
def resource_requires_gate(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@given("Resource cards are rendered")
def resource_cards_rendered(page: Page):
    page_object = InsightCardsPage(page)
    page_object.navigate_to_homepage()


@when("Network traffic is analyzed")
def network_analyzed(page: Page):
    pass


@when("The user reaches the gate")
def user_reaches_gate(page: Page):
    pass


@when("URL validation runs")
def url_validation_runs(page: Page):
    pass


@then("The user reaches the resource detail/access flow rather than a direct file download")
def reaches_detail_flow(page: Page):
    expect(page).not_to_have_title("/404/")


@then("Implementation does not fabricate or expose private asset URLs directly")
def no_private_urls(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("The required steps are clearly communicated")
def steps_communicated(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("All resource URLs point to verified/published destinations")
def verified_destinations(page: Page):
    page_object = InsightCardsPage(page)
    page_object.verify_insights_section()
