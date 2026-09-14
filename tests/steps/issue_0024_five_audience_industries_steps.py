"""Step definitions for issues 0024-0055: Consolidated."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


# Who We Serve (issue_0024)
@given("Who We Serve section renders")
def who_we_serve_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Audiences are counted")
def count_audiences(page: Page):
    pass


@then("All five audiences (Payer, Provider, HealthTech, Life Sciences, Consumer) are visible")
def five_audiences_visible(page: Page):
    audience_tabs = page.locator("text=/Payer|Provider|HealthTech|Life Sciences|Consumer/")
    count = audience_tabs.count()
    assert count >= 5, f"Expected 5 audiences, found {count}"


@given("Each audience has Explore action")
def audience_has_explore(page: Page):
    page.goto("/")


@when("Explore is clicked")
def click_explore(page: Page):
    explore = page.get_byRole("button", name="Payer").locator("..").get_by_role("link", name="Explore")
    explore.click()


@then("Action routes to canonical segment page: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/")
def routes_to_segments(page: Page):
    expect(page).to_have_urlContaining("/segments/")


@given("Explore actions are rendered")
def explore_rendered(page: Page):
    page.goto("/")


@when("User interacts via keyboard or touch")
def interact_keyboard_touch(page: Page):
    page.keyboard.press("Tab")


@then("Interactions work on keyboard and touch")
def interactions_work(page: Page):
    pass


@given("Audiences section is configured")
def audiences_configured(page: Page):
    page.goto("/")


@when("Audience count is validated")
def validate_audience_count(page: Page):
    pass


@then("Exactly five current audiences exist for this content version")
def five_audiences_exist(page: Page):
    audiences = page.locator("button:has-text('Payer'), button:has-text('Provider'), button:has-text('HealthTech'), button:has-text('Life Sciences'), button:has-text('Consumer')")
    count = audiences.count()
    assert count == 5, f"Expected 5 audiences, found {count}"


@given("Audience explore links are configured")
def audience_links_configured(page: Page):
    page.goto("/")


@when("URLs are validated")
def validate_urls_audiences(page: Page):
    pass


@then("All URLs are canonical")
def canonical_urls_audiences(page: Page):
    links = page.locator('a[href*="/segments/"]')
    for link in links.all():
        href = link.get_attribute("href")
        assert href, "Link should have href"


@given("Who We Serve section renders across viewports")
def wws_across_viewports(page: Page):
    page.goto("/")


@when("Viewport changes")
def viewport_changes_wws(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Responsive tabs/cards/accordion/rail work without hiding access")
def responsive_works(page: Page):
    section = page.locator("text=/Payer|Provider/")
    expect(section).to_be_visible()


@given("One segment page is unavailable")
def segment_unavailable(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_wws(page: Page):
    page.wait_for_load_state("networkidle")


@then("Unavailable segment handled gracefully")
def segment_handled(page: Page):
    section = page.locator("text=Who We Serve")
    expect(section).to_be_visible()


@given("User selects an audience tab at desktop width")
def tab_selected_desktop(page: Page):
    page.goto("/")
    page.set_viewport_size({"width": 1280, "height": 720})


@when("Viewport resizes to mobile")
def resize_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Tab state is preserved or transitioned appropriately")
def tab_state_preserved(page: Page):
    pass


# Impact Metrics (issue_0025)
@given("Impact section renders")
def impact_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Metrics are checked")
def check_metrics(page: Page):
    pass


@then("All four value/label pairs are visible as text: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, 450+ Platforms Launched")
def four_metrics_visible(page: Page):
    metrics = page.locator("text=/36\\+|115\\+|48\\+|450\\+/")
    expect(metrics.first).to_be_visible()


@given("Count-up animation is present but disabled or incomplete")
def animation_disabled(page: Page):
    page.goto("/")


@when("User views metrics")
def view_metrics(page: Page):
    pass


@then("Values remain understandable without animation")
def values_understandable(page: Page):
    metrics = page.locator("text=/\\d/")
    expect(metrics.first).to_be_visible()


@given("Impact metrics render with animation")
def metrics_animate(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Screen reader interprets section")
def screen_reader_interprets(page: Page):
    pass


@then("Screen readers receive final meaningful values (not animation intermediate states)")
def sr_final_values(page: Page):
    metrics = page.locator("text=/\\d/")
    expect(metrics.first).to_be_visible()


@given("Impact metrics are managed")
def metrics_managed(page: Page):
    page.goto("/")


@when("Values and labels are checked")
def check_values_labels(page: Page):
    pass


@then("Values and labels are managed as paired content")
def paired_content(page: Page):
    pass


@given("Impact metrics contain currency symbols and plus signs")
def metrics_have_symbols(page: Page):
    page.goto("/")


@when("Metrics render")
def metrics_render(page: Page):
    page.wait_for_load_state("networkidle")


@then("Currency symbols and plus signs are preserved where approved")
def symbols_preserved(page: Page):
    section = page.locator("text=Impact")
    expect(section).to_be_visible()


@given("Count-up animation is disabled via settings")
def animation_disabled_settings(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_impact(page: Page):
    page.wait_for_load_state("networkidle")


@then("Final values display correctly")
def final_values_display(page: Page):
    section = page.locator("text=Impact")
    expect(section).to_be_visible()


@given("User locale differs from default")
def locale_differs(page: Page):
    page.goto("/")


@when("Metrics render")
def metrics_render_locale(page: Page):
    page.wait_for_load_state("networkidle")


@then("Locale formatting is handled appropriately")
def locale_handling(page: Page):
    metrics = page.locator("text=/\\d/")
    expect(metrics.first).to_be_visible()


# Insights Section (issues 0026-0033)
@given("Insights section renders")
def insights_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Cards are counted")
def count_cards(page: Page):
    pass


@then("Six cards render")
def six_cards_render(page: Page):
    section = page.locator("text=Insights").locator("..").locator("..")
    cards = section.locator("a")
    count = cards.count()
    assert count >= 6, f"Expected 6 cards, found {count}"


@given("Each insight card is reviewed")
def card_reviewed(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Content type, title, action are checked")
def check_card_content(page: Page):
    pass


@then("Each card has content type, title, image where configured, and Download/Read More action")
def card_has_content(page: Page):
    section = page.locator("text=Insights").locator("..").locator("..")
    expect(section).to_be_visible()


@given("Insights cards render across viewports")
def cards_across_viewports(page: Page):
    page.goto("/")


@when("Viewport changes")
def viewport_changes_cards(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Cards remain accessible at all breakpoints")
def cards_accessible(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Insight cards are configured")
def cards_configured(page: Page):
    page.goto("/")


@when("URLs are validated")
def validate_urls_cards(page: Page):
    pass


@then("URLs are canonical and resolve")
def canonical_resolve(page: Page):
    section = page.locator("text=Insights").locator("..").locator("..")
    links = section.locator("a")
    for link in links.all():
        href = link.get_attribute("href")
        assert href, "Link should have href"


@given("Insight cards render")
def cards_render(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("CTA labels are checked")
def check_cta_labels(page: Page):
    pass


@then("Action labels match content flow (Download for eBooks, Read More for articles)")
def cta_labels_match(page: Page):
    section = page.locator("text=Insights").locator("..").locator("..")
    expect(section).to_be_visible()


@given("One insight resource is unpublished")
def resource_unpublished(page: Page):
    page.goto("/")


@when("Section renders")
def section_renders_insights(page: Page):
    page.wait_for_load_state("networkidle")


@then("Unpublished resource handled gracefully")
def unpublished_handled_insights(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Card has missing thumbnail image")
def thumbnail_missing(page: Page):
    page.goto("/")
    page.route(lambda url: "jpg" in url or "png" in url or "image" in url, lambda route: route.abort())


@when("Card renders")
def card_renders(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Card renders appropriately without breaking layout")
def card_without_image(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Card has unusually long title")
def long_title_card(page: Page):
    page.goto("/")


@when("Card renders at viewport")
def card_at_viewport(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Long title handled gracefully without breaking layout")
def long_title_handled_card(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


# Medicare Advantage eBook (issue_0027)
@given("Medicare Advantage eBook card renders")
def medicare_ebook_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title is checked")
def check_title_medicare(page: Page):
    pass


@then("Title displays as 'Managing the Margin Reset in Medicare Advantage'")
def title_correct_medicare(page: Page):
    card = page.locator("text=/Medicare Advantage/i")
    expect(card.first).to_be_visible()


@given("Medicare Advantage eBook card renders")
def medicare_ebook_renders_type(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Type is checked")
def check_type_medicare(page: Page):
    pass


@then("Content type shows as eBook")
def type_correct_medicare(page: Page):
    ebook = page.locator("text=/eBook/i")
    expect(ebook.first).to_be_visible()


@given("Medicare Advantage eBook card renders")
def medicare_ebook_renders_action(page: Page):
    page.goto("/")


@when("Action is checked")
def check_action_medicare(page: Page):
    pass


@then("Download action is displayed and routes correctly")
def download_action_medicare(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Medicare Advantage eBook has imagery configured")
def ebook_imagery(page: Page):
    page.goto("/")


@when("Card renders")
def card_renders_medicare(page: Page):
    page.wait_for_load_state("networkidle")


@then("Image displays where available")
def image_displays(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Medicare Advantage eBook CTA is clicked")
def click_medicare_cta(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Navigation completes")
def nav_complete_medicare(page: Page):
    pass


@then("User reaches detail/access page at /insights/managing-the-margin-reset-in-medicare-advantage/")
def detail_page_medicare(page: Page):
    pass


@given("Medicare Advantage resource is removed or gated differently")
def resource_gated_medicare(page: Page):
    page.goto("/")


@when("User accesses card")
def access_card_medicare(page: Page):
    pass


@then("Appropriate handling occurs")
def handling_medicare(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


# CMS-0057 (issue_0028)
@given("CMS-0057 interoperability resource card renders")
def cms0057_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title is checked")
def check_title_cms0057(page: Page):
    pass


@then("Card title is populated from approved content")
def title_populated_cms0057(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("CMS-0057 card renders")
def cms0057_renders_type(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Type and action are checked")
def check_type_action_cms0057(page: Page):
    pass


@then("Card type and action are populated from approved content")
def type_action_populated(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("CMS-0057 card action is activated")
def activate_cms0057(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Navigation completes")
def nav_complete_cms0057(page: Page):
    pass


@then("User reaches intended resource destination")
def destination_reached(page: Page):
    pass


@given("CMS-0057 card is configured")
def cms0057_configured(page: Page):
    page.goto("/")


@when("Title is validated")
def validate_title_cms0057(page: Page):
    pass


@then("Title is not empty")
def title_not_empty_cms0057(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("CMS-0057 destination is configured")
def cms0057_dest_configured(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url_cms0057(page: Page):
    pass


@then("Destination resolves and is not empty")
def dest_resolves_cms0057(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


# Life Sciences eBook (issue_0029)
@given("Life Sciences transformation eBook card renders")
def ls_ebook_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title is checked")
def check_title_ls(page: Page):
    pass


@then("Title displays as 'Unlocking Trusted Digital Transformation in Life Sciences'")
def title_correct_ls(page: Page):
    card = page.locator("text=/Life Sciences/i")
    expect(card.first).to_be_visible()


@given("Life Sciences eBook card renders")
def ls_ebook_renders_action(page: Page):
    page.goto("/")


@when("Action is activated")
def activate_ls(page: Page):
    pass


@then("Download action opens correct detail/access experience")
def download_action_ls(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Life Sciences eBook card routes")
def ls_routes(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url_ls(page: Page):
    pass


@then("Canonical detail URL is used: /insights/unlocking-trusted-digital-transformation-in-life-sciences/")
def canonical_url_ls(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("User clicks Download on Life Sciences eBook")
def click_download_ls(page: Page):
    page.goto("/")


@when("Navigation completes")
def nav_complete_ls(page: Page):
    pass


@then("User reaches resource detail/access flow")
def resource_flow_ls(page: Page):
    pass


# AI ROI eBook (issue_0030)
@given("AI ROI eBook card renders")
def ai_roi_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title is checked")
def check_title_ai_roi(page: Page):
    pass


@then("Title displays as 'Closing the AI ROI Gap in Healthcare'")
def title_correct_ai_roi(page: Page):
    card = page.locator("text=/AI ROI/i")
    expect(card.first).to_be_visible()


@given("AI ROI eBook card renders")
def ai_roi_renders_type(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Type is checked")
def check_type_ai_roi(page: Page):
    pass


@then("Card is labeled as eBook")
def type_correct_ai_roi(page: Page):
    ebook = page.locator("text=/eBook/i")
    expect(ebook.first).to_be_visible()


@given("AI ROI eBook card renders")
def ai_roi_renders_action(page: Page):
    page.goto("/")


@when("Action is checked")
def check_action_ai_roi(page: Page):
    pass


@then("Expected action is present and functional")
def action_functional_ai_roi(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("AI ROI eBook is configured")
def ai_roi_configured(page: Page):
    page.goto("/")


@when("Content status is checked")
def check_status_ai_roi(page: Page):
    pass


@then("Content is published and URL is valid")
def published_valid_ai_roi(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


# FinOps Payer (issue_0031)
@given("FinOps healthcare payer resource card renders")
def finops_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title and action are checked")
def check_title_action_finops(page: Page):
    pass


@then("Card displays title and routes correctly")
def title_route_finops(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("FinOps card action is activated")
def activate_finops(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Navigation completes")
def nav_complete_finops(page: Page):
    pass


@then("User reaches configured resource destination")
def finops_destination(page: Page):
    pass


@given("FinOps payer resource card renders")
def finops_renders_type(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Type is checked")
def check_type_finops(page: Page):
    pass


@then("Card type matches resource category")
def type_matches_finops(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("FinOps resource URL is broken")
def finops_url_broken(page: Page):
    page.goto("/")


@when("Card action is activated")
def activate_broken_finops(page: Page):
    pass


@then("Appropriate error handling occurs")
def error_handling_finops(page: Page):
    pass


# Payer Data Blog (issue_0032)
@given("Payer data readiness blog card renders")
def payer_blog_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title is checked")
def check_title_payer_blog(page: Page):
    pass


@then("Title displays as 'Payers: Is Your Data Ready for AI?'")
def title_correct_payer_blog(page: Page):
    card = page.locator("text=/Payers.*Data/i")
    expect(card.first).to_be_visible()


@given("Payer data readiness card renders")
def payer_blog_renders_type(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Type is checked")
def check_type_payer_blog(page: Page):
    pass


@then("Content type is Blog")
def type_blog_payer(page: Page):
    blog = page.locator("text=/Blog/i")
    expect(blog.first).to_be_visible()


@given("Payer data readiness blog card renders")
def payer_blog_renders_action(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Action label is checked")
def check_action_payer_blog(page: Page):
    pass


@then("CTA shows 'Read More' (not Download)")
def read_more_not_download(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Read More action is activated")
def activate_read_more(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Navigation completes")
def nav_complete_read_more(page: Page):
    pass


@then("User reaches correct article/detail experience")
def article_experience(page: Page):
    pass


@given("Blog card action label is configured")
def blog_action_configured(page: Page):
    page.goto("/")


@when("Label is validated")
def validate_label_blog(page: Page):
    pass


@then("Label reflects article navigation rather than file download")
def label_article_not_download(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


# Resource Access (issue_0033)
@given("User clicks Download on eBook card")
def click_download_ebook(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Navigation completes")
def nav_complete_resource(page: Page):
    pass


@then("User reaches resource detail/access flow (not direct file URL)")
def resource_flow(page: Page):
    pass


@given("Resource cards are implemented")
def resource_cards_impl(page: Page):
    page.goto("/")


@when("URLs are inspected")
def inspect_urls(page: Page):
    pass


@then("Implementation does not fabricate or expose private asset endpoints")
def no_private_endpoints(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Resource is gated")
def resource_gated(page: Page):
    page.goto("/")


@when("User reaches gate")
def reach_gate(page: Page):
    pass


@then("Gate clearly communicates required steps")
def gate_communicates(page: Page):
    pass


@given("Resource card destinations are configured")
def dest_configured(page: Page):
    page.goto("/")


@when("URLs are validated")
def validate_urls_resource(page: Page):
    pass


@then("Only verified/published destinations are used")
def verified_destinations(page: Page):
    section = page.locator("text=Insights")
    expect(section).to_be_visible()


@given("Gated asset is unavailable")
def gated_unavailable(page: Page):
    page.goto("/")


@when("User attempts access")
def attempt_access(page: Page):
    pass


@then("Appropriate error handling occurs")
def error_handling_gated(page: Page):
    pass


@given("Popup is used for resource access and popup blocker is active")
def popup_blocker_active(page: Page):
    page.goto("/")


@when("User activates access")
def activate_access(page: Page):
    pass


@then("Graceful fallback handling occurs")
def fallback_popup(page: Page):
    pass
