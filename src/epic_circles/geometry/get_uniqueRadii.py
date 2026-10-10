"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

def find_number_of_unique_radii(input_array):
    radius_values = []
    for i in range(0,len(input_array)):
        radius_values.append(input_array[i][2])
    radius_values.sort()
    radius_values = get_unique_array(radius_values)
    return np.array(radius_values)