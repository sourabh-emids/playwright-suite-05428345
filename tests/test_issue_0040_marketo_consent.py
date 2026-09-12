"""Test for issue_0040 - Marketo marketing integration consent gating."""
import pytest

from pages.issue_0040_marketo_consent_page import Issue0040MarketoConsentPage


@pytest.fixture
def marketo_consent_page(page) -> Issue0040MarketoConsentPage:
    """Create page object for issue_0040 tests."""
    return Issue0040MarketoConsentPage(page)
