"""Test for issue_0023 - Platforms capability taxonomy consistency."""
import pytest

from pages.issue_0023_platforms_capability_page import Issue0023PlatformsCapabilityPage


@pytest.fixture
def platforms_capability_page(page) -> Issue0023PlatformsCapabilityPage:
    """Create page object for issue_0023 tests."""
    return Issue0023PlatformsCapabilityPage(page)
