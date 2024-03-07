import numpy as np
import matplotlib.pyplot as plt
import math 

def main():
    graph_range = 1

    circle1 = plt.Circle((0, 0.5), 0.5, color='r',fill=False)
    circle2 = plt.Circle((0, 0), 1, color='blue',fill=False)
    circle2 = plt.Circle((0, 0), 0.5, color='blue',fill=False)
    circle3 = plt.Circle((0, -0.5), 0.5, color='g',fill=False)

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
    result = finding_the_intersection_of_two_circles(2,3,3,1,1,4)
    1

def finding_the_intersection_of_two_circles(x1,y1,r1,x2,y2,r2):
    # x1,y1 is the center of the first  circle, with radius r1
    # x2,y2 is the center of the second circle, with radius r2
    
    #remembering old math is hard
    #https://math.stackexchange.com/questions/256100/how-can-i-find-the-points-at-which-two-circles-intersect
    #https://stackoverflow.com/questions/15398427/solving-quadratic-equation
    #https://pressbooks.bccampus.ca/algebraintermediate/chapter/solve-quadratic-equations-using-the-quadratic-formula/
    r1r2_numerator_add = (r1**2)+(r2**2)
    r1r2_numerator_sub = (r1**2)-(r2**2)
    R = math.sqrt((x2-x1)**2+(y2-y1)**2)
    a = r1r2_numerator_sub/(2*R)
    c = math.sqrt((2*(r1r2_numerator_add/(R**2)))-((r1r2_numerator_sub**2)/(R**4))-1)
    fx = ((x1+x2)/2)+a*(x2-x1)
    gx = (c/2)
    fy = ((y1+y2)/2)+a*(y2-y1)
    fg = 
    
    
def Solve_My_Quadratic(a,b,c):
    #   Quadratic equation reminder:    a*x**2+b*x+c=0
    d = b**2-4*a*c # discriminant, I don't remember this at all from maths
    if d < 0:
        raise Exception("No real solution")
    elif d == 0:
        value_1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        raise Exception("This equation has 1 solution")
    else:
        value_1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        value_2 = (-b-math.sqrt(b**2-4*a*c))/2*a

def PointsInCircum(r,number_of_points):
    pi = math.pi
    return [(math.cos(2*pi/number_of_points*x)*r,math.sin(2*pi/number_of_points*x)*r) for x in range(0,number_of_points+1)]

if __name__ == '__main__':
    main()  


# circle1 = plt.Circle((0, 0), 2, color='r')
# # now make a circle with no fill, which is good for hi-lighting key results
# circle2 = plt.Circle((5, 5), 0.5, color='b', fill=False)
# circle3 = plt.Circle((10, 10), 2, color='g', clip_on=False)
    
# ax = plt.gca()
# ax.cla() # clear things for fresh plot

# # change default range so that new circles will work
# ax.set_xlim((0, 10))
# ax.set_ylim((0, 10))
# # some data

# # key data point that we are encircling
# ax.plot((5), (5), 'o', color='y')
    
# ax.add_patch(circle1)
# ax.add_patch(circle2)
# ax.add_patch(circle3)
# fig.savefig('plotcircles2.png')