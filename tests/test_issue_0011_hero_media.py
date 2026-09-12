"""Test for issue_0011 - Hero media optimization and load behavior."""
import pytest

from pages.issue_0011_hero_media_page import Issue0011HeroMediaPage


@pytest.fixture
def hero_media_page(page) -> Issue0011HeroMediaPage:
    """Create page object for issue_0011 tests."""
    return Issue0011HeroMediaPage(page)
