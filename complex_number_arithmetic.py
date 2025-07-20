from math import sqrt, atan2, cos, sin

def getComplexNumberSum(complex_number1,complex_number2):
    #   Adds two complex numbers together and returns resulting complex number
    #   (a + ib) + (c + id) = (a + c) + i(b + d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a+c, b+d)

def getComplexNumberSubtraction(complex_number1,complex_number2):
    #   Subtracts two complex numbers and returns resulting complex number
    #   (a + ib) - (c + id) = (a - c) + i(b - d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a-c, b-d)

def getComplexNumberMultipliedConstant(complex_number,constant_number):
    a = complex_number.real
    b = complex_number.imag
    return complex((a*constant_number),(b*constant_number))

def getComplexNumberMultiplication(complex_number_1,complex_number_2):
    # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    a = complex_number_1.real
    b = complex_number_1.imag
    c = complex_number_2.real
    d = complex_number_2.imag
    return complex((a*c)-(b*d),(a*d)+(b*c))

def getComplexNumberSquareRoot(complex_number):
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