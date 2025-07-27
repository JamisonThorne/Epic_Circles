import numpy as np
from geometry import find_my_tangent_circle

def test_find_my_tangent_circle():
    tang_cir = [[0.0, 0.0, 50.0], [25.0, 0.0, 25.0], [-25.0, 0.0, 25.0]]
    kiss_cir = [[0.0, 33.33, 16.67], [-0.0, -33.33, 16.67]]
    result = find_my_tangent_circle(tang_cir, kiss_cir)
    assert [0.0, 33.33, 16.67] in result