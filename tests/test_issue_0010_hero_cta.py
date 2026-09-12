"""Test for issue_0010 - Hero CTA routing to FDCE experience."""
import pytest

from pages.issue_0010_hero_cta_page import Issue0010HeroCTAPage


@pytest.fixture
def hero_cta_page(page) -> Issue0010HeroCTAPage:
    """Create page object for issue_0010 tests."""
    return Issue0010HeroCTAPage(page)
