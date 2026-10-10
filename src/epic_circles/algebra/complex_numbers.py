from __future__ import annotations

from math import sqrt, atan2, cos, sin

def convert_toComplexNumbers(tangential_circles):
    temp = []
    for i in range(0,len(tangential_circles)):
        temp.append([complex(tangential_circles[i][0],tangential_circles[i][1]),tangential_circles[i][2]])
    return temp

def convert_toRealNumbers(tangential_circles):
    temp = []
    for i in range(0,len(tangential_circles)):
        temp.append([tangential_circles[i][0].real,tangential_circles[i][0].imag,tangential_circles[i][1]])
    return temp

def get_complexAdd(complex_number1,complex_number2):
    #   Adds two complex numbers together and returns resulting complex number
    #   (a + ib) + (c + id) = (a + c) + i(b + d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a+c, b+d)

def get_complexSubtract(complex_number1,complex_number2):
    #   Subtracts two complex numbers and returns resulting complex number
    #   (a + ib) - (c + id) = (a - c) + i(b - d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a-c, b-d)

def get_complexMultiply(complex_number_1,complex_number_2):
    # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    a = complex_number_1.real
    b = complex_number_1.imag
    c = complex_number_2.real
    d = complex_number_2.imag
    return complex((a*c)-(b*d),(a*d)+(b*c))

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

def get_realMultiply(complex_number,constant_number):
    a = complex_number.real
    b = complex_number.imag
    return complex((a*constant_number),(b*constant_number))
