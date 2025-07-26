import numpy as np
from geometry import find_small_r

def test_find_small_r():
    R = 10
    assert np.isclose(find_small_r(R, 2), 5)
    assert np.isclose(find_small_r(R, 3), R/(1+2/np.sqrt(3)))
    assert np.isclose(find_small_r(R, 4), R/(1+np.sqrt(2)))
    assert np.isclose(find_small_r(R, 5), R/(1+np.sqrt(2*(1+1/np.sqrt(5)))))
