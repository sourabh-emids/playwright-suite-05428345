"""Page object for issue_0025: Impact metrics render correctly"""

from playwright.sync_api import Page, expect

from locators.issue_0025_impact_metrics_render_correctly_locators import Issue0025ImpactLocators


class Issue0025ImpactPage:
    """Page object for Impact metrics."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0025ImpactLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_metrics_visible(self) -> None:
        """Verify Impact metrics are visible."""
        expect(self.locators.impact_section).to_be_visible()
        expect(self.locators.metrics_text).to_be_visible()

    def verify_currency_symbols(self) -> None:
        """Verify currency symbols are present."""
        content = self.page.content()
        expect("$" in content).to_be(True)
