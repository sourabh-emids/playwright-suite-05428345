"""Locators for issue_0045 - Footer legal navigation links."""
from playwright.sync_api import Locator


class Issue0045FooterLegalLinksLocators:
    """Locators for footer legal links."""

    @property
    def code_of_conduct_link(self) -> Locator:
        """Return the Code of Conduct link."""
        return self.page.get_by_role("link", name="Code of Conduct")

    @property
    def privacy_policy_link(self) -> Locator:
        """Return the Privacy Policy link."""
        return self.page.get_by_role("link", name="Privacy Policy")

    @property
    def transparency_in_coverage_link(self) -> Locator:
        """Return the Transparency in Coverage link."""
        return self.page.get_by_role("link", name="Transparency in Coverage")

    @property
    def cookie_policy_link(self) -> Locator:
        """Return the Cookie Policy link."""
        return self.page.get_by_role("link", name="Cookie Policy")

    @property
    def accessibility_statement_link(self) -> Locator:
        """Return the Accessibility Statement link."""
        return self.page.get_by_role("link", name="Accessibility Statement")
