from geometry import are_circles_tangent

def test_are_circles_tangent():
    c1 = [0, 0, 1]
    c2 = [2, 0, 1]
    assert are_circles_tangent(c1, c2)
    c3 = [0, 0, 1]
    c4 = [0, 0, 2]
    assert are_circles_tangent(c3, c4)
    c5 = [0, 0, 1]
    c6 = [3, 0, 1]
    assert not are_circles_tangent(c5, c6)