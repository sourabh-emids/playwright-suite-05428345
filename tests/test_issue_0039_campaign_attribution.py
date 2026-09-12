"""Test for issue_0039 - Campaign attribution parameters handling."""
import pytest

from pages.issue_0039_campaign_attribution_page import Issue0039CampaignAttributionPage


@pytest.fixture
def campaign_attribution_page(page) -> Issue0039CampaignAttributionPage:
    """Create page object for issue_0039 tests."""
    return Issue0039CampaignAttributionPage(page)
