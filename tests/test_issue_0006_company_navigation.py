"""Test for issue_0006 - Company navigation group keyboard and touch access."""
import pytest

from pages.issue_0006_company_page import Issue0006CompanyMenuPage


@pytest.fixture
def company_menu_page(page) -> Issue0006CompanyMenuPage:
    """Create page object for issue_0006 tests."""
    return Issue0006CompanyMenuPage(page)
