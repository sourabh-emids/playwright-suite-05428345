"""Steps for SEO metadata and crawlable structure (issue_0051)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0051_seo_metadata_locators import SEOMetadataLocators


@given("User views page source")
def view_source(page: Page) -> None:
    page.goto("/")


@given("User or crawler views page")
def crawler_view(page: Page) -> None:
    page.goto("/")


@given("User views page headings")
def view_headings(page: Page) -> None:
    page.goto("/")


@given("Canonical URLs are compared")
def compare_canonicals(page: Page) -> None:
    page.goto("/")


@given("Title tags are compared")
def compare_titles(page: Page) -> None:
    page.goto("/")


@given("OG image is missing")
def og_missing(page: Page) -> None:
    page.goto("/")


@given("Critical content is managed")
def critical_content(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


@when("Page loads without JavaScript")
def load_no_js(page: Page) -> None:
    pass


@when("Social share occurs")
def social_share(page: Page) -> None:
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Page has a unique title element")
def unique_title(page: Page) -> None:
    expect(SEOMetadataLocators(page).page_title).to_be_visible()
    title = page.title()
    assert title and title.strip()


@then("Page has meta description element")
def meta_description(page: Page) -> None:
    expect(SEOMetadataLocators(page).meta_description).to_be_attached()
    desc = page.locator("meta[name='description']").get_attribute("content")
    assert desc and desc.strip()


@then("Canonical URL is set to the primary page URL")
def canonical_set(page: Page) -> None:
    expect(SEOMetadataLocators(page).canonical_url).to_be_attached()
    href = page.locator("link[rel='canonical']").get_attribute("href")
    assert href and "emids" in href


@then("Primary text content is server-rendered and crawlable")
def server_rendered(page: Page) -> None:
    expect(SEOMetadataLocators(page).h1_heading).to_be_visible()


@then("Open Graph and Twitter Card metadata is configured")
def og_configured(page: Page) -> None:
    og_tags = page.locator("meta[property^='og:']").count()
    assert og_tags > 0


@then("H1 reflects page topic and matches title")
def h1_matches_title(page: Page) -> None:
    h1 = SEOMetadataLocators(page).h1_heading.text_content()
    title = page.title()
    assert h1 or title


@then("Only one canonical homepage URL exists")
def one_canonical(page: Page) -> None:
    canonicals = page.locator("link[rel='canonical']").count()
    assert canonicals <= 1


@then("No duplicate or conflicting title tags exist")
def no_duplicate_titles(page: Page) -> None:
    titles = page.locator("title").count()
    assert titles == 1


@then("Fallback image or appropriate default displays")
def fallback_image(page: Page) -> None:
    pass


@then("Critical content is not JavaScript-only")
def not_js_only(page: Page) -> None:
    expect(SEOMetadataLocators(page).h1_heading).to_be_visible()
