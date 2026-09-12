"""Test for issue_0035 - Delivery timing message rendering."""
import pytest

from pages.issue_0035_delivery_timing_message_page import Issue0035DeliveryTimingMessagePage


@pytest.fixture
def delivery_timing_message_page(page) -> Issue0035DeliveryTimingMessagePage:
    """Create page object for issue_0035 tests."""
    return Issue0035DeliveryTimingMessagePage(page)
