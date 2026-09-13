"""Locators for emids_lp_012: Render How We Deliver section."""
from playwright.sync_api import Locator, Page


class HowWeDeliverLocators:
    """How We Deliver section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading container."""
        return self.page.get_by_text("How We Deliver")

    @property
    def main_heading(self) -> Locator:
        """Main heading (H2)."""
        return self.page.get_by_role("heading", name="Embedded healthcare expertise")

    @property
    def body_copy(self) -> Locator:
        """Body copy paragraph."""
        return self.page.get_by_text("Forward-deployed context engineering turns ambition into measurable outcomes")

    @property
    def see_model_cta(self) -> Locator:
        """See the model CTA link."""
        return self.page.get_by_role("link", name="See the model")

    @property
    def fdce_heading(self) -> Locator:
        """Forward-Deployed Context Engineering H3."""
        return self.page.get_by_role("heading", name="Forward-Deployed Context Engineering")

    @property
    def timeline_list(self) -> Locator:
        """Timeline list items."""
        return self.page.get_by_role("list").filter(has=self.page.get_by_text("1 Day"))

    @property
    def all_h2s(self) -> Locator:
        """All H2 headings."""
        return self.page.get_by_role("heading", level=2)

    @property
    def all_h3s(self) -> Locator:
        """All H3 headings."""
        return self.page.get_by_role("heading", level=3)
