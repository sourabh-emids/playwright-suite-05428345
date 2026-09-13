"""Locators for emids_lp_014: Maintain semantic section hierarchy."""
from playwright.sync_api import Locator, Page


class GlobalLocators:
    """Global section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def all_h1s(self) -> Locator:
        """All H1 elements."""
        return self.page.get_by_role("heading", level=1)

    @property
    def all_h2s(self) -> Locator:
        """All H2 elements."""
        return self.page.get_by_role("heading", level=2)

    @property
    def all_h3s(self) -> Locator:
        """All H3 elements."""
        return self.page.get_by_role("heading", level=3)

    @property
    def main_landmark(self) -> Locator:
        """Main landmark."""
        return self.page.get_by_role("main")

    @property
    def header_landmark(self) -> Locator:
        """Header landmark."""
        return self.page.get_by_role("banner")

    @property
    def footer_landmark(self) -> Locator:
        """Footer landmark."""
        return self.page.get_by_role("contentinfo")

    @property
    def navigation_landmarks(self) -> Locator:
        """Navigation landmarks."""
        return self.page.get_by_role("navigation")

    @property
    def all_sections(self) -> Locator:
        """Section landmarks."""
        return self.page.get_by_role("region")


class FeaturedSolutionsLocators:
    """Featured Solutions section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("Featured solutions")

    @property
    def all_solutions(self) -> Locator:
        """All solution cards."""
        return self.page.get_by_role("link", name__regex=r"^Explore solution:")

    @property
    def solution_01(self) -> Locator:
        """Solution 01 - Modernization as a Service."""
        return self.page.get_by_role("link", name="Explore solution: Modernization as a Service")

    @property
    def solution_02(self) -> Locator:
        """Solution 02 - Interoperability."""
        return self.page.get_by_role("link", name="Explore solution: Interoperability")

    @property
    def solution_03(self) -> Locator:
        """Solution 03 - Cloud Migration."""
        return self.page.get_by_role("link", name="Explore solution: Cloud Migration")

    @property
    def solution_04(self) -> Locator:
        """Solution 04 - Global Capability Center."""
        return self.page.get_by_role("link", name="Explore solution: Global Capability Center")

    @property
    def solution_05(self) -> Locator:
        """Solution 05 - Epic Implementation."""
        return self.page.get_by_role("link", name="Explore solution: Epic Implementation")

    @property
    def solution_06(self) -> Locator:
        """Solution 06 - Agentic AI."""
        return self.page.get_by_role("link", name="Explore solution: Agentic AI")

    @property
    def all_solutions_cta(self) -> Locator:
        """All solutions CTA."""
        return self.page.get_by_role("link", name="All solutions")

    @property
    def solution_numbers(self) -> Locator:
        """Solution number badges (01-06)."""
        return self.page.locator("text=01, text=02, text=03, text=04, text=05, text=06").first


class PartnershipsLocators:
    """Partnerships section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("Partnerships")

    @property
    def partner_logos(self) -> Locator:
        """Partner logo images."""
        return self.page.get_by_role("img", name__regex=r"Logo|Partner|logo|partner")

    @property
    def marquee_container(self) -> Locator:
        """Marquee animation container."""
        return self.page.locator("[class*='marquee'], [data-marquee]").first


class CapabilitiesSectionLocators:
    """Capabilities section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("Capabilities")

    @property
    def ai_group(self) -> Locator:
        """AI capability group."""
        return self.page.get_by_role("heading", name="Artificial Intelligence")

    @property
    def engineering_group(self) -> Locator:
        """Engineering capability group."""
        return self.page.get_by_role("heading", name="Engineering")

    @property
    def platforms_group(self) -> Locator:
        """Platforms capability group."""
        return self.page.get_by_role("heading", name="Platforms")

    @property
    def all_capability_cards(self) -> Locator:
        """All capability cards."""
        return self.page.locator("[class*='capability'], [class*='card']").filter(has=self.page.get_by_role("heading"))


class WhoWeServeLocators:
    """Who We Serve section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("Who we Serve")

    @property
    def payer_tab(self) -> Locator:
        """Payer audience tab."""
        return self.page.get_by_role("button", name="Payer")

    @property
    def provider_tab(self) -> Locator:
        """Provider audience tab."""
        return self.page.get_by_role("button", name="Provider")

    @property
    def healthtech_tab(self) -> Locator:
        """HealthTech audience tab."""
        return self.page.get_by_role("button", name="HealthTech")

    @property
    def life_sciences_tab(self) -> Locator:
        """Life Sciences audience tab."""
        return self.page.get_by_role("button", name="Life Sciences")

    @property
    def consumer_tab(self) -> Locator:
        """Consumer audience tab."""
        return self.page.get_by_role("button", name="Consumer")

    @property
    def explore_buttons(self) -> Locator:
        """Explore action buttons."""
        return self.page.get_by_role("link", name="Explore")
