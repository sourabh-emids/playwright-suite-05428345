"""Test for issue_0009 - Hero section rendering and H1 uniqueness."""
import pytest

from pages.issue_0009_hero_page import Issue0009HeroPage


@pytest.fixture
def hero_page(page) -> Issue0009HeroPage:
    """Create page object for issue_0009 tests."""
    return Issue0009HeroPage(page)
