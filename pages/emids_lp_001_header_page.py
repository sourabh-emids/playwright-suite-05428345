"""Page object for emids_lp_001 - Header basic rendering."""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class HeaderPage(BasePage):
    """Page object for the global header."""

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def logo(self) -> Locator:
        return self.page.locator("header").get_by_role("link", name="Emids logo").or_(self.page.locator("header img").first)

    @property
    def navigation(self) -> Locator:
        return self.page.locator("header navigation, header nav, header [role='navigation']").first

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def connect_ctas(self) -> Locator:
        return self.page.locator("header a:has-text('Connect')")

    @property
    def navigation_items(self) -> Locator:
        return self.page.locator("header nav a, header nav button")

    @property
    def all_nav_links(self) -> Locator:
        return self.page.locator("header a")

    @property
    def mobile_menu_toggle(self) -> Locator:
        return self.page.locator("[aria-label='Menu'], button:has-text('Menu'), .menu-toggle").first


class SolutionsMenuPage(BasePage):
    """Page object for Solutions mega-menu."""

    @property
    def solutions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions").or_(self.page.locator("header nav a:has-text('Solutions')")).first

    def hover_solutions_button(self) -> None:
        self.solutions_button.hover()

    def click_solutions_button(self) -> None:
        self.solutions_button.click()

    @property
    def mega_menu(self) -> Locator:
        return self.page.locator("[role='menu'], .mega-menu, .solutions-dropdown").first

    @property
    def solutions_heading(self) -> Locator:
        return self.page.locator("text=Solutions by Initiative, text=Solutions").first

    @property
    def solution_links(self) -> Locator:
        return self.page.locator(".mega-menu a, [role='menu'] a")

    @property
    def mobile_menu(self) -> Locator:
        return self.page.locator(".mobile-menu, .drawer, .disclosure")

    def close_menu(self) -> None:
        self.page.keyboard.press("Escape")


class CapabilitiesMenuPage(BasePage):
    """Page object for Capabilities mega-menu."""

    @property
    def capabilities_button(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities").or_(self.page.locator("header a:has-text('Capabilities')")).first

    def click_capabilities_button(self) -> None:
        self.capabilities_button.click()

    @property
    def capabilities_menu(self) -> Locator:
        return self.page.locator(".mega-menu, .capabilities-dropdown, [role='menu']").first

    @property
    def ai_group(self) -> Locator:
        return self.page.locator("text=AI").first

    @property
    def engineering_group(self) -> Locator:
        return self.page.locator("text=Engineering").first

    @property
    def platforms_group(self) -> Locator:
        return self.page.locator("text=Platforms").first

    @property
    def ai_label(self) -> Locator:
        return self.page.locator(".capabilities-menu h3:has-text('AI'), .mega-menu h3:has-text('AI')").first

    @property
    def engineering_label(self) -> Locator:
        return self.page.locator(".capabilities-menu h3:has-text('Engineering'), .mega-menu h3:has-text('Engineering')").first

    @property
    def platforms_label(self) -> Locator:
        return self.page.locator(".capabilities-menu h3:has-text('Platforms'), .mega-menu h3:has-text('Platforms')").first

    @property
    def capability_links(self) -> Locator:
        return self.page.locator(".capabilities-menu a, .mega-menu a")

    @property
    def all_capability_labels(self) -> Locator:
        return self.page.locator(".capabilities-menu h3, .mega-menu h3")


class IndustriesMenuPage(BasePage):
    """Page object for Industries mega-menu."""

    @property
    def industries_button(self) -> Locator:
        return self.page.get_by_role("button", name="Industries").or_(self.page.locator("header a:has-text('Industries')")).first

    def click_industries_button(self) -> None:
        self.industries_button.click()

    @property
    def industries_menu(self) -> Locator:
        return self.page.locator(".mega-menu, .industries-dropdown").first

    @property
    def payer_link(self) -> Locator:
        return self.page.locator("a[href*='/segments/payer/']").first

    @property
    def provider_link(self) -> Locator:
        return self.page.locator("a[href*='/segments/provider/']").first

    @property
    def healthtech_link(self) -> Locator:
        return self.page.locator("a[href*='/segments/healthtech/']").first

    @property
    def life_sciences_link(self) -> Locator:
        return self.page.locator("a[href*='/segments/life-sciences/']").first

    @property
    def consumer_link(self) -> Locator:
        return self.page.locator("a[href*='/segments/consumer/']").first

    @property
    def industry_links(self) -> Locator:
        return self.page.locator("a[href*='/segments/']")

    @property
    def industry_labels(self) -> Locator:
        return self.page.locator(".industries-menu h3, .mega-menu h3")

    @property
    def mobile_industry_list(self) -> Locator:
        return self.page.locator(".mobile-menu li, .stacked-list")


class InsightsMenuPage(BasePage):
    """Page object for Insights menu."""

    @property
    def insights_button(self) -> Locator:
        return self.page.get_by_role("button", name="Insights").or_(self.page.locator("header a:has-text('Insights')")).first

    def click_insights_button(self) -> None:
        self.insights_button.click()

    @property
    def insights_menu(self) -> Locator:
        return self.page.locator(".mega-menu, .insights-dropdown").first

    @property
    def insights_child_links(self) -> Locator:
        return self.page.locator(".insights-menu a, .mega-menu a[href*='/insights/']")

    @property
    def menu_groups(self) -> Locator:
        return self.page.locator(".insights-menu > div, .mega-menu section")


class CompanyMenuPage(BasePage):
    """Page object for Company menu."""

    @property
    def company_button(self) -> Locator:
        return self.page.get_by_role("button", name="Company").or_(self.page.locator("header a:has-text('Company')")).first

    def click_company_button(self) -> None:
        self.company_button.click()

    @property
    def company_menu(self) -> Locator:
        return self.page.locator(".mega-menu, .company-dropdown").first

    @property
    def menu_links(self) -> Locator:
        return self.page.locator(".company-menu a, .mega-menu a")


class ConnectCTAPage(BasePage):
    """Page object for Connect CTA."""

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def primary_connect_ctas(self) -> Locator:
        return self.page.locator("header a.primary:has-text('Connect'), header a.cta:has-text('Connect')")


class ResponsiveNavPage(BasePage):
    """Page object for responsive navigation."""

    @property
    def navigation(self) -> Locator:
        return self.page.locator("header nav, header navigation").first

    @property
    def menu_trigger(self) -> Locator:
        return self.page.locator("button.menu-toggle, [aria-label='Menu']").first

    @property
    def menu(self) -> Locator:
        return self.page.locator(".mobile-menu, nav[aria-expanded]").first

    @property
    def all_interactive_elements(self) -> Locator:
        return self.page.locator("header button, header a")
