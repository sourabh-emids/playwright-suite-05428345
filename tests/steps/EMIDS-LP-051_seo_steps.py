"""Step definitions for SEO metadata - EMIDS-LP-051"""
from pytest_bdd import given, when, then
from playwright.sync_api import expect


@given("Homepage document head")
def homepage_head(page):
    page.goto("/")


@when("Title tag is verified")
def verify_title_tag(page):
    pass


@then("Page has unique title")
def verify_unique_title(page):
    title = page.title()
    assert title and len(title) > 0


@given("Homepage metadata")
def homepage_metadata(page):
    page.goto("/")


@when("Meta description is verified")
def verify_meta_description(page):
    pass


@then("Meta description is present and descriptive")
def verify_present_description(page):
    meta_desc = page.locator('meta[name="description"]').get_attribute("content")
    assert meta_desc and len(meta_desc) > 0


@given("Homepage canonical link")
def homepage_canonical(page):
    page.goto("/")


@when("Canonical is verified")
def verify_canonical(page):
    pass


@then("Canonical URL points to primary homepage URL")
def verify_primary_url(page):
    canonical = page.locator('link[rel="canonical"]').get_attribute("href")
    assert canonical and "emids.com" in canonical


@given("Critical page content")
def critical_content(page):
    page.goto("/")


@when("Page source is analyzed")
def analyze_source(page):
    pass


@then("Primary text is server-rendered and crawlable")
def verify_server_rendered(page):
    content = page.locator("h1").first.text_content()
    assert content and len(content) > 0


@given("Open Graph and Twitter metadata")
def og_twitter_metadata(page):
    page.goto("/")


@when("Social sharing is tested")
def test_social_sharing(page):
    pass


@then("Social preview metadata is configured")
def verify_social_configured(page):
    og_title = page.locator('meta[property="og:title"]').get_attribute("content")
    assert og_title is not None


@given("Page heading structure")
def page_heading_structure(page):
    page.goto("/")


@when("Headings are reviewed")
def review_headings(page):
    pass


@then("Headings reflect the page topic for search engines")
def verify_topic(page):
    h1 = page.locator("h1").first.text_content()
    assert h1 and "healthcare" in h1.lower()


@given("Page title tags")
def page_title_tags(page):
    page.goto("/")


@when("Title tags are audited")
def audit_title(page):
    pass


@then("No duplicate or conflicting title tags exist")
def verify_no_conflicts(page):
    title_count = page.evaluate('document.querySelectorAll("title").length')
    assert title_count == 1
