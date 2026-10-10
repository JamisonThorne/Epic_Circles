"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

from epic_circles.general.get_uniqueArray import get_uniqueArray
import numpy as np
from math import sqrt

def get_roundedCircle(circle):
    for i in range(0,np.shape(circle)[0]):
        for j in range(0,np.shape(circle)[1]):
            # circle[i][j] = round(circle[i][j], 3)
            if circle[i][j] == -0.0:
                circle[i][j] = 0.0
    return circle

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

def get_uniqueRadii(input_array):
    radius_values = []
    for i in range(0,len(input_array)):
        radius_values.append(input_array[i][2])
    radius_values.sort()
    radius_values = get_uniqueArray(radius_values)
    return np.array(radius_values)