"""Locators for issue_0012: How We Deliver section render"""

from playwright.sync_api import Page, Locator


class Issue0012HowWeDeliverLocators:
    """Locators for How We Deliver section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def how_we_deliver_section(self) -> Locator:
        """Returns the How We Deliver section."""
        return self.page.get_by_text("Forward-Deployed Context Engineering").locator("..").locator("..")

    @property
    def fdce_heading(self) -> Locator:
        """Returns the FDCE heading."""
        return self.page.get_by_role("heading", level=3, name="Forward-Deployed Context Engineering")

    @property
    def see_model_cta(self) -> Locator:
        """Returns the See the model CTA."""
        return self.page.get_by_role("link", name="See the model")

    @property
    def section_title(self) -> Locator:
        """Returns the section title."""
        return self.page.get_by_text("Forward-Deployed Context Engineering")

    @property
    def section_copy(self) -> Locator:
        """Returns the section body copy."""
        return self.page.get_by_text("Forward-deployed context engineering turns ambition into measurable outcomes.")
