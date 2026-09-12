"""Test for issue_0050 - WCAG 2.1 AA compliance across landing page."""
import pytest

from pages.issue_0050_wcag_compliance_page import Issue0050WCAGCompliancePage


@pytest.fixture
def wcag_compliance_page(page) -> Issue0050WCAGCompliancePage:
    """Create page object for issue_0050 tests."""
    return Issue0050WCAGCompliancePage(page)
