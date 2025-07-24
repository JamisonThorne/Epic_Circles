from math import cos, sin, radians
from plots import plot_myCircles
from geometry import track_tangent_circles, find_small_r
from decartes_theorems import find_descartes_circles

def main():
    R = 50
    number_of_starting_inner_circles = 2
    graph_bounds = R + R/2
    cir_res = []
    for i in range(0,5):
        tracker = []
        if i==0:
            current_circle = initialize_setup(number_of_starting_inner_circles, R)
            plot_myCircles(current_circle, graph_bounds)
            # print("np.shape(current_circle)",np.shape(current_circle))
            tracker = track_tangent_circles(current_circle)
            cir_res = find_descartes_circles(current_circle,tracker,R)
            # print("tracker",tracker.sum())
            # print("cir_res",cir_res)
            plot_myCircles(cir_res, graph_bounds)
        else:
            # print("np.shape(current_circle)",np.shape(cir_res))
            tracker = track_tangent_circles(cir_res)
            cir_res.extend(find_descartes_circles(cir_res,tracker,R))
            # print("tracker",tracker.sum())
            # print("cir_res",cir_res)
            plot_myCircles(cir_res, graph_bounds)

    # R = 50
    # number_of_starting_inner_circles = 3
    # graph_bounds = R + R/2
    # cir_res = []
    # for i in range(0,5):
    #     tracker = []
    #     if i==0:
    #         current_circle = initialize_setup(number_of_starting_inner_circles, R)
    #         plot_myCircles(current_circle, graph_bounds)
    #         # print("np.shape(current_circle)",np.shape(current_circle))
    #         tracker = track_tangent_circles(current_circle)
    #         cir_res = find_descartes_circles(current_circle,tracker,R)
    #         # print("tracker",tracker.sum())
    #         # print("cir_res",cir_res)
    #         plot_myCircles(cir_res, graph_bounds)
    #     else:
    #         # print("np.shape(current_circle)",np.shape(cir_res))
    #         tracker = track_tangent_circles(cir_res)
    #         cir_res.extend(find_descartes_circles(cir_res,tracker,R))
    #         # print("tracker",tracker.sum())
    #         # print("cir_res",cir_res)
    #         plot_myCircles(cir_res, graph_bounds)

    # R = 50
    # number_of_starting_inner_circles = 4
    # graph_bounds = R + R/2
    # cir_res = []
    # for i in range(0,5):
    #     tracker = []
    #     if i==0:
    #         current_circle = initialize_setup(number_of_starting_inner_circles, R)
    #         plot_myCircles(current_circle, graph_bounds)
    #         # print("np.shape(current_circle)",np.shape(current_circle))
    #         tracker = track_tangent_circles(current_circle)
    #         cir_res = find_descartes_circles(current_circle,tracker,R)
    #         # print("tracker",tracker.sum())
    #         # print("cir_res",cir_res)
    #         plot_myCircles(cir_res, graph_bounds)
    #     else:
    #         # print("np.shape(current_circle)",np.shape(cir_res))
    #         tracker = track_tangent_circles(cir_res)
    #         cir_res.extend(find_descartes_circles(cir_res,tracker,R))
    #         # print("tracker",tracker.sum())
    #         # print("cir_res",cir_res)
    #         plot_myCircles(cir_res, graph_bounds)

    # R = 50
    # number_of_starting_inner_circles = 5
    # graph_bounds = R + R/2
    # cir_res = []
    # for i in range(0,5):
    #     tracker = []
    #     if i==0:
    #         current_circle = initialize_setup(number_of_starting_inner_circles, R)
    #         plot_myCircles(current_circle, graph_bounds)
    #         # print("np.shape(current_circle)",np.shape(current_circle))
    #         tracker = track_tangent_circles(current_circle)
    #         cir_res = find_descartes_circles(current_circle,tracker,R)
    #         # print("tracker",tracker.sum())
    #         # print("cir_res",cir_res)
    #         plot_myCircles(cir_res, graph_bounds)
    #     else:
    #         # print("np.shape(current_circle)",np.shape(cir_res))
    #         tracker = track_tangent_circles(cir_res)
    #         cir_res.extend(find_descartes_circles(cir_res,tracker,R))
    #         # print("tracker",tracker.sum())
    #         # print("cir_res",cir_res)
    #         plot_myCircles(cir_res, graph_bounds)
            
def initialize_setup(number_of_starting_circles,R):
    r = find_small_r(R, number_of_starting_circles)
    current_circle = []
    current_angles = list(range(0,360,int(360/number_of_starting_circles)))
    for i in range(0,len(current_angles)):
        current_angles[i] = radians(current_angles[i]) 
    current_circle.append([0,0,R]) #   center, radius
    for placement_angles in current_angles:
        current_circle.append([(R-r)*cos(placement_angles),(R-r)*sin(placement_angles),r])    #  Define Circles
    return current_circle

if __name__ == "__main__":
    main()