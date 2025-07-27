import numpy as np
from geometry import convert_circle_radius_to_curvature

def test_convert_circle_radius_to_curvature():
    circles = [[0, 0, 2], [1, 1, 0.5]]
    result = convert_circle_radius_to_curvature([c.copy() for c in circles])
    assert np.allclose(result[0][2], 0.5)
    assert np.allclose(result[1][2], 2.0)