"""Page object for issue_0019 - Reduced motion preference for partner animation."""
from playwright.sync_api import Page, expect

from locators.issue_0019_reduced_motion_locators import Issue0019ReducedMotionLocators


class Issue0019ReducedMotionPage:
    """Page object for reduced motion preference."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0019ReducedMotionLocators()
        self.locators.page = page

    def set_reduced_motion_preference(self) -> None:
        """Set reduced motion preference."""
        self.page.emulate_media(reduced_motion="reduce")

    def view_partnerships_section(self) -> None:
        """Scroll to the Partnerships section."""
        self.locators.partnerships_section.scroll_into_view_if_needed()

    def animation_should_be_reduced_or_disabled(self) -> None:
        """Verify animation is reduced or disabled with reduced motion preference."""
        # Check that animation-related CSS is not active
        carousel = self.locators.partner_carousel
        if carousel.count() > 0:
            animation_duration = await carousel.first.evaluate(
                "el => window.getComputedStyle(el).animationDuration"
            )
            animation_play_state = await carousel.first.evaluate(
                "el => window.getComputedStyle(el).animationPlayState"
            )
            # Animation should be paused or have zero duration
            assert animation_duration == "0s" or animation_play_state == "paused", \
                "Animation should be reduced or disabled with prefers-reduced-motion"
