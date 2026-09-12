"""Page object for issue_0052 - Responsive layout across common viewports."""
from playwright.sync_api import Page


class Issue0052ResponsiveLayoutPage:
    """Page object for responsive layout."""

    def __init__(self, page: Page):
        self.page = page

    def set_viewport(self, width: int, height: int) -> None:
        """Set the viewport size."""
        self.page.set_viewport_size({"width": width, "height": height})

    def page_should_render_without_horizontal_overflow(self) -> None:
        """Verify page renders without horizontal overflow."""
        # Get the scroll width and client width
        scroll_width = self.page.evaluate("() => document.documentElement.scrollWidth")
        client_width = self.page.evaluate("() => document.documentElement.clientWidth")
        assert scroll_width <= client_width + 5, f"Page has horizontal overflow: scrollWidth={scroll_width}, clientWidth={client_width}"
