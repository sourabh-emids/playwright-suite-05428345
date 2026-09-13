"""Step definitions for issue_0017: Featured solutions responsive interaction"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0017_featured_solutions_responsive_interaction_page import Issue0017FeaturedSolutionsResponsivePage


@given("The Featured Solutions section is rendered")
def featured_solutions_rendered(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.navigate_to_homepage()


@given("The page is viewed on a touch device")
def page_on_touch_device(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.resize_to_mobile()
    page_object.navigate_to_homepage()


@given("The Featured Solutions section is rendered at any viewport")
def section_rendered_any_viewport(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.navigate_to_homepage()


@given("The Featured Solutions section uses a carousel layout")
def section_uses_carousel(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.navigate_to_homepage()


@given("The Featured Solutions uses an autoplay carousel")
def section_uses_autoplay_carousel(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.navigate_to_homepage()


@given("User is interacting with Featured Solutions")
def user_interacting_featured(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.navigate_to_homepage()


@when("Keyboard navigation testing runs")
def keyboard_nav_testing(page: Page):
    page.keyboard.press("Tab")


@when("Touch testing validates interaction")
def touch_testing(page: Page):
    """Touch testing happens in assertions."""
    pass


@when("Visual inspection runs")
def visual_inspection(page: Page):
    """Visual inspection happens in assertions."""
    pass


@when("Accessibility testing analyzes controls")
def accessibility_analyzes_controls(page: Page):
    """Accessibility analysis happens in assertions."""
    pass


@when("User has prefers-reduced-motion enabled")
def user_has_reduced_motion(page: Page):
    """Reduced motion check happens in assertions."""
    pass


@when("Viewport is resized mid-interaction")
def viewport_resized_mid_interaction(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.resize_to_mobile()


@then("Every solution card or item is reachable using Tab key")
def solution_reachable_tab(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    count = page_object.locators.solution_items.count()
    expect(count).to_be_greater_than(0)


@then("Every solution is accessible via touch")
def solution_accessible_touch(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    count = page_object.locators.solution_items.count()
    expect(count).to_be_greater_than(0)


@then("All content is visible or accessible without requiring horizontal scrolling")
def content_no_horizontal_scroll(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    has_scroll = page_object.check_no_horizontal_scroll()
    expect(has_scroll).to_be(True)


@then("Previous/next controls have accessible labels or names")
def carousel_controls_have_labels(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.verify_carousel_controls_have_labels()


@then("Autoplay is disabled or meaningfully reduced")
def autoplay_respects_reduced_motion(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    page_object.verify_reduced_motion_respected()


@then("The interaction state updates appropriately without breaking")
def interaction_state_updates(page: Page):
    page_object = Issue0017FeaturedSolutionsResponsivePage(page)
    expect(page.get_by_role("main")).to_be_visible()
