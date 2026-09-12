"""Test for issue_0019 - Reduced motion preference for partner animation."""
import pytest

from pages.issue_0019_reduced_motion_page import Issue0019ReducedMotionPage


@pytest.fixture
def reduced_motion_page(page) -> Issue0019ReducedMotionPage:
    """Create page object for issue_0019 tests."""
    return Issue0019ReducedMotionPage(page)
