"""Locators for issue_0002: Solutions mega-menu functionality"""

from playwright.sync_api import Page, Locator


class Issue0002SolutionsMenuLocators:
    """Locators for the Solutions mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_nav_button(self) -> Locator:
        """Returns the Solutions navigation button."""
        return self.page.get_by_role("button", name="Solutions")

    @property
    def solutions_menu(self) -> Locator:
        """Returns the Solutions mega-menu container."""
        return self.page.locator("button:has-text('Solutions') + *, button:has-text('Solutions') ~ *").first

    @property
    def solutions_by_initiative_heading(self) -> Locator:
        """Returns the 'Solutions by Initiative' heading."""
        return self.page.get_by_text("Solutions by Initiative")

    @property
    def browse_by_industry_heading(self) -> Locator:
        """Returns the 'Browse By Industry' heading."""
        return self.page.get_by_text("Browse By Industry")

    @property
    def portfolio_heading(self) -> Locator:
        """Returns the 'The Portfolio' heading."""
        return self.page.get_by_text("The Portfolio")

    def get_solution_group_links(self, group_name: str) -> Locator:
        """Returns links within a specific solution group."""
        return self.page.get_by_role("link", name=group_name)

    def get_all_solution_links(self) -> Locator:
        """Returns all solution links in the menu."""
        return self.page.locator("header a, header button + * a")
