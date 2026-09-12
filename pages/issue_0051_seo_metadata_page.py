"""Page object for issue_0051 - SEO metadata and crawlable structure."""
from playwright.sync_api import Page, expect


class Issue0051SEOMetadataPage:
    """Page object for SEO metadata."""

    def __init__(self, page: Page):
        self.page = page

    def view_page_source(self) -> None:
        """View the page source."""
        pass

    def page_should_have_title_tag(self) -> None:
        """Verify page has a title tag."""
        title = self.page.locator("title")
        expect(title).to_be_attached()
        title_text = title.inner_text()
        assert len(title_text) > 0, "Page title should not be empty"

    def page_should_have_meta_description(self) -> None:
        """Verify page has meta description."""
        meta_desc = self.page.locator("meta[name='description']")
        expect(meta_desc).to_be_attached()
        content = await meta_desc.get_attribute("content")
        assert content is not None and len(content) > 0, "Meta description should not be empty"

    def page_should_have_canonical_url(self) -> None:
        """Verify page has canonical URL."""
        canonical = self.page.locator("link[rel='canonical']")
        expect(canonical).to_be_attached()
        href = await canonical.get_attribute("href")
        assert href is not None and len(href) > 0, "Canonical URL should not be empty"
