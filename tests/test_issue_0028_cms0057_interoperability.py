"""Test for issue_0028 - CMS-0057 interoperability resource card display."""
import pytest

from pages.issue_0028_cms0057_interoperability_page import Issue0028CMS0057InteroperabilityPage


@pytest.fixture
def cms0057_interoperability_page(page) -> Issue0028CMS0057InteroperabilityPage:
    """Create page object for issue_0028 tests."""
    return Issue0028CMS0057InteroperabilityPage(page)
