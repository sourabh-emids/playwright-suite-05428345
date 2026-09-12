"""Page object for issue_0016 - All Solutions CTA visibility and routing."""
from playwright.sync_api import Page, expect

from locators.issue_0016_all_solutions_cta_locators import Issue0016AllSolutionsCTALocators


class Issue0016AllSolutionsCTAPage:
    """Page object for All Solutions CTA."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0016AllSolutionsCTALocators()
        self.locators.page = page

    def view_featured_solutions_section(self) -> None:
        """Scroll to the Featured Solutions section."""
        self.locators.all_solutions_cta.scroll_into_view_if_needed()

    def all_solutions_cta_should_be_visible(self) -> None:
        """Verify All solutions CTA is visible."""
        expect(self.locators.all_solutions_cta).to_be_visible()

    def cta_should_link_to_solutions_page(self) -> None:
        """Verify CTA links to solutions page."""
        expect(self.locators.all_solutions_cta).to_have_attribute(
            "href", "https://www.emids.com/solutions/"
        )

    def click_all_solutions_cta(self) -> None:
        """Click the All solutions CTA."""
        self.locators.all_solutions_cta.click()

    def should_be_on_solutions_page(self) -> None:
        """Verify user is on the solutions page."""
        expect(self.page).to_have_url("**/solutions/**")
