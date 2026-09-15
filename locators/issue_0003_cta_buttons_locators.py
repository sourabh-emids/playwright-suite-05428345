"""Locators for issue_0003: Primary CTA buttons function properly."""
from playwright.sync_api import Page, Locator


class CtaButtonsLocators:
    """Locators for CTA buttons on the homepage."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def see_how_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").last

    @property
    def see_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model")

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions")
