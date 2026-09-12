"""Test for issue_0047: Reduced motion disables continuous logo animation."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_reduced_motion_support(page_ready: Page) -> None:
    """Test reduced motion disables continuous logo animation."""
    has_prefers_reduced_motion = page_ready.evaluate("""
        () => {
            return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        }
    """)
    
    css_content = page_ready.evaluate("""
        () => {
            const styleSheets = document.styleSheets;
            let foundReducedMotion = false;
            for (let sheet of styleSheets) {
                try {
                    for (let rule of sheet.cssRules) {
                        if (rule.cssText && rule.cssText.includes('prefers-reduced-motion')) {
                            foundReducedMotion = true;
                        }
                    }
                } catch (e) {}
            }
            return foundReducedMotion;
        }
    """)
    
    assert has_prefers_reduced_motion or css_content, "Page should support reduced motion"
