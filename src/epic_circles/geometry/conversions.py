from __future__ import annotations

def get_curvature_or_radius_conversion(circle_set):
    # look at the radius for the three circles and invert if not equal to 0
    new_set = []
    for circle_group in circle_set:
        inverted_group = []
        for i, x in enumerate(circle_group):
            if (i == 2 and x != 0):
                inverted_group.append(1/x)
            else:
                inverted_group.append(x)
        new_set.append(inverted_group)
    return new_set