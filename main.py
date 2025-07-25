from math import cos, sin, radians
# from plots import plot_myCircles
from geometry import track_tangent_circles, find_small_r
from decartes_theorems import find_descartes_circles
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

def main():
    R = 50  # Outer circle needs to be large enough to display smaller circles generated
    number_of_starting_inner_circles = 2    # acceptable values; 2,3,4,5
    graph_bounds = R + R/2  # just to provide a nice buffer around the outer circle
    cir_res = []
    fig, ax = plt.subplots(2,2)
    axes = ax.flat
    for i in range(0,4):
        tracker = []
        if i==0:
            current_circle = initialize_setup(number_of_starting_inner_circles, R)
            # plot_myCircles(current_circle, graph_bounds, i)
            tracker = track_tangent_circles(current_circle)
            cir_res = find_descartes_circles(current_circle,tracker,R)
            # plot_myCircles(cir_res, graph_bounds, i)
            # ax.cla() # clear things for fresh plot
            # change default range so that new circles will work
            axes[i].set_xlim((-1*graph_bounds, graph_bounds))
            axes[i].set_ylim((-1*graph_bounds,  graph_bounds))
            for circle_idx in range(0,len(cir_res)):
                # color = colors[int(np.where(unique_radii == cir_res[i][2])[0])]
                # circle = ax[i].Circle((cir_res[i][0], cir_res[i][1]), -1*cir_res[i][2], color=color,fill=False)
                circle = Circle((cir_res[circle_idx][0], cir_res[circle_idx][1]), -1*cir_res[circle_idx][2],fill=False)
                axes[i].add_patch(circle)
        else:
            tracker = track_tangent_circles(cir_res)
            cir_res.extend(find_descartes_circles(cir_res,tracker,R))
            # plot_myCircles(cir_res, graph_bounds, i)6
            # ax[i].cla() # clear things for fresh plot
            # change default range so that new circles will work
            axes[i].set_xlim((-1*graph_bounds, graph_bounds))
            axes[i].set_ylim((-1*graph_bounds,  graph_bounds))
            for circle_idx in range(0,len(cir_res)):
                # color = colors[int(np.where(unique_radii == current_circle[i][2])[0])]
                # circle = ax[i].Circle((current_circle[i][0], current_circle[i][1]), -1*current_circle[i][2], color=color,fill=False)
                circle = plt.Circle((cir_res[circle_idx][0], cir_res[circle_idx][1]), -1*cir_res[circle_idx][2],fill=False)
                axes[i].add_patch(circle)
    plt.show()
            
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