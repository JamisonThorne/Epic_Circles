"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

def check_thrice_circleIntersection(test_circle, other_circles, tol=0.02):
    # other_circles: list of three circles, each [x, y, r]
    return all(circles_intersect_test(test_circle, c, tol) for c in other_circles)
