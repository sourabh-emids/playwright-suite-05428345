"""Test for issue_0055 - Homepage modal behavior default state."""
import pytest

from pages.issue_0055_homepage_modal_behavior_page import Issue0055HomepageModalBehaviorPage


@pytest.fixture
def homepage_modal_behavior_page(page) -> Issue0055HomepageModalBehaviorPage:
    """Create page object for issue_0055 tests."""
    return Issue0055HomepageModalBehaviorPage(page)
