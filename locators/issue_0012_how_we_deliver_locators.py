"""Locators for issue_0012 - How We Deliver section content rendering."""
from playwright.sync_api import Locator


class Issue0012HowWeDeliverLocators:
    """Locators for How We Deliver section."""

    @property
    def how_we_deliver_section(self) -> Locator:
        """Return the How We Deliver section."""
        return self.page.locator("text=Forward-deployed context engineering")

    @property
    def fdce_heading(self) -> Locator:
        """Return the FDCE heading."""
        return self.page.get_by_role("heading", name="Forward-Deployed Context Engineering")

    @property
    def fdce_description(self) -> Locator:
        """Return the FDCE description text."""
        return self.page.locator("text=Forward-deployed context engineering turns ambition")

    @property
    def feature_list(self) -> Locator:
        """Return the feature list."""
        return self.fdce_heading.locator("..").locator("ul, ol")
