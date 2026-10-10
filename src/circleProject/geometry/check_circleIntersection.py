"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

from math import sqrt, isclose

def check_circleIntersection(circle1, circle2, tol):
    # circle = [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Circles intersect if their centers are closer than the sum of radii
    # and farther apart than the absolute difference of radii
    # return abs(r1 -  r2) < center_dist < (r1 + r2) 
    return isclose(center_dist, r1 + r2, abs_tol=tol) or isclose(center_dist, abs(r1 - r2), abs_tol=tol)