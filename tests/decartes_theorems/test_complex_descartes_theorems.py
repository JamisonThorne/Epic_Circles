from descartes_theorems import complex_descartes_theorem
from math import sqrt

def test_complex_descartes_theorem():
    # Three mutually tangent circles with centers at (0,0), (2,0), (1,sqrt(3)), all radius 1
    # Convert to complex and curvature
    z1 = complex(0, 0)
    z2 = complex(2, 0)
    z3 = complex(1, sqrt(3))
    k1 = k2 = k3 = 1
    current_circle = [
        [z1, k1],
        [z2, k2],
        [z3, k3]
    ]
    result = complex_descartes_theorem(current_circle)
    # Should return two possible centers/radii for the fourth circle
    assert isinstance(result, list)
    assert len(result) == 2
    # Check that the result contains real numbers
    for circle in result:
        assert isinstance(circle[0], float)
        assert isinstance(circle[1], float)
        assert isinstance(circle[2], float)