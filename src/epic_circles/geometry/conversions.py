from __future__ import annotations

def get_kr_rk_conversion(tangential_circles):
    # look at the radius for the three circles and invert if not equal to 0
    for i in range(0,len(tangential_circles)):
        if tangential_circles[i][2] != 0:
            tangential_circles[i][2] = 1/tangential_circles[i][2]
    return tangential_circles