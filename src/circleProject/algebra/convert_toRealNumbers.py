"""convert_toRealNumbers returns the real components of imaginary numbers in a list."""

from __future__ import annotations

def convert_toRealNumbers(tangential_circles):
    temp = []
    for i in range(0,len(tangential_circles)):
        temp.append([tangential_circles[i][0].real,tangential_circles[i][0].imag,tangential_circles[i][1]])
    return temp