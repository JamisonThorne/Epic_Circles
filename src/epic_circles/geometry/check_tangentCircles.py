"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

from math import sqrt, isclose

def check_tangentCircles(circle1, circle2):
    #determines if two circles are tangent
    # circle = [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Check for external tangency
    if isclose(center_dist, r1 + r2):
        return True
    # Check for internal tangency
    if isclose(center_dist, abs(r1 - r2)):
        return True
    return False