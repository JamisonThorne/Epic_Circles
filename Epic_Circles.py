import numpy as np
import matplotlib.pyplot as plt
import math 

def main():
    # Define a radius for the first circle, after that everything else is taken care of. Enjoy :)
    radius_n = 1    # radius of first circle
    origin_x = 0    # origin (center of first circle) in this case will always be at 0,0
    origin_y = 0    # origin (center of first circle) in this case will always be at 0,0
    graph_range = 1

    circle1 = plt.Circle((origin_x, origin_y), radius_n, color='r',fill=False)
    circle2 = plt.Circle((origin_x, origin_y + radius_n/2), radius_n/2, color='blue',fill=False)
    circle3 = plt.Circle((origin_x, origin_y - radius_n/2), radius_n/2, color='blue',fill=False)

    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.cla() # clear things for fresh plot

    # change default range so that new circles will work
    ax.set_xlim((-1*graph_range, graph_range))
    ax.set_ylim((-1*graph_range, graph_range))
    # change default range so that new circles will work
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    plt.show()
    [x0,y0,x1,y1] = finding_the_intersection_of_two_circles(2,3,3,1,-1,4)



def finding_the_intersection_of_two_circles(x0,y0,r0,x1,y1,r1):
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