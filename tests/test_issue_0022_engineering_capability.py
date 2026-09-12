"""Test for issue_0022 - Engineering capability content rendering."""
import pytest

from pages.issue_0022_engineering_capability_page import Issue0022EngineeringCapabilityPage


@pytest.fixture
def engineering_capability_page(page) -> Issue0022EngineeringCapabilityPage:
    """Create page object for issue_0022 tests."""
    return Issue0022EngineeringCapabilityPage(page)
