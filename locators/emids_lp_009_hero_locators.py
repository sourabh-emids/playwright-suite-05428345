"""Locators for emids_lp_009: Render hero messaging and visual."""
from playwright.sync_api import Locator, Page


class HeroLocators:
    """Hero section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_section(self) -> Locator:
        """Hero section container."""
        return self.page.locator("section").filter(has=self.page.get_by_role("heading", level=1)).first

    @property
    def h1_heading(self) -> Locator:
        """Primary H1 heading."""
        return self.page.get_by_role("heading", level=1)

    @property
    def h2_subheading(self) -> Locator:
        """H2 supporting heading."""
        return self.page.get_by_role("heading", level=2).first

    @property
    def hero_body_copy(self) -> Locator:
        """Hero body copy text."""
        return self.page.get_by_role("heading", level=2).locator("..").locator("..").locator("p").first

    @property
    def hero_cta(self) -> Locator:
        """Hero primary CTA button."""
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def hero_media(self) -> Locator:
        """Hero media element (image/video)."""
        return self.page.locator("img").first

    @property
    def all_h1s(self) -> Locator:
        """All H1 elements on page."""
        return self.page.get_by_role("heading", level=1)

    @property
    def hero_tagline(self) -> Locator:
        """AI · Engineering · Platforms tagline."""
        return self.page.get_by_text("AI · Engineering · Platforms")
