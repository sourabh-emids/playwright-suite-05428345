"""Test for issue_0031 - FinOps healthcare payer resource card display."""
import pytest

from pages.issue_0031_finops_healthcare_payer_page import Issue0031FinopsHealthcarePayerPage


@pytest.fixture
def finops_healthcare_payer_page(page) -> Issue0031FinopsHealthcarePayerPage:
    """Create page object for issue_0031 tests."""
    return Issue0031FinopsHealthcarePayerPage(page)
