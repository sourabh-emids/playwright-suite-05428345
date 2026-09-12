"""Test for issue_0053 - Performance and Core Web Vitals optimization."""
import pytest

from pages.issue_0053_performance_optimization_page import Issue0053PerformanceOptimizationPage


@pytest.fixture
def performance_optimization_page(page) -> Issue0053PerformanceOptimizationPage:
    """Create page object for issue_0053 tests."""
    return Issue0053PerformanceOptimizationPage(page)
