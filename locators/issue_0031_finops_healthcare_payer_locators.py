"""Locators for issue_0031 - FinOps healthcare payer resource card display."""
from playwright.sync_api import Locator


class Issue0031FinopsHealthcarePayerLocators:
    """Locators for FinOps healthcare payer card."""

    @property
    def finops_card(self) -> Locator:
        """Return the FinOps resource card."""
        return self.page.get_by_role("link", name="FinOps Principles: 4 Best Practices for Healthcare Payers")
