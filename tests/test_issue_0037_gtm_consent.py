"""Test for issue_0037 - Google Tag Manager consent-governed loading."""
import pytest

from pages.issue_0037_gtm_consent_page import Issue0037GTMConsentPage


@pytest.fixture
def gtm_consent_page(page) -> Issue0037GTMConsentPage:
    """Create page object for issue_0037 tests."""
    return Issue0037GTMConsentPage(page)
