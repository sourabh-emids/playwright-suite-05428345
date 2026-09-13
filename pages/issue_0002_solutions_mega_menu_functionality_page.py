"""Page object for issue_0002: Solutions mega-menu functionality"""

from playwright.sync_api import Page, expect

from locators.issue_0002_solutions_mega_menu_functionality_locators import Issue0002SolutionsMenuLocators


class Issue0002SolutionsMenuPage:
    """Page object for Solutions mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0002SolutionsMenuLocators(page)

    def open_solutions_menu(self) -> None:
        """Open the Solutions mega-menu."""
        self.locators.solutions_nav_button.click()

    def close_solutions_menu(self) -> None:
        """Close the Solutions mega-menu by pressing Escape."""
        self.page.keyboard.press("Escape")

    def click_outside_menu(self) -> None:
        """Click outside the menu to close it."""
        self.page.locator("main").click()

    def verify_menu_opened(self) -> None:
        """Verify the Solutions menu is open."""
        expect(self.locators.solutions_nav_button).to_be_visible()

    def verify_solution_groupings_visible(self) -> None:
        """Verify solution groups with headings are visible."""
        expect(self.locators.solutions_by_initiative_heading).to_be_visible()
        expect(self.locators.browse_by_industry_heading).to_be_visible()
        expect(self.locators.portfolio_heading).to_be_visible()

    def click_solution_link(self, link_text: str) -> None:
        """Click a specific solution link."""
        self.page.get_by_role("link", name=link_text).first.click()

    def verify_valid_destination(self) -> None:
        """Verify navigation to a valid destination."""
        self.page.wait_for_load_state("domcontentloaded")
        # Verify no 404 error page
        expect(self.page).not_to_have_title("/404/")

    def navigate_menu_with_keyboard(self) -> None:
        """Navigate through menu using keyboard."""
        self.page.keyboard.press("Tab")

    def get_current_url(self) -> str:
        """Get the current page URL."""
        return self.page.url

    def focus_on_solutions_button(self) -> None:
        """Focus on the Solutions button."""
        self.locators.solutions_nav_button.focus()

    def resize_to_mobile(self) -> None:
        """Resize browser to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})

    def get_solution_item_count(self) -> int:
        """Get the count of solution items in the menu."""
        return self.locators.get_all_solution_links().count()

    def get_solution_items(self) -> list[Locator]:
        """Get all solution items as locators."""
        return self.locators.get_all_solution_links().all()
