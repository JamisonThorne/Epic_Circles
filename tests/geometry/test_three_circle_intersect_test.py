import numpy as np
from geometry import three_circle_intersect_test

def test_three_circle_intersect_test():
    c1 = [0, 0, 1]
    c2 = [2, 0, 1]
    c3 = [1, np.sqrt(3), 1]
    test_c = [1, 1/np.sqrt(3), 1/3]
    assert not three_circle_intersect_test(test_c, [c1, c2, c3], tol=0.1)  # Should be False for these values
