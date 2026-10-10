"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

from math import sqrt, isclose

def get_krConversion(tangential_circles):
    for i in range(0,len(tangential_circles)):
        if tangential_circles[i][2] != 0:
            tangential_circles[i][2] = 1/tangential_circles[i][2]
    return tangential_circles