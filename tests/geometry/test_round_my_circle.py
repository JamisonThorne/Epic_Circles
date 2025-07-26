import numpy as np
from geometry import round_my_circle

def test_round_my_circle():
    arr = [[-0.0, 1.0], [2.0, -0.0]]
    rounded = round_my_circle(np.array(arr).copy())
    assert np.all(rounded == np.array([[0.0, 1.0], [2.0, 0.0]]))