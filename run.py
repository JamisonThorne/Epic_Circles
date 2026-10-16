"""Generates an appolonian gasket with only the starting circle and number of inner circles as input. Calculations based on descartes complex theorem for finding kissing circles"""

from apollonian_gaskets.geometry.tangency import is_circles_tangent
from apollonian_gaskets.geometry.circles import initialize_setup
from apollonian_gaskets.plots.plot_circles import plot_circles
from apollonian_gaskets.theorems.descartes import find_descartes_circles
from apollonian_gaskets.utils.logging import get_logger

log = get_logger(__name__)

def main():
    R = 1000 # select any given starting radius 
    number_of_starting_inner_circles = 5 # selecting desired number of inner circles

    graph_bounds = R + R/64
    # create a circle_tracker that contains all circles that need to be drawn
    circle_tracker = initialize_setup(number_of_starting_inner_circles, R)
    # note, ranges above 6 will take longer than 10 seconds
    for i in range(6):
        # plot_circles(circle_tracker, graph_bounds)
        unique_tangent_sets = []
        n = len(circle_tracker)
        log.info(f"Searching for new tangent circles")
        for a in range(n):
            for b in range(a + 1, n):
                if not is_circles_tangent(circle_tracker[a], circle_tracker[b]):
                    continue
                for c in range(b + 1, n):
                    if not is_circles_tangent(circle_tracker[a], circle_tracker[c]):
                        continue
                    if not is_circles_tangent(circle_tracker[b], circle_tracker[c]):
                        continue
                    if ((circle_tracker[a], circle_tracker[b], circle_tracker[c]) not in unique_tangent_sets):
                        unique_tangent_sets.append((circle_tracker[a], circle_tracker[b], circle_tracker[c]))
        log.info("Tangent circles found, adding new circles")
        for tangent_set in unique_tangent_sets:
            circle_tracker.extend(find_descartes_circles(tangent_set,R))
                    
    log.info("Generating plots")
    plot_circles(circle_tracker,graph_bounds)

if __name__ == "__main__":
    main()