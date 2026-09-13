"""Page object for issue_0016: All Solutions CTA functionality"""

from playwright.sync_api import Page, expect

from locators.issue_0016_all_solutions_cta_functionality_locators import Issue0016AllSolutionsCTALocators


class Issue0016AllSolutionsCTAPage:
    """Page object for All Solutions CTA."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0016AllSolutionsCTALocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def click_all_solutions_cta(self) -> None:
        """Click the All Solutions CTA."""
        self.locators.all_solutions_cta.click()

    def verify_cta_visible(self) -> None:
        """Verify CTA is visible."""
        expect(self.locators.all_solutions_cta).to_be_visible()

    def verify_routes_to_solutions(self) -> None:
        """Verify navigation to solutions page."""
        expect(self.page).to_have_url("https://www.emids.com/solutions/")

    def verify_canonical_url(self) -> None:
        """Verify URL is canonical."""
        href = self.locators.all_solutions_cta.get_attribute("href")
        expect(href).to_match(r"^https://www\.emids\.com/solutions/?$")
