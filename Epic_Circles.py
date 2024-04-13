import numpy as np
import matplotlib.pyplot as plt
import math 
from fraction import Fraction

def main(arg_1):
    # Define a radius for the first circle, after that everything else is taken care of. Enjoy :)
    decartes_circles = []
    graph_range = arg_1
    # Figure Generation
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.cla() # clear things for fresh plot
    # change default range so that new circles will work
    ax.set_xlim((-1*graph_range, graph_range))
    ax.set_ylim((-1*graph_range, graph_range))
    #   Initial declaration of the first three circles, after this decartes will take over
    decartes_circles.append([0,0,arg_1]) #  Define first circle
    decartes_circles.append([0,arg_1/2,arg_1/2]) #  Define first circle
    decartes_circles.append([0,arg_1/2-1,arg_1/2]) #  Define first circle
    ###############################################
    for i in range(0,2):
        if i==0:
            temp_r = Descartes_Theorem(-1*decartes_circles[i][2],decartes_circles[i+1][2],decartes_circles[i+2][2])
            [temp_x,temp_y] = Complex_Descartes_Theorem(
                decartes_circles[i][0],decartes_circles[i][1],-1*decartes_circles[i][2],
                decartes_circles[i+1][0],decartes_circles[i+1][1],decartes_circles[i+1][2],
                decartes_circles[i+2][0],decartes_circles[i+2][1],decartes_circles[i+2][2],
                temp_r)
            if abs(temp_x) == abs(temp_y):
                temp_y = 0
            decartes_circles.append([temp_x,temp_y,temp_r])
        else:
            temp_r = Descartes_Theorem(decartes_circles[i][2],decartes_circles[i+1][2],decartes_circles[i+2][2])
            [temp_x,temp_y] = Complex_Descartes_Theorem(
                decartes_circles[i][0],decartes_circles[i][1],decartes_circles[i][2],
                decartes_circles[i+1][0],decartes_circles[i+1][1],decartes_circles[i+1][2],
                decartes_circles[i+2][0],decartes_circles[i+2][1],decartes_circles[i+2][2],
                temp_r)
            if abs(temp_x) == abs(temp_y):
                temp_y = 0
            decartes_circles.append([temp_x,temp_y,temp_r])
            
    for i in range(0,len(decartes_circles)):
        ###############################################
        # Drawing Initial Circle
        circle = plt.Circle((decartes_circles[i][0], decartes_circles[i][1]), decartes_circles[i][2], color='r',fill=False)
        ax.add_patch(circle)
    plt.show()
    1
    

def Complex_Descartes_Theorem(x1,y1,r1,x2,y2,r2,x3,y3,r3,r4):
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   Where k is radius or circles
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy
    k1 = 1/r1
    k2 = 1/r2
    k3 = 1/r3
    k4 = 1/r4
    z1 = complex(x1,y1)
    z2 = complex(x2,y2)
    z3 = complex(x3,y3)
    first_value = z1*k1 + z2*k2 + z3*k3
    second_value = k1*k2*z1*z2 + k2*k3*z2*z3 + k1*k3*z1*z3
    z4_x = (abs(first_value) - (2*math.sqrt(abs(second_value))))/k4
    z4_y = (abs(first_value) + (2*math.sqrt(abs(second_value))))/k4
    return z4_x,z4_y
    
def Descartes_Theorem(r1,r2,r3):
    k1 = 1/r1
    k2 = 1/r2
    k3 = 1/r3
    k_sum = k1+k2+k3
    k_multiple = k1*k2 + k2*k3 + k1*k3
    k4_solution1 = k_sum + 2*math.sqrt(k_multiple)
    k4_solution2 = k_sum - 2*math.sqrt(k_multiple)
    result = max(k4_solution1,k4_solution2)
    return 1/result

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