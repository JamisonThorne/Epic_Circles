from geometry import circles_intersect_test

def test_circles_intersect_test():
    c1 = [0, 0, 1]
    c2 = [2, 0, 1]
    assert circles_intersect_test(c1, c2, tol=1e-8)
    c3 = [0, 0, 1]
    c4 = [0, 0, 2]
    assert circles_intersect_test(c3, c4, tol=1e-8)
    c5 = [0, 0, 1]
    c6 = [3, 0, 1]
    assert not circles_intersect_test(c5, c6, tol=1e-8)