from math import sqrt, isclose
from descartes_theorems import descartes_theorem
    
def test_descartes_theorem():
    # Example: three circles of radius 1 (curvature 1)
    k1 = k2 = k3 = 1
    k4a, k4b = descartes_theorem(k1, k2, k3)
    # k4 = 1+1+1 ± 2*sqrt(1*1 + 1*1 + 1*1) = 3 ± 2*sqrt(3)
    assert isclose(k4a, 3 + 2*sqrt(3))
    assert isclose(k4b, 3 - 2*sqrt(3))