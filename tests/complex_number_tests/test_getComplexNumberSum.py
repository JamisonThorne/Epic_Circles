from complex_number_arithmetic import getComplexNumberSum # A test function for add_numbers

def test_getComplexNumberSum():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberSum(complex(5,2),complex(3,-7))
    assert result == complex(8,-5)