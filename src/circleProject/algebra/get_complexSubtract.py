"""get_complexRoot returns the root of a complex number"""

from __future__ import annotations

from math import sqrt, atan2, cos, sin

def get_complexSubtract(complex_number1,complex_number2):
    #   Subtracts two complex numbers and returns resulting complex number
    #   (a + ib) - (c + id) = (a - c) + i(b - d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a-c, b-d)