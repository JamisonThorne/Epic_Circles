import numpy as np
from geometry import find_my_tangent_circle

def test_find_my_tangent_circle():
    tangential = [[0, 0, 1], [2, 0, 1], [1, np.sqrt(3), 1]]
    kissing = [[1, 1/np.sqrt(3), 1/3], [5, 5, 1]]
    result = find_my_tangent_circle(tangential.copy(), kissing)
    assert [1, 1/np.sqrt(3), 1/3] in result