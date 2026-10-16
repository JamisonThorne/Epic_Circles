"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

from apollonian_gaskets.general.get_unique_array import get_unique_array
import numpy as np
from math import sqrt
from math import radians, cos, sin

# def get_rounded_circle(input_set):
#     for i in range(0,np.shape(input_set)[0]):
#         for j in range(0,np.shape(input_set)[1]):
#             # input_set[i][j] = round(input_set[i][j], 3)
#             if input_set[i][j] == -0.0:
#                 input_set[i][j] = 0.0
#     return input_set

def get_smallest_radius(R, number_of_starting_circles):
    match number_of_starting_circles:
        case 2:
            return R/2
        case 3:
            return R/(1+(2/sqrt(3)))
        case 4:
            return R/(1+sqrt(2))
        case 5:
            return R/(1+sqrt(2*(1+(1/sqrt(5)))))

def get_unique_radii(input_array):
    radius_values = []
    for i in range(0,len(input_array)):
        radius_values.append(input_array[i][2])
    radius_values.sort()
    radius_values = get_unique_array(radius_values)
    return np.array(radius_values)

def check_for_initial_circle_to_invert(circle_set, R):
    flipped_set = []
    for circle_group in circle_set:
        flipped_group = []
        for x in circle_group:
            if x == R or x == -R:
                flipped_group.append(-x)
            else:
                flipped_group.append(x)
        flipped_set.append(flipped_group)
    return flipped_set

def get_rounded_circle(circle_set):
    flipped_set = []
    for circle_group in circle_set:
        flipped_group = []
        for x in circle_group:
            if x == -0.0:
                flipped_group.append(0.0)
            else:
                flipped_group.append(x)
        flipped_set.append(flipped_group)
    return flipped_set

def initialize_setup(number_of_starting_circles,R):
    r = get_smallest_radius(R, number_of_starting_circles)
    current_circle = []
    current_angles = list(range(0,360,int(360/number_of_starting_circles)))
    for i in range(0,len(current_angles)):
        current_angles[i] = radians(current_angles[i]) 

    current_circle.append([0,0,R]) #   center, radius

    for placement_angles in current_angles:
        current_circle.append([(R-r)*cos(placement_angles),(R-r)*sin(placement_angles),r])    #  Define Circles

    return current_circle