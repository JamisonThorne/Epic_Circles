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
    # multiply complex number against a constant and returns result
    # (a + ib) * constant = (a * constant) + (b * constant)
    a = complex_number.real
    b = complex_number.imag
    return complex((a*constant_number),(b*constant_number))

def getComplexNumberMultiplication(complex_number_1,complex_number_2):
    # multiply two complex numbers
    # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    a = complex_number_1.real
    b = complex_number_1.imag
    c = complex_number_2.real
    d = complex_number_2.imag
    return complex((a*c)-(b*d),(a*d)+(b*c))

def getComplexNumberSquareRoot(complex_number):
    # TODO technically needs to return more than one result
    # TODO see this: https://www.google.com/search?q=complex+square+root+example&rlz=1C1VDKB_enUS932US932&oq=complex+square+root+example&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyCggFEAAYogQYiQUyCggGEAAYgAQYogTSAQg0MjU0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#vhid=wl3lkSNz8Pb1SM&vssid=l
    # TODO 5. Important Note: Since trigonometric functions are periodic, 
    # there are actually two square roots for any complex number (except zero). 
    # These are found by adding 2π (or 360 degrees) to the argument before
    # dividing by two: w = √r (cos((θ + 2π)/2) + i sin((θ + 2π)/2)), which 
    # simplifies to w = √r (cos(π + θ/2) + i sin(π + θ/2)) take the square
    # root of the modulus and divide the argument by two
    # (a + ib) = (sqrt(r) * cos(arctangent(theta/2), sqrt(r) * sin(arctangent(theta/2)i)
    a = complex_number.real
    b = complex_number.imag
    r = sqrt((a**2)+(b**2)) # modulus of a complex number is the distance from the origin of the complex plane
    root_r = sqrt(r)
    theta = atan2(b, a) # Calculate angle theta for imaginary point a+bi
    half_theta = theta/2
    return complex(root_r*cos(half_theta),root_r*sin(half_theta))

def convert_real_to_complex_numbers(tangential_circles):
    temp = []
    for i in range(0,len(tangential_circles)):
        temp.append([complex(tangential_circles[i][0],tangential_circles[i][1]),tangential_circles[i][2]])
    return temp

def convert_complex_to_real_numbers(tangential_circles):
    temp = []
    for i in range(0,len(tangential_circles)):
        temp.append([tangential_circles[i][0].real,tangential_circles[i][0].imag,tangential_circles[i][1]])
    return temp