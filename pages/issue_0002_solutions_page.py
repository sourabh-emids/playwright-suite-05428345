"""Page object for issue_0002 - Solutions mega-menu functionality."""
from playwright.sync_api import Page, expect

from locators.issue_0002_solutions_menu_locators import Issue0002SolutionsMenuLocators


class Issue0002SolutionsMenuPage:
    """Page object for Solutions mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0002SolutionsMenuLocators()
        self.locators.page = page

    def click_solutions_navigation(self) -> None:
        """Click the Solutions navigation item."""
        self.locators.solutions_nav_button.click()

    def mega_menu_should_appear(self) -> None:
        """Verify mega-menu appears."""
        expect(self.locators.solutions_by_initiative_header).to_be_visible()

    def menu_should_display_initiative_section(self) -> None:
        """Verify 'Solutions by Initiative' section is displayed."""
        expect(self.locators.solutions_by_initiative_header).to_be_visible()

    def menu_should_display_solution(self, solution: str) -> None:
        """Verify a solution is displayed in the menu."""
        link = self.page.get_by_role("link", name=solution)
        expect(link).to_be_visible()

    def menu_should_display_industry_section(self) -> None:
        """Verify 'Browse By Industry' section is displayed."""
        expect(self.locators.browse_by_industry_header).to_be_visible()

    def menu_should_display_industry(self, industry: str) -> None:
        """Verify an industry is displayed in the menu."""
        link = self.page.get_by_role("link", name=industry)
        expect(link).to_be_visible()

    def menu_should_display_portfolio_section(self) -> None:
        """Verify 'The Portfolio' section is displayed."""
        expect(self.locators.the_portfolio_header).to_be_visible()

    def solution_links_should_be_clickable(self) -> None:
        """Verify solution links are clickable."""
        expect(self.locators.modernization_link).to_be_enabled()
        expect(self.locators.interoperability_link).to_be_enabled()
        expect(self.locators.cloud_transformation_link).to_be_enabled()
        expect(self.locators.agentic_ai_link).to_be_enabled()
        expect(self.locators.global_capability_center_link).to_be_enabled()

    def industry_links_should_be_clickable(self) -> None:
        """Verify industry links are clickable."""
        expect(self.locators.payers_link).to_be_enabled()
        expect(self.locators.providers_link).to_be_enabled()
        expect(self.locators.health_tech_link).to_be_enabled()
        expect(self.locators.life_sciences_link).to_be_enabled()

    def explore_all_solutions_link_should_be_present(self) -> None:
        """Verify 'Explore all solutions' link is present."""
        expect(self.locators.explore_all_solutions_link).to_be_visible()

    def mega_menu_should_close(self) -> None:
        """Verify mega-menu closes (by checking menu is not visible)."""
        # Menu closing is indicated by Solutions button having aria-expanded="false"
        expect(self.locators.solutions_nav_button).to_have_attribute("aria-expanded", "false")

    def click_modernization_solution(self) -> None:
        """Click the Modernization solution link."""
        self.locators.modernization_link.click()

    def should_be_on_modernization_page(self) -> None:
        """Verify user is on the Modernization page."""
        expect(self.page).to_have_url("**/solutions/modernization-as-a-service/**")
