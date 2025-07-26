from geometry import get_unique_array

def test_get_unique_array():
    arr = [1, 2, 2, 3, 1]
    unique = get_unique_array(arr)
    assert set(unique) == {1, 2, 3}