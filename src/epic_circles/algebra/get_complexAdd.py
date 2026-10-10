"""get_complexRoot returns the root of a complex number"""

from __future__ import annotations

def get_complexAdd(complex_number1,complex_number2):
    #   Adds two complex numbers together and returns resulting complex number
    #   (a + ib) + (c + id) = (a + c) + i(b + d)
    a = complex_number1.real
    b = complex_number1.imag
    c = complex_number2.real
    d = complex_number2.imag
    return complex(a+c, b+d)