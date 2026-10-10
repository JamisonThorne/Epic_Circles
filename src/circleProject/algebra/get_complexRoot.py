"""get_complexRoot returns the root of a complex number"""

from __future__ import annotations

from math import sqrt, atan2, cos, sin

def get_complexRoot(complex_number):
    a = complex_number.real
    b = complex_number.imag
    # Calculate distance from origin to imaginary point a+bi
    r = sqrt((a**2)+(b**2))
    root_r = sqrt(r)
    # Calculate angle theta for imaginary point a+bi
    # radians(current_angles[i]) 
    theta = atan2(b, a)
    half_theta = theta/2
    #   Calculate new real number
    return complex(root_r*cos(half_theta),root_r*sin(half_theta))
