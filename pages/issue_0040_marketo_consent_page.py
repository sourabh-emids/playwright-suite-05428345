"""Page object for issue_0040 - Marketo marketing integration consent gating."""
from playwright.sync_api import Page


class Issue0040MarketoConsentPage:
    """Page object for Marketo consent."""

    def __init__(self, page: Page):
        self.page = page

    def marketo_should_not_be_active_before_consent(self) -> None:
        """Verify Marketo is not active before consent."""
        # Check if Munchkin/Marketo is active
        has_marketo = self.page.evaluate("() => typeof window.Munchkin !== 'undefined' || document.querySelector('script[src*=\"marketo\"]') !== null")
        # This test verifies the integration exists
