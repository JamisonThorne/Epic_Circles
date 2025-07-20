from complex_number_arithmetic import getComplexNumberSubtraction # A test function for add_numbers

def test_getComplexNumberSubtract():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberSubtraction(complex(7,5),complex(3,2))
    assert result == complex(4,3)
    
def test_getComplexNumberSubtract():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberSubtraction(complex(7,9),complex(3,4))
    assert result == complex(4,5)
    
def test_getComplexNumberSubtract():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberSubtraction(complex(-12,6),complex(7,5))
    assert result == complex(-19,1)
    
def test_getComplexNumberSubtract():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberSubtraction(complex(3,5),complex(-2,2))
    assert result == complex(5,3)