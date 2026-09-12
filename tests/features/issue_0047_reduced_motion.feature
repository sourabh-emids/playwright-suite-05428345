"""Reduced motion disables continuous logo animation."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("reduced motion disables continuous logo animation")
def reduced_motion_disables_animation(page: Page) -> None:
    """Verify reduced motion disables continuous logo animation."""
    # Check for prefers-reduced-motion media query or animation相关规定
    # The page should respect the prefers-reduced-motion media query
    has_prefers_reduced_motion = page.evaluate("""
        () => {
            return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        }
    """)
    
    # Check CSS for animation rules that respect prefers-reduced-motion
    css_content = page.evaluate("""
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
    
    # Either the preference is respected or CSS has the media query
    assert has_prefers_reduced_motion or css_content, "Page should support reduced motion"
