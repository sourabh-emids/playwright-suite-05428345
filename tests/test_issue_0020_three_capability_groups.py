"""Test for issue_0020 - Three capability groups visibility and content."""
import pytest

from pages.issue_0020_three_capability_groups_page import Issue0020ThreeCapabilityGroupsPage


@pytest.fixture
def three_capability_groups_page(page) -> Issue0020ThreeCapabilityGroupsPage:
    """Create page object for issue_0020 tests."""
    return Issue0020ThreeCapabilityGroupsPage(page)
