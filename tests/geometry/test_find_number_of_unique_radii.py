from geometry import find_number_of_unique_radii

def test_find_number_of_unique_radii():
    arr = [[0, 0, 1], [1, 1, 2], [2, 2, 1]]
    unique = find_number_of_unique_radii(arr)
    assert set(unique) == {1, 2}