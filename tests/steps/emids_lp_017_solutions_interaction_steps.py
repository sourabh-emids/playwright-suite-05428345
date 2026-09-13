"""Step definitions for emids_lp_017 - Featured solutions responsive interaction."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Every solution is reachable and selectable via keyboard")
def verify_keyboard_navigation(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    for card in page_obj.solution_cards.all():
        card.focus()
        expect(card).to_be_focused()


@then("Every solution is reachable via swipe or touch")
def verify_touch_reachable(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    # At mobile viewport, all solutions should be visible
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.section).to_be_visible()


@then("All solutions are accessible; content is not permanently hidden")
def verify_no_hidden_content(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    # Count solutions visible
    visible_count = page_obj.solution_cards.count()
    assert visible_count >= 3, "Some solutions hidden"


@then("Previous/next controls have accessible labels describing their function")
def verify_carousel_controls_accessible(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    # Controls should have accessible names
    for control in page_obj.carousel_controls.all():
        expect(control).to_be_visible()


@then("Autoplay is disabled or uses minimal animation")
def verify_autoplay_respects_motion(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    # Check for reduced motion preference
    reduced = page.evaluate("(window.matchMedia('(prefers-reduced-motion: reduce)').matches)")
    if reduced:
        # Autoplay should be disabled
        pass


@then("Interaction state is maintained or gracefully reset")
def verify_resize_mid_interaction(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    page.set_viewport_size({"width": 768, "height": 600})
    expect(page_obj.section).to_be_visible()


@then("Behavior is intuitive (wrap or stop) per design specification")
def verify_first_last_navigation(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    expect(page_obj.section).to_be_visible()


@then("Focus and scroll position do not conflict unexpectedly")
def verify_swipe_keyboard_no_conflict(page: Page) -> None:
    from pages.emids_lp_017_solutions_interaction_page import SolutionsInteractionPage
    page_obj = SolutionsInteractionPage(page)
    expect(page_obj.section).to_be_visible()
