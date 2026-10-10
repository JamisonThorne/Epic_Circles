"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

from math import sqrt

def get_smallestRadius(R, number_of_starting_circles):
    match number_of_starting_circles:
        case 2:
            return R/2
        case 3:
            return R/(1+(2/sqrt(3)))
        case 4:
            return R/(1+sqrt(2))
        case 5:
            return R/(1+sqrt(2*(1+(1/sqrt(5)))))