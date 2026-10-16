"""Write processed data back to disk."""

from __future__ import annotations

from math import sqrt
from apollonian_gaskets.algebra.complex_numbers import get_complex_add,get_complex_subtract,get_complex_root,get_complex_multiply,get_real_multiply, convert_to_complex_numbers
from apollonian_gaskets.geometry.conversions import get_curvature_or_radius_conversion
from apollonian_gaskets.geometry.circles import get_rounded_circle, check_for_initial_circle_to_invert
from apollonian_gaskets.geometry.tangency import get_tangent_circles

def complex_descartes_theorem(current_circle):
    kissing_circle = []
    k4_curvature = []
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy    
    z1, z2, z3 = current_circle[0][0], current_circle[1][0], current_circle[2][0]
    k1, k2, k3 = current_circle[0][1], current_circle[1][1], current_circle[2][1]
    k4 = descartes_theorem(k1,k2,k3)
    r4 = 1/k4   # gather radius of the tangential circle curvature
    #   z1*k1
    z1_k1 = get_real_multiply(z1,k1)  #   Multiply complex number by curvature k (1/r)
    #   z2*k2
    z2_k2 = get_real_multiply(z2,k2)  #   Multiply complex number by curvature k (1/r)
    #   z3*k3
    z3_k3 = get_real_multiply(z3,k3)  #   Multiply complex number by curvature k (1/r)
    # first_portion = z1*k1+z2*k2+z3*k3
    first_portion = get_complex_add(get_complex_add(z1_k1,z2_k2),z3_k3)
    #   (k1*k2*z1*z2)
    z1k1_z2k2 = get_complex_multiply(z1_k1,z2_k2)
    #   (k2*k3*z2*z3)
    z2k2_z3k3 = get_complex_multiply(z2_k2,z3_k3)
    #   (k1*k3*z1*z3)
    z1k1_z3k3 = get_complex_multiply(z1_k1,z3_k3)
    #   (k1*k2*z1*z2)+(k2*k3*z2*z3)+(k1*k3*z1*z3)
    second_portion = get_complex_add(get_complex_add(z1k1_z2k2,z2k2_z3k3),z1k1_z3k3)
    #   second_portion = root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3)
    sqrt_second_portion = get_complex_root(second_portion)  # Calculate the root of the complex number
    #   first_portion + (2 * second_portion)
    z4_add = get_complex_add(first_portion,(get_real_multiply(sqrt_second_portion,2)))
    #   (first_portion + (2 * second_portion)) * r4
    z4_add = get_real_multiply(z4_add,r4)
    #   first_portion - (2 * second_portion)
    z4_subtract = get_complex_subtract(first_portion,(get_real_multiply(sqrt_second_portion,2))) 
    #   (first_portion - (2 * second_portion)) * r4
    z4_subtract = get_real_multiply(z4_subtract,r4)
    #   return the four kissing circles found
    kissing_circle.append([z4_add.real,z4_add.imag,r4]) #   x, y, radius
    kissing_circle.append([z4_subtract.real,z4_subtract.imag,r4]) #   x, y, radius
    return kissing_circle

def descartes_theorem(k1,k2,k3):
    #   k4 = k1+k2+k3+/-2*sqrt(k1*k2+k2*k3+k1*k3)
    #   k4 has two possible values
    k_sum = k1+k2+k3
    k_multiple = max((k1*k2) + (k2*k3) + (k1*k3),0)
    # print(k_multiple)
    k4 = k_sum + 2*sqrt(k_multiple)
    # k4_b = k_sum - 2*sqrt(k_multiple)
    return k4

def find_descartes_circles(tangent_set,R):
    inverted_tangent_set = check_for_initial_circle_to_invert(tangent_set, R)
    curvature_tangent_set = get_curvature_or_radius_conversion(inverted_tangent_set)
    complex_tangent_set = convert_to_complex_numbers(curvature_tangent_set)
    kissing_circles = complex_descartes_theorem(complex_tangent_set)
    kissing_circles = get_rounded_circle(kissing_circles)
    kissing_circles = get_tangent_circles(tangent_set,kissing_circles)
    return kissing_circles