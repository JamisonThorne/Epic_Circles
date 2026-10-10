"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

def get_tangentCircles(tangential_circles,kissing_circles):
    result = []
    for i in range(0,len(kissing_circles)):
        # print("before kissing_circles",kissing_circles)
        # print("tangential_circles",tangential_circles)
        if three_circle_intersect_test(kissing_circles[i],tangential_circles):
            result.append(kissing_circles[i])
    tangential_circles.extend(result)
    return tangential_circles