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

def finding_the_intersection_of_two_circles(x_1,y_1,r_1,x_2,y_2,r_2):
    #x1 and y1 are the center of the first circle with r1 being the radius
    #x2 and y2 are the center of the first circle with r2 being the radius
    # First Circle Equation:   
    x_1 = 1
    x_2 = 1
    y_1 = 1
    y_2 = 1
    r_1 = 1
    r_2 = 1 
    x = 1
    y = 1
    #remembering old math is hard
    #https://math.stackexchange.com/questions/256100/how-can-i-find-the-points-at-which-two-circles-intersect
    #https://stackoverflow.com/questions/15398427/solving-quadratic-equation
    #https://pressbooks.bccampus.ca/algebraintermediate/chapter/solve-quadratic-equations-using-the-quadratic-formula/
    ((x-x_1)**2)+((y-y_1)**2)=(r_1**2) == (x**2)-2*((x)*(x_1))+(x_1**2)+(y**2)-2*((y)*(y_1))+(y_1**2)=(r_1**2)    (eq. 1)
    # Second Circle Equation:   
    ((x-x_2)**2)+((y-y_2)**2)=(r_1**2) == (x**2)-2*((x)*(x_2))+(x_2**2)+(y**2)-2*((y)*(y_2))+(y_2**2)=(r_2**2)    (eq. 2)
    # Subtract (eq. 1) from (eq. 2) and simplify while solving for y
    # (x**2 - x**2 -2(x)(x_1) - -2(x)(x_2) +x_1**2 - x_2**2) + y**2 - y**2-2(y)(y_1)--2(y)(y_2)+y_1**2-y_2**2 = r_1**2 - r_2**2
    # -2(x)(x_1-x_2)-2(y)(y_1-y_2) = r_1**2 - r_2**2-x_1**2+x_2**2-y_1**2+y_2**2
    # -2(y)(y_1-y_2) = r_1**2-r_2**2-x_1**2+x_2**2-y_1**2+y_2**2+2(x)(x_1-x_2)
    # (y) = (r_1**2-r_2**2)/(-2(y_1-y_2))-(x_1**2+x_2**2)/(-2(y_1-y_2))-(y_1**2+y_2**2)/(-2(y_1-y_2))-(x)((x_1-x_2)/((y_1-y_2)))    (eq. 3)
    # Plug eq. 3 instead eq. 1 or eq.2 and solve for x. Plug x value(s) into eq. 3 and solve for y
    # Note: Can verify same x values by plugging into both eq. 1 and eq. 2 which will be done below before solving for y
    c=(x_1**2)+((((r_1**2-r_2**2)/(-2*(y_1-y_2)))-((x_1**2+x_2**2)/(-2*(y_1-y_2)))-((y_1**2+y_2**2)/(-2*(y_1-y_2)))-(x)*(((x_1-x_2)/((y_1-y_2))))))**2-(2*((((r_1**2-r_2**2)/(-2*(y_1-y_2)))-((x_1**2+x_2**2)/(-2*(y_1-y_2)))-((y_1**2+y_2**2)/(-2*(y_1-y_2)))-(x)*(((x_1-x_2)/((y_1-y_2))))))*(y_1))+(y_1**2)-(r_1**2)
    first_x = []
    second_x = []
    [first_x,second_x] = Solve_My_Quadratic(1,-2*x_1,c)
    1
 
# def Solve_My_Quadratic(a,b,c):
#     #   a*x**2+b*x+c=0
#     d = b**2-4*a*c # discriminant

#     if d < 0:
#         # print "This equation has no real solution"
#     elif d == 0:
#         x = (-b+math.sqrt(b**2-4*a*c))/2*a
#         # print "This equation has one solutions: ", x
#     else:
#         x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
#         x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
#         # print "This equation has two solutions: ", x1, " and", x2

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