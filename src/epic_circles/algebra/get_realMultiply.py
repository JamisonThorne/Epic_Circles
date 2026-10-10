"""get_complexRoot returns the root of a complex number"""

from __future__ import annotations

def get_realMultiply(complex_number,constant_number):
    a = complex_number.real
    b = complex_number.imag
    return complex((a*constant_number),(b*constant_number))
