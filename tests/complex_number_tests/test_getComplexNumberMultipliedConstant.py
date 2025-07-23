from complex_number_arithmetic import getComplexNumberMultipliedConstant

def test_getComplexNumberMultipliedConstant():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberMultipliedConstant(complex(7,5),2)
    assert result == complex(14,10)
    
def test_getComplexNumberMultipliedConstant():
    """
    Tests the addition of two positive numbers.
    """
    result = getComplexNumberMultipliedConstant(complex(-12,6),4)
    assert result == complex(-48,24)