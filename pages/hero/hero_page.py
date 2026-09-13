"""Page object for emids_lp_009: Render hero messaging and visual."""
from playwright.sync_api import Page, expect
from locators.emids_lp_009_hero_locators import HeroLocators


class HeroPage:
    """Hero section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeroLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def get_h1_text(self) -> str:
        """Get H1 text content."""
        return self.locators.h1_heading.inner_text()

    def get_h1_count(self) -> int:
        """Get count of H1 elements on page."""
        return self.locators.all_h1s.count()

    def is_hero_cta_visible_without_scroll(self) -> bool:
        """Check if CTA is visible without deep scrolling."""
        cta = self.locators.hero_cta
        box = cta.bounding_box()
        if box:
            return box["y"] < 800  # Within initial viewport
        return False

    def is_body_copy_visible(self) -> bool:
        """Check if body copy is visible."""
        return self.locators.h2_subheading.is_visible()

    def get_media_url(self) -> str:
        """Get media element URL."""
        return self.locators.hero_media.get_attribute("src") or ""

    def click_hero_cta(self) -> None:
        """Click the hero CTA."""
        self.locators.hero_cta.click()

    def get_media_alt_text(self) -> str:
        """Get media alt text."""
        return self.locators.hero_media.get_attribute("alt") or ""

    def is_media_decorative(self) -> bool:
        """Check if media is marked as decorative."""
        alt = self.get_media_alt_text()
        return alt == "" or alt == "decorative"
