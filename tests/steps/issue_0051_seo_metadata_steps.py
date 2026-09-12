"""Step definitions for issue_0051 - SEO metadata and crawlable structure."""
from pytest_bdd import given, then, when

from pages.issue_0051_seo_metadata_page import Issue0051SEOMetadataPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0051SEOMetadataPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the page source")
def view_page_source(page: Issue0051SEOMetadataPage):
    """View the page source."""
    page.view_page_source()


@then("the page should have a title tag")
def title_tag(page: Issue0051SEOMetadataPage):
    """Verify page has a title tag."""
    page.page_should_have_title_tag()


@then("the page should have meta description")
def meta_description(page: Issue0051SEOMetadataPage):
    """Verify page has meta description."""
    page.page_should_have_meta_description()


@then("the page should have canonical URL")
def canonical_url(page: Issue0051SEOMetadataPage):
    """Verify page has canonical URL."""
    page.page_should_have_canonical_url()
