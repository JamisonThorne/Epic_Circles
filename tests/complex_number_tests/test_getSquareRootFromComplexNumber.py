from complex_number_arithmetic import getComplexNumberSquareRoot
from math import isclose, sqrt, atan2, cos, sin, pi

def test_getComplexNumberSquareRoot():
    z = complex(3, 4)
    # Expected roots: 2 + 1j and -2 - 1j
    result = getComplexNumberSquareRoot(z)
    # Check if result is close to one of the two possible roots
    expected1 = complex(2, 1)
    expected2 = complex(-2, -1)
    assert (isclose(result.real, expected1.real, abs_tol=1e-6) and isclose(result.imag, expected1.imag, abs_tol=1e-6)) or \
           (isclose(result.real, expected2.real, abs_tol=1e-6) and isclose(result.imag, expected2.imag, abs_tol=1e-6))

    # Test a purely real positive number
    z2 = complex(9, 0)
    result2 = getComplexNumberSquareRoot(z2)
    expected3 = complex(3, 0)
    expected4 = complex(-3, 0)
    assert (isclose(result2.real, expected3.real, abs_tol=1e-6) and isclose(result2.imag, expected3.imag, abs_tol=1e-6)) or \
           (isclose(result2.real, expected4.real, abs_tol=1e-6) and isclose(result2.imag, expected4.imag, abs_tol=1e-6))

    # Test a purely imaginary number
    z3 = complex(0, 4)
    result3 = getComplexNumberSquareRoot(z3)
    # The roots are approximately 1.4142 + 1.4142j and -1.4142 - 1.4142j
    expected5 = complex(sqrt(2), sqrt(2))
    expected6 = complex(-sqrt(2), -sqrt(2))
    assert (isclose(result3.real, expected5.real, abs_tol=1e-6) and isclose(result3.imag, expected5.imag, abs_tol=1e-6)) or \
           (isclose(result3.real, expected6.real, abs_tol=1e-6) and isclose(result3.imag, expected6.imag, abs_tol=1e-6))