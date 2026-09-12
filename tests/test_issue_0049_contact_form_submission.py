"""Test for issue_0049 - Contact form submission feedback and retry."""
import pytest

from pages.issue_0049_contact_form_submission_page import Issue0049ContactFormSubmissionPage


@pytest.fixture
def contact_form_submission_page(page) -> Issue0049ContactFormSubmissionPage:
    """Create page object for issue_0049 tests."""
    return Issue0049ContactFormSubmissionPage(page)
