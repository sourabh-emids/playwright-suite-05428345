"""Page object for issue_0055 - Homepage modal behavior default state."""
from playwright.sync_api import Page, expect


class Issue0055HomepageModalBehaviorPage:
    """Page object for homepage modal behavior."""

    def __init__(self, page: Page):
        self.page = page

    def page_loads(self) -> None:
        """Wait for page to load."""
        self.page.wait_for_load_state("domcontentloaded")

    def no_modal_should_be_visible_by_default(self) -> None:
        """Verify no modal is visible by default."""
        modals = self.page.locator("[role='dialog'], [class*='modal']")
        for i in range(modals.count()):
            modal = modals.nth(i)
            if await modal.is_visible():
                # Modal should have aria-hidden or be closed
                aria_hidden = await modal.get_attribute("aria-hidden")
                assert aria_hidden == "true" or not await modal.is_visible(), "Modal should not be visible by default"

    def main_content_should_be_accessible(self) -> None:
        """Verify main content is accessible."""
        main = self.page.locator("main")
        expect(main).to_be_attached()
