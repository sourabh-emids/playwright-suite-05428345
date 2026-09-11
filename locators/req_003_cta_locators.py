"""Locators for REQ-003: Primary CTA buttons function correctly."""

from playwright.sync_api import Page, Locator


class Req003CtaLocators:
    """Locators for CTA button elements."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def see_how_we_deliver_outcomes_link(self) -> Locator:
        """'See How We Deliver Outcomes' link on homepage."""
        return self._page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def see_the_model_link(self) -> Locator:
        """'See the model' link on homepage."""
        return self._page.get_by_role("link", name="See the model")

    @property
    def all_solutions_link(self) -> Locator:
        """'All solutions' link on homepage."""
        return self._page.get_by_role("link", name="All solutions")

    @property
    def connect_cta_link(self) -> Locator:
        """'Connect' CTA link on homepage."""
        return self._page.get_by_role("link", name="Connect").last

    @property
    def contact_button(self) -> Locator:
        """Contact Us button."""
        return self._page.get_by_role("button", name="Contact Us")

    @property
    def learn_more_button(self) -> Locator:
        """Learn More button."""
        return self._page.get_by_role("button", name="Learn More")

    @property
    def forward_deployed_section(self) -> Locator:
        """Forward-Deployed Context Engineering section."""
        return self._page.get_by_role("heading", name="Forward-Deployed Context Engineering")

    @property
    def ai_capabilities_section(self) -> Locator:
        """AI Capabilities section."""
        return self._page.get_by_role("heading", name="Capabilities that deliver on ambitious goals")

    @property
    def solutions_section(self) -> Locator:
        """Featured solutions section."""
        return self._page.get_by_role("heading", name="Measurable outcomes, prescribed for healthcare's hardest problems")
