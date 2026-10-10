"""get_complexRoot returns the root of a complex number"""

from __future__ import annotations

from math import sqrt, atan2, cos, sin

def get_complexMultiply(complex_number_1,complex_number_2):
    # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
    a = complex_number_1.real
    b = complex_number_1.imag
    c = complex_number_2.real
    d = complex_number_2.imag
    return complex((a*c)-(b*d),(a*d)+(b*c))