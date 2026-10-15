from __future__ import annotations

from math import sqrt, isclose
import numpy as np

def track_tangent_circles(current_circle):
    #Creates NxN zero matrix (tracker) where N is the number of circles in current_circle. 
    # Loops through each pair of circles and notes where they are tangent in the zero matrix.
    tracker = []
    tracker = np.zeros((np.shape(current_circle)[0],np.shape(current_circle)[0],np.shape(current_circle)[0]))
    for i in range(0,len(current_circle)):
        for j in range(0,len(current_circle)):
            for k in range(0,len(current_circle)):
                if i != j and i != k and j != k:  # Ensure we are not comparing the same circle
                    if check_tangent_circles(current_circle[i], current_circle[j]) and check_tangent_circles(current_circle[i], current_circle[k]) and check_tangent_circles(current_circle[j], current_circle[k]):
                        tracker[i][j][k] = 1
                    else:
                        tracker[i][j][k] = 0
    tracker = tracker * np.tri(np.shape(tracker)[0], np.shape(tracker)[1], np.shape(tracker)[2], dtype=int)
    return tracker

def get_tangent_circles(tangential_circles,kissing_circles):
    result = []
    for i in range(0,len(kissing_circles)):
        # print("before kissing_circles",kissing_circles)
        # print("tangential_circles",tangential_circles)
        if check_thrice_circle_intersection(kissing_circles[i],tangential_circles):
            result.append(kissing_circles[i])
    # tangential_circles.extend(result)
    return result

def is_circles_tangent(ca, cb):
    #determines if two circles are tangent
    # circle = [x, y, r]
    x1, y1, r1 = ca
    x2, y2, r2 = cb
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Check for external tangency
    if isclose(center_dist, r1 + r2):
        return True
    # Check for internal tangency
    if isclose(center_dist, abs(r1 - r2)):
        return True
    return False

def check_tangent_circles(circle1, circle2):
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

def check_thrice_circle_intersection(test_circle, other_circles, tol=0.02):
    # other_circles: list of three circles, each [x, y, r]
    return all(check_circle_intersection(test_circle, c, tol) for c in other_circles)

def check_circle_intersection(circle1, circle2, tol):
    # circle = [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Circles intersect if their centers are closer than the sum of radii
    # and farther apart than the absolute difference of radii
    # return abs(r1 -  r2) < center_dist < (r1 + r2) 
    return isclose(center_dist, r1 + r2, abs_tol=tol) or isclose(center_dist, abs(r1 - r2), abs_tol=tol)