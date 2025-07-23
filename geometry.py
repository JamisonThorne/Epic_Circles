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

def are_circles_tangent(circle1, circle2):
    #determines if two circles are tangent
    # circle = [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Check for external tangency
    if isclose(center_dist, r1 + r2):
        return True
    # Check for internal tangency
    if isclose(center_dist, abs(r1 - r2)):
        return True
    return False

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

def circles_intersect_test(circle1, circle2, tol):
    # circle = [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    center_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Circles intersect if their centers are closer than the sum of radii
    # and farther apart than the absolute difference of radii
    # return abs(r1 -  r2) < center_dist < (r1 + r2) 
    return isclose(center_dist, r1 + r2, abs_tol=tol) or isclose(center_dist, abs(r1 - r2), abs_tol=tol)
    
def three_circle_intersect_test(test_circle, other_circles, tol=0.02):
    # other_circles: list of three circles, each [x, y, r]
    return all(circles_intersect_test(test_circle, c, tol) for c in other_circles)

def find_my_tangent_circle(tangential_circles,kissing_circles):
    result = []
    for i in range(0,len(kissing_circles)):
        # print("before kissing_circles",kissing_circles)
        # print("tangential_circles",tangential_circles)
        if three_circle_intersect_test(kissing_circles[i],tangential_circles):
            result.append(kissing_circles[i])
    tangential_circles.extend(result)
    return tangential_circles

def round_my_circle(circle):
    for i in range(0,np.shape(circle)[0]):
        for j in range(0,np.shape(circle)[1]):
            if circle[i][j] == -0.0:
                circle[i][j] = 0.0
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