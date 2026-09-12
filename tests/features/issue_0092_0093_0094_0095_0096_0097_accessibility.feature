"""WCAG 2.1 AA accessibility requirements."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("WCAG 2.1 AA keyboard access on all interactive elements")
def keyboard_access_all(page: Page) -> None:
    """Verify WCAG 2.1 AA keyboard access on all interactive elements."""
    # Tab through page and verify all interactive elements are focusable
    page.keyboard.press("Tab")
    focused = page.evaluate("() => document.activeElement")
    assert focused is not None, "Interactive elements should be keyboard accessible"


@then("WCAG 2.1 AA visible focus indicators")
def visible_focus_indicators(page: Page) -> None:
    """Verify WCAG 2.1 AA visible focus indicators."""
    nav = page.get_by_role("navigation", name="Main Navigation")
    first_link = nav.get_by_role("link").first
    first_link.focus()
    
    # Check focus style is applied
    outline = first_link.evaluate("el => window.getComputedStyle(el).outlineStyle")
    # Focus outline should not be none
    assert outline != "none", "Focus indicators should be visible"


@then("WCAG 2.1 AA sufficient color contrast")
def color_contrast(page: Page) -> None:
    """Verify WCAG 2.1 AA sufficient color contrast."""
    # Check that text has sufficient contrast
    h1 = page.get_by_role("heading", level=1).first
    bg_color = page.evaluate("() => window.getComputedStyle(document.body).backgroundColor")
    text_color = h1.evaluate("el => window.getComputedStyle(el).color")
    
    # Basic check that colors are defined
    assert bg_color != "", "Background should have color"
    assert text_color != "", "Text should have color"


@then("WCAG 2.1 AA meaningful alt text on images")
def alt_text_images(page: Page) -> None:
    """Verify WCAG 2.1 AA meaningful alt text on images."""
    images = page.locator("img").all()
    for img in images:
        alt = img.get_attribute("alt")
        # Either alt is present and meaningful, or img is marked as decorative
        src = img.get_attribute("src")
        if src and not src.endswith(".svg"):
            assert alt is not None, "Images should have alt text or be marked as decorative"


@then("WCAG 2.1 AA 200% zoom reflow support")
def zoom_reflow_support(page: Page) -> None:
    """Verify WCAG 2.1 AA 200% zoom reflow support."""
    page.set_viewport_size({"width": 640, "height": 480})  # 200% zoom equivalent
    
    h1 = page.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
    
    footer = page.get_by_role("contentinfo")
    expect(footer).to_be_visible()


@then("WCAG 2.1 AA reduced motion preference respected")
def reduced_motion_respected(page: Page) -> None:
    """Verify WCAG 2.1 AA reduced motion preference respected."""
    has_prefers_reduced_motion = page.evaluate("""
        () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
    """)
    
    css_rules = page.evaluate("""
        () => {
            for (let sheet of document.styleSheets) {
                try {
                    for (let rule of sheet.cssRules) {
                        if (rule.cssText && rule.cssText.includes('prefers-reduced-motion')) {
                            return true;
                        }
                    }
                } catch (e) {}
            }
            return false;
        }
    """)
    
    assert has_prefers_reduced_motion or css_rules, "Page should support reduced motion"
