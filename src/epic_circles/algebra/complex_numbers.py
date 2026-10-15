from __future__ import annotations

from math import sqrt, atan2, cos, sin

def convert_to_complex_numbers(tangent_single):
    temp = []
    for i,j,k in tangent_single:
        temp.append([complex(i,j),k])
    return temp

def convert_to_real_numbers(circle_set):
    temp = []
    for i in range(0,len(circle_set)):
        temp.append([circle_set[i][0].real,circle_set[i][0].imag,circle_set[i][1]])
    return temp

def get_complex_add(z1,z2):
    #   Adds two complex numbers together and returns resulting complex number
    #   (a + ib) + (c + id) = (a + c) + i(b + d)
    a = z1.real
    b = z1.imag
    c = z2.real
    d = z2.imag
    return complex(a+c, b+d)

def get_complex_subtract(z1,z2):
    #   Subtracts two complex numbers and returns resulting complex number
    #   (a + ib) - (c + id) = (a - c) + i(b - d)
    a = z1.real
    b = z1.imag
    c = z2.real
    d = z2.imag
    return complex(a-c, b-d)

def get_complex_multiply(z1,z2):
    # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    a = z1.real
    b = z1.imag
    c = z2.real
    d = z2.imag
    return complex((a*c)-(b*d),(a*d)+(b*c))

def get_complex_root(z):
    a = z.real
    b = z.imag
    # Calculate distance from origin to imaginary point a+bi
    r = sqrt((a**2)+(b**2))
    root_r = sqrt(r)
    # Calculate angle theta for imaginary point a+bi
    # radians(current_angles[i]) 
    theta = atan2(b, a)
    half_theta = theta/2
    #   Calculate new real number
    return complex(root_r*cos(half_theta),root_r*sin(half_theta))

def get_real_multiply(z,k):
    a = z.real
    b = z.imag
    return complex((a*k),(b*k))
