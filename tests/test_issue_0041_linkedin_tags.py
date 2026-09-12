"""Test for issue_0041 - LinkedIn marketing tags conditional loading."""
import pytest

from pages.issue_0041_linkedin_tags_page import Issue0041LinkedInTagsPage


@pytest.fixture
def linkedin_tags_page(page) -> Issue0041LinkedInTagsPage:
    """Create page object for issue_0041 tests."""
    return Issue0041LinkedInTagsPage(page)
