import numpy as np
import matplotlib.pyplot as plt
import math 
from fraction import Fraction

def main(arg_1):
    # Define a radius for the first circle, after that everything else is taken care of. Enjoy :)
    circle_information = []
    graph_range = arg_1*2
    # Figure Generation
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.cla() # clear things for fresh plot
    # change default range so that new circles will work
    ax.set_xlim((graph_range*-1, graph_range))
    ax.set_ylim((graph_range*-1, graph_range))
    #   Initial declaration of the first three circles, after this decartes will take over
    circle_information.append([complex(0,0),(1/-1*arg_1)])             #  Define first circle with curvature (1/r)
    circle_information.append([complex(0,(arg_1/2)),1/(arg_1/2)])    #  Define secondS circle with curvature (1/r)
    circle_information.append([complex(0,(arg_1/2-1)),1/(arg_1/2)])  #  Define third circle with curvature (1/r)
    ###############################################
    for i in  range(0,1):
        #   Initial circle will have a negative radius due to all circles being inside of that circle...
        [decartes_circles] = Recursive_Descartes_Theorem(circle_information,1)
        decartes_circles.append([complex_number_1.real,complex_number_1.imag,temp_r])
        decartes_circles.append([complex_number_2.real,complex_number_2.imag,temp_r])
    #https://sites.math.washington.edu//~julia/teaching/445_Spring2013/DescartesAndTheApollonianGasket%20(1).pdf
    for i in range(0,len(decartes_circles)):
        ###############################################
        # Drawing Initial Circle 
        circle = plt.Circle((decartes_circles[i][0], decartes_circles[i][1]), decartes_circles[i][2], color='r',fill=False)
        ax.add_patch(circle)
    plt.show()
    
def Recursive_Descartes_Theorem(circle_information,counter):
    counter = counter + 1
    if counter == 3:
        return circle_information
    else:
        new_circle_information = Complex_Descartes_Theorem(z1,k1,z2,k2,z3,k3,k4,circle_information,counter)


def Complex_Descartes_Theorem(circle_information,counter):
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy
    z1 = circle_information[0][0]
    z2 = circle_information[1][0]
    z3 = circle_information[2][0]
    k1 = circle_information[0][1]
    k2 = circle_information[1][1]
    k3 = circle_information[2][1]
    k4 = Descartes_Theorem(k1,k2,k3)
    #########
    #   Calculate the first portion of Descartes Complex Theorem
    z1k1 = Complex_Real_Multiply(z1,k1)  #   Multiply complex number by curvature k (1/r)
    z2k2 = Complex_Real_Multiply(z2,k2)  #   Multiply complex number by curvature k (1/r)
    z3k3 = Complex_Real_Multiply(z3,k3)  #   Multiply complex number by curvature k (1/r)
    first_value = Complex_Add(Complex_Add(z1k1,z2k2),z3k3)
    ######
    #   Calculate the second portion of Descartes Complex Theorem
    z1k1_z2k2_prod = Complex_Multiply(z1k1,z2k2)    #   Multiple two complex numbers together
    z2k2_z3k3_prod = Complex_Multiply(z2k2,z3k3)    #   Multiple two complex numbers together
    z1k1_z3k3_prod = Complex_Multiply(z1k1,z3k3)    #   Multiple two complex numbers together
    complex_number_sum = Complex_Add(Complex_Add(z1k1_z2k2_prod,z2k2_z3k3_prod),z1k1_z3k3_prod)   #   Add together above resulting multiples
    sqrt_second_value = Complex_Root(complex_number_sum)  # Calculate the root of the complex number
    z4_1 = Complex_Real_Multiply(Complex_Add(first_value,(Complex_Real_Multiply(sqrt_second_value,2))),1/k4)    #   Calculate Final Complex Number
    z4_2 = Complex_Real_Multiply(Complex_Sub(first_value,(Complex_Real_Multiply(sqrt_second_value,2))),1/k4)    #   Calculate Final Complex Number
    Recursive_Circle_Info = []
    Recursive_Circle_Info.append([z1,k1],[z2,k2],[z4_1,k4],counter)
    Recursive_Circle_Info.append([z3,k3],[z2,k2],[z4_1,k4],counter)
    Recursive_Circle_Info.append([z1,k1],[z3,k3],[z4_1,k4],counter)
    Recursive_Descartes_Theorem(Recursive_Circle_Info)
    Recursive_Circle_Info = []
    Recursive_Circle_Info.append([z1,k1],[z2,k2],[z4_1,k4],counter)
    Recursive_Circle_Info.append([z3,k3],[z2,k2],[z4_1,k4],counter)
    Recursive_Circle_Info.append([z1,k1],[z3,k3],[z4_1,k4],counter)
    Recursive_Descartes_Theorem(Recursive_Circle_Info)
    return z4_x,z4_y

