"""Test for issue_0013 - See the model CTA routing and operation."""
import pytest

from pages.issue_0013_see_model_cta_page import Issue0013SeeModelCTAPage


@pytest.fixture
def see_model_cta_page(page) -> Issue0013SeeModelCTAPage:
    """Create page object for issue_0013 tests."""
    return Issue0013SeeModelCTAPage(page)
