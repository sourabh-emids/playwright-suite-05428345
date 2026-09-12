"""Test for issue_0033 - Resource access handoff for eBook cards."""
import pytest

from pages.issue_0033_resource_access_handoff_page import Issue0033ResourceAccessHandoffPage


@pytest.fixture
def resource_access_handoff_page(page) -> Issue0033ResourceAccessHandoffPage:
    """Create page object for issue_0033 tests."""
    return Issue0033ResourceAccessHandoffPage(page)