def Complex_Add(complex_number1,complex_number2):
    #   Adds two complex numbers together and returns resulting complex number
    #   (a + ib) + (c + id) = (a + c) + i(b + d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a+c, b+d)

def Complex_Sub(complex_number1,complex_number2):
    #   Subtracts two complex numbers and returns resulting complex number
    #   (a + ib) - (c + id) = (a - c) + i(b - d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a-c, b-d)

def Complex_Real_Multiply(complex_number,constant_number):
    a = complex_number.real
    b = complex_number.imag
    return complex((a*constant_number),(b*constant_number))

def Complex_Multiply(complex_number_1,complex_number_2):
    # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    a = complex_number_1.real
    b = complex_number_1.imag
    c = complex_number_2.real
    d = complex_number_2.imag
    return complex((a*c)-(b*d),(a*d)+(c*b))

def Complex_Root(complex_number):
    a = complex_number.real
    b = complex_number.imag
    # Calculate distance from origin to imaginary point a+bi
    r = math.sqrt((a**2)+(b**2))
    # Calculate angle theta for imaginary point a+bi
    theta = math.atan(b/a)
    theta = theta/2
    #   Calculate new real number
    return complex(r*math.cos(theta),r*math.sin(theta))

def Descartes_Theorem(k1,k2,k3):
    #   k4 = k1+k2+k3+/-2*sqrt(k1*k2+k2*k3+k1*k3)
    #   k4 has two possible values
    k_sum = k1+k2+k3
    k_multiple = (k1*k2) + (k2*k3) + (k1*k3)
    r_a = k_sum + 2*math.sqrt(k_multiple)
    r_b = k_sum - 2*math.sqrt(k_multiple)
    return max(1/r_a,1/r_b)

def equation_of_a_line(x0,y0,x1,y1):
    a = (y1-y0)/(x1-x0)
    b = y0 - a*x0
    #   y = a*x+b
    return a, b
    
def intersection_of_two_circles(x0,y0,r0,x1,y1,r1):
    # Reference: https://mathworld.wolfram.com/Circle-CircleIntersection.html
    # x0,y0 is the center of the first  circle, with radius r0
    # x1,y1 is the center of the second circle, with radius r1
    # Say you have two circles overlapping at two points x_1,x_2,y_1,y_2, 
    # this function find the location of the two points of overlap by drawing a line
    # across each point. 
    dx = x1-x0
    dy = y1-y0
    d = math.sqrt(dx**2 + dy**2)    #   length between the center location of each circle
    dr = (r0**2)-(r1**2)            #   Pythagorus
    l = (dr+(d**2))/(2*d)           #   length from the line drawn between the two intersection points and the center of a circle 
    h = math.sqrt((r0**2)-(l**2))   #   half the length of the line drawn between the two intersection points
    # These lines of code are calculating the coordinates of the two intersection points of two circles.
    tempx = x0 + l*dx/d
    tempy = y0 + l*dy/d
    x_0 = tempx + h*dy/d
    x_1 = tempx - h*dy/d
    y_0 = tempy - h*dx/d
    y_1 = tempy + h*dx/d
    return x_0, y_0, x_1, y_1

def PointsInCircum(r,number_of_points):
    pi = math.pi
    return [(math.cos(2*pi/number_of_points*x)*r,math.sin(2*pi/number_of_points*x)*r) for x in range(0,number_of_points+1)]

if __name__ == '__main__':
    main(1)