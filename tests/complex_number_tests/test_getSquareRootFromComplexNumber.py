from complex_number_arithmetic import getSquareRootFromComplexNumber # A test function for add_numbers

def test_getSquareRootFromComplexNumber():
    """
    (a + ib) = (sqrt(r) * cos(arctangent(theta/2), sqrt(r) * sin(arctangent(theta/2)i)
    """
    result = getSquareRootFromComplexNumber(complex(3,4))
    assert result == complex(2,1)