"""Test for issue_0018 - Partner logo rail rendering and accessibility."""
import pytest

from pages.issue_0018_partner_logo_rail_page import Issue0018PartnerLogoRailPage


@pytest.fixture
def partner_logo_rail_page(page) -> Issue0018PartnerLogoRailPage:
    """Create page object for issue_0018 tests."""
    return Issue0018PartnerLogoRailPage(page)
