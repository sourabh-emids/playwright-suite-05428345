"""Page object for All Solutions CTA functionality (issue_0016)."""
from playwright.sync_api import Page

from locators.issue_0016_all_solutions_cta_locators import AllSolutionsCTALocators


class AllSolutionsCTAPage:
    """Page object for All Solutions CTA functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = AllSolutionsCTALocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def click_cta(self) -> None:
        self.locators.all_solutions_cta.click()

    def get_href(self) -> str:
        return self.locators.all_solutions_cta.get_attribute("href")
