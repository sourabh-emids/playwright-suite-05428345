"""Test for issue_0034 - Final conversion banner rendering and CTA."""
import pytest

from pages.issue_0034_final_conversion_banner_page import Issue0034FinalConversionBannerPage


@pytest.fixture
def final_conversion_banner_page(page) -> Issue0034FinalConversionBannerPage:
    """Create page object for issue_0034 tests."""
    return Issue0034FinalConversionBannerPage(page)
