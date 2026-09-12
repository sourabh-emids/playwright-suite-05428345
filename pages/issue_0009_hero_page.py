"""Page object for issue_0009 - Hero section rendering and H1 uniqueness."""
from playwright.sync_api import Page, expect

from locators.issue_0009_hero_locators import Issue0009HeroLocators


class Issue0009HeroPage:
    """Page object for hero section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0009HeroLocators()
        self.locators.page = page

    def view_hero_section(self) -> None:
        """View the hero section."""
        pass

    def hero_section_should_be_visible(self) -> None:
        """Verify hero section is visible."""
        expect(self.locators.hero_section).to_be_visible()

    def there_should_be_exactly_one_h1(self) -> None:
        """Verify exactly one H1 heading exists."""
        count = self.page.get_by_role("heading", level=1).count()
        assert count == 1, f"Expected exactly 1 H1, but found {count}"

    def h1_should_contain_text(self) -> None:
        """Verify H1 contains expected text."""
        expect(self.locators.h1_heading).to_contain_text("In Healthcare, Only Outcomes Matter")

    def subtitle_should_be_present(self) -> None:
        """Verify subtitle is present."""
        expect(self.locators.hero_subtitle).to_be_visible()
