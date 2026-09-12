"""Test for issue_0012 - How We Deliver section content rendering."""
import pytest

from pages.issue_0012_how_we_deliver_page import Issue0012HowWeDeliverPage


@pytest.fixture
def how_we_deliver_page(page) -> Issue0012HowWeDeliverPage:
    """Create page object for issue_0012 tests."""
    return Issue0012HowWeDeliverPage(page)
