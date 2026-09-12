"""Step definitions for SEO requirements."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("page has unique title and meta description")
def unique_title_meta_description(page: Page) -> None:
    """Verify page has unique title and meta description."""
    title = page.title()
    assert title is not None and title.strip() != ""
    assert len(title) > 10
    
    meta_desc = page.locator('meta[name="description"]').get_attribute("content")
    assert meta_desc is not None and meta_desc.strip() != ""


@then("canonical URL set on homepage")
def canonical_url_set(page: Page) -> None:
    """Verify canonical URL set on homepage."""
    canonical = page.locator('link[rel="canonical"]').get_attribute("href")
    assert canonical is not None
    assert "emids.com" in canonical


@then("Open Graph Twitter social preview metadata configured")
def social_preview_metadata(page: Page) -> None:
    """Verify Open Graph Twitter social preview metadata configured."""
    og_title = page.locator('meta[property="og:title"]').get_attribute("content")
    og_description = page.locator('meta[property="og:description"]').get_attribute("content")
    og_image = page.locator('meta[property="og:image"]').get_attribute("content")
    
    assert og_title is not None or og_description is not None or og_image is not None
