from math import sqrt
from descartes_theorems import find_descartes_circles
    
def test_find_descartes_circles():
    # Setup: three circles, tracker marks them as mutually tangent

    R = 1
    current_circle = [
        [0, 0, R],
        [2, 0, R],
        [1, sqrt(3), R]
    ]
    tracker = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    # Mark the triple as tangent
    tracker[0][1][2] = 1
    # Should return a list of circles (with unique radii/centers)
    result = find_descartes_circles(current_circle, tracker, R)
    assert isinstance(result, list)
    assert all(len(c) == 3 for c in result)
    # Should contain more than the original three circles
    assert len(result) >= 3