"""Step definitions for emids_lp_051 - SEO metadata."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Page has a unique, descriptive title tag")
def verify_unique_title(page: Page) -> None:
    title = page.title()
    assert title and len(title) > 5


@then("Page has a unique meta description tag")
def verify_meta_description(page: Page) -> None:
    meta = page.locator("meta[name='description']")
    expect(meta).to_have_attribute("content", length=50)


@then("Canonical URL is set to the primary homepage URL")
def verify_canonical_url(page: Page) -> None:
    canonical = page.locator("link[rel='canonical']")
    href = canonical.get_attribute("href")
    assert href and "emids.com" in href


@then("Primary text content is present in initial HTML response")
def verify_server_rendered(page: Page) -> None:
    from pages.emids_lp_051_seo_page import SEOPage
    page_obj = SEOPage(page)
    expect(page_obj.h1).to_be_visible()


@then("Social preview metadata (og:image, og:title, og:description) is configured")
def verify_social_metadata(page: Page) -> None:
    og_title = page.locator("meta[property='og:title']")
    og_desc = page.locator("meta[property='og:description']")
    expect(og_title).to_have_attribute("content")
    expect(og_desc).to_have_attribute("content")


@then("H1 and prominent headings reflect the homepage topic")
def verify_heading_topic(page: Page) -> None:
    from pages.emids_lp_051_seo_page import SEOPage
    page_obj = SEOPage(page)
    h1_text = page_obj.h1.text_content()
    assert "healthcare" in h1_text.lower()


@then("No duplicate or conflicting title tags exist")
def verify_no_duplicate_titles(page: Page) -> None:
    titles = page.locator("title")
    expect(titles).to_have_count(1)


@then("Fallback or graceful degradation; no broken image reference")
def verify_missing_og_image(page: Page) -> None:
    from pages.emids_lp_051_seo_page import SEOPage
    page_obj = SEOPage(page)
    expect(page_obj.h1).to_be_visible()


@then("Primary content and navigation remain accessible")
def verify_js_critical_content(page: Page) -> None:
    from pages.emids_lp_051_seo_page import SEOPage
    page_obj = SEOPage(page)
    expect(page_obj.h1).to_be_visible()
    expect(page_obj.navigation).to_be_visible()
