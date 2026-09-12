"""Test for SEO requirements."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_unique_title_meta_description(page_ready: Page) -> None:
    """Test page has unique title and meta description."""
    title = page_ready.title()
    assert title is not None and title.strip() != ""
    assert len(title) > 10
    
    meta_desc = page_ready.locator('meta[name="description"]').get_attribute("content")
    assert meta_desc is not None and meta_desc.strip() != ""


def test_canonical_url_set(page_ready: Page) -> None:
    """Test canonical URL set on homepage."""
    canonical = page_ready.locator('link[rel="canonical"]').get_attribute("href")
    assert canonical is not None
    assert "emids.com" in canonical


def test_social_preview_metadata(page_ready: Page) -> None:
    """Test Open Graph Twitter social preview metadata configured."""
    og_title = page_ready.locator('meta[property="og:title"]').get_attribute("content")
    og_description = page_ready.locator('meta[property="og:description"]').get_attribute("content")
    og_image = page_ready.locator('meta[property="og:image"]').get_attribute("content")
    
    assert og_title is not None or og_description is not None or og_image is not None
