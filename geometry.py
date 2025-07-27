import numpy as np
from math import sqrt, isclose

def convert_circle_curvature_to_radius(tangential_circles):
    # differential geometry
    for i in range(0,len(tangential_circles)):
        if tangential_circles[i][2] != 0:
            tangential_circles[i][2] = 1/tangential_circles[i][2]
    return tangential_circles

def convert_circle_radius_to_curvature(tangential_circles):
    # differential geometry
    for i in range(0,len(tangential_circles)):
        if tangential_circles[i][2] != 0:
            tangential_circles[i][2] = 1/tangential_circles[i][2]
    return tangential_circles

def track_tangent_circles(current_circle):
    #Creates NxN zero matrix (tracker) where N is the number of circles in current_circle. 
    # Loops through each pair of circles and notes where they are tangent in the zero matrix.
    tracker = []
    tracker = np.zeros((np.shape(current_circle)[0],np.shape(current_circle)[0],np.shape(current_circle)[0]))
    for i in range(0,len(current_circle)):
        for j in range(0,len(current_circle)):
            for k in range(0,len(current_circle)):
                if i != j and i != k and j != k:  # Ensure we are not comparing the same circle
                    if are_circles_tangent(current_circle[i], current_circle[j]) and are_circles_tangent(current_circle[i], current_circle[k]) and are_circles_tangent(current_circle[j], current_circle[k]):
                        tracker[i][j][k] = 1
                    else:
                        tracker[i][j][k] = 0
    tracker = tracker * np.tri(np.shape(tracker)[0], np.shape(tracker)[1], np.shape(tracker)[2], dtype=int)
    return tracker

def are_circles_tangent(circle1, circle2):
    #determines if two circles are tangent
    # circle = [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Check for external tangency
    if isclose(center_dist, r1 + r2, rel_tol=0.01):
        return True
    # Check for internal tangency
    if isclose(center_dist, abs(r1 - r2), rel_tol=0.01):
        return True
    return False

def find_my_tangent_circle(tangential_circles,kissing_circles):
    for tangential_circle_check in kissing_circles:
        counter = 0
        for tangent_circle in tangential_circles:
            if are_circles_tangent(tangential_circle_check, tangent_circle):
                counter+=1
        if counter == 3:
            tangential_circles.append(tangential_circle_check)
    return tangential_circles

def round_my_circle(circle): 
    for i in range(0,np.shape(circle)[0]):
        for j in range(0,np.shape(circle)[1]):
            if circle[i][j] == -0.0:
                circle[i][j] = 0.0
            else:
                circle[i][j] = round(circle[i][j],2)
    return circle

def find_number_of_unique_radii(input_array):
    radius_values = []
    for i in range(0,len(input_array)):
        radius_values.append(input_array[i][2])
    radius_values.sort()
    radius_values = get_unique_array(radius_values)
    return np.array(radius_values)

def find_small_r(R, number_of_starting_circles):
    match number_of_starting_circles:
        case 2:
            return R/2
        case 3:
            return R/(1+(2/sqrt(3)))
        case 4:
            return R/(1+sqrt(2))
        case 5:
            return R/(1+sqrt(2*(1+(1/sqrt(5)))))
        
def get_unique_array(circle_array):
        unique_list = []
        for item in circle_array:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list