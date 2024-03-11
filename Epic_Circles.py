import numpy as np
import matplotlib.pyplot as plt
import math 
from fraction import Fraction

def main():
    # Define a radius for the first circle, after that everything else is taken care of. Enjoy :)
    decartes_circles = []
    radius_n = 1    # radius of first circle
    origin_x = 0    # origin (center of first circle) in this case will always be at 0,0
    origin_y = 0    # origin (center of first circle) in this case will always be at 0,0
    ###############################################
    graph_range = 1
    # Figure
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.cla() # clear things for fresh plot
    # change default range so that new circles will work
    ax.set_xlim((-1*graph_range, graph_range))
    ax.set_ylim((-1*graph_range, graph_range))
    ###############################################
    # Drawing Initial Circle
    circle = plt.Circle((origin_x, origin_y), radius_n, color='r',fill=False)
    ax.add_patch(circle)
    #################################
    #   First Circle
    next_circle_x = origin_x
    next_circle_y = origin_y + radius_n/2
    circle = plt.Circle((next_circle_x, next_circle_y), radius_n/2, color='blue',fill=False)
    ax.add_patch(circle)
    #################################
    #   Second Circle
    next_circle_x = origin_x
    next_circle_y = origin_y - radius_n/2
    circle = plt.Circle((next_circle_x, next_circle_y), radius_n/2, color='blue',fill=False)
    ax.add_patch(circle)
    #################################
    #   Descartes
    decartes_circles.append(Descartes_Theorem(0.5,0.5,-1))
    #################################
    #   Third Circle
    next_circle_x = 1-decartes_circles[0]
    third_circle_radius = decartes_circles[0]
    next_circle_y = 0
    circle = plt.Circle((next_circle_x, next_circle_y), decartes_circles[0], color='blue',fill=False)
    ax.add_patch(circle)
    #################################
    #   Fourth Circle 
    next_circle_x = decartes_circles[0]-1
    next_circle_y = 0
    circle = plt.Circle((next_circle_x, next_circle_y), decartes_circles[0], color='blue',fill=False)
    ax.add_patch(circle)
    #################################
    #   Descartes
    decartes_circles.append(Descartes_Theorem(decartes_circles[0],0.5,0.5))
    #################################
    #   Kissing Circle 
    next_circle_x = -1*radius_n + third_circle_radius + third_circle_radius + decartes_circles[1]
    next_circle_y = 0
    circle = plt.Circle((next_circle_x, next_circle_y), decartes_circles[1], color='blue',fill=True)
    ax.add_patch(circle)
    #################################
    #   Kissing Circle 
    next_circle_x = 1*radius_n - third_circle_radius - third_circle_radius - decartes_circles[1]
    next_circle_y = 0
    circle = plt.Circle((next_circle_x, next_circle_y), decartes_circles[1], color='blue',fill=True)
    ax.add_patch(circle)
    #################################
    #   At this point, the next circles to be found need to be automated or this could get painful.
    #   Probably after automation of next steps, the beginning can be automated
    #################################
    #   Descartes
    decartes_circles.append(Descartes_Theorem(decartes_circles[0],0.5,-1))
    1
    # [x0,y0,x1,y1] = intersection_of_two_circles(next_circle_x,next_circle_y,radius_n/2,origin_x,origin_y,radius_n/2)
    # [a1, b1] = equation_of_a_line(next_circle_x,next_circle_y,x0,y0) # Find the equation of a line going from point of intersection to center
    # plt.axline((next_circle_x, next_circle_y), (x0, y0))
    # plt.axline((next_circle_x, next_circle_y), (x1, y1))
    # plt.plot(next_circle_x, next_circle_y, x0, y0, marker = 'o')
    # plt.plot(next_circle_x, next_circle_y, x1, y1, marker = 'o')
    
    # next_circle_x = origin_x - 0.5
    # next_circle_y = origin_y
    # # circle = plt.Circle((next_circle_x, next_circle_y), radius_n/2, color='blue',fill=False)
    # # ax.add_patch(circle)
    # plt.plot(-(b0/a0), 0, x1,0, marker = 'o')
    # plt.plot(-1-x1, 0, marker = 'o')
    # plt.plot((-(b0/a0))-x1/2, 0, marker = '^')
    # temp = (-(b0/a0))-x1/2
    # test1 = -1-temp
    # dx = x1 - temp
    # dy = y1
    # test2 = d = math.sqrt(dx**2 + dy**2)
    # 1
    
    
    # plt.show()
    # [a0, b0] = equation_of_a_line(next_circle_x,next_circle_y,x0,y0) # Find the equation of a line going from point of intersection to center
    # equation_of_a_line(next_circle_x,next_circle_y,x1,y1) # Find the equation of a line going from point of intersection to center
    # 1

def Complex_Descartes_Theorem(r1,r2,r3):
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   Where k is radius or circles
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy
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
    main()