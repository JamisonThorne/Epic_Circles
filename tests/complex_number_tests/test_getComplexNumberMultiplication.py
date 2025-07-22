from complex_number_arithmetic import getComplexNumberMultiplication # A test function for add_numbers

def test_getComplexNumberMultiplication():
    """
    (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    """
    result = getComplexNumberMultiplication(complex(7,5),complex(3,2))
    assert result == complex(11,29)

def test_getComplexNumberMultiplication():
    """
    (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    """
    result = getComplexNumberMultiplication(complex(-7,5),complex(3,-2))
    assert result == complex(-11,29)