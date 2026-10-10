"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

import numpy as np

def track_tangentCircles(current_circle):
    #Creates NxN zero matrix (tracker) where N is the number of circles in current_circle. 
    # Loops through each pair of circles and notes where they are tangent in the zero matrix.
    tracker = []
    tracker = np.zeros((np.shape(current_circle)[0],np.shape(current_circle)[0],np.shape(current_circle)[0]))
    for i in range(0,len(current_circle)):
        for j in range(0,len(current_circle)):
            for k in range(0,len(current_circle)):
                if i != j and i != k and j != k:  # Ensure we are not comparing the same circle
                    if check_tangentCircles(current_circle[i], current_circle[j]) and check_tangentCircles(current_circle[i], current_circle[k]) and check_tangentCircles(current_circle[j], current_circle[k]):
                        tracker[i][j][k] = 1
                    else:
                        tracker[i][j][k] = 0
    tracker = tracker * np.tri(np.shape(tracker)[0], np.shape(tracker)[1], np.shape(tracker)[2], dtype=int)
    return tracker