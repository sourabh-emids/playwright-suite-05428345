"""Page object for emids_lp_002: Implement Solutions mega-menu."""
from playwright.sync_api import Page, expect
from locators.emids_lp_002_solutions_menu_locators import SolutionsMenuLocators


class SolutionsMenuPage:
    """Solutions mega-menu page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = SolutionsMenuLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def open_solutions_menu(self) -> None:
        """Open the Solutions mega-menu."""
        self.locators.solutions_nav.click()
        # Wait for menu to open
        self.page.wait_for_selector('[role="menu"]', state="visible", timeout=5000)

    def close_solutions_menu(self) -> None:
        """Close the Solutions mega-menu."""
        self.page.keyboard.press("Escape")
        # Or click outside
        self.locators.solutions_nav.click()

    def is_menu_open(self) -> bool:
        """Check if the Solutions menu is open."""
        try:
            return self.locators.solutions_button.get_attribute("aria-expanded") == "true"
        except Exception:
            return False

    def activate_menu_with_keyboard(self) -> None:
        """Activate menu using keyboard (Enter/Space)."""
        self.locators.solutions_nav.focus()
        self.page.keyboard.press("Enter")

    def click_solution_link(self, link_name: str) -> None:
        """Click a solution link by name."""
        link_lower = link_name.lower()
        if "modernization" in link_lower:
            self.locators.modernization_link.click()
        elif "interoperability" in link_lower:
            self.locators.interoperability_link.click()
        elif "cloud" in link_lower:
            self.locators.cloud_transformation_link.click()
        elif "agentic" in link_lower:
            self.locators.agentic_ai_link.click()
        elif "global capability" in link_lower:
            self.locators.global_capability_center_link.click()
        else:
            raise ValueError(f"Unknown solution link: {link_name}")

    def are_all_groups_visible(self) -> bool:
        """Check if all solution groups are visible."""
        return (
            self.locators.solutions_by_initiative.is_visible()
            and self.locators.browse_by_industry.is_visible()
            and self.locators.the_portfolio.is_visible()
        )

    def get_solution_urls(self) -> list[str]:
        """Get URLs of all solution links."""
        urls = []
        for link in self.locators.get_all_solution_links():
            href = link.get_attribute("href")
            if href:
                urls.append(href)
        return urls

    def is_solution_link_valid(self, link: "SolutionsMenuLocators") -> bool:
        """Check if a solution link has non-empty label and valid URL."""
        href = link.get_attribute("href")
        return href and href.strip() != "" and href.startswith("/")
