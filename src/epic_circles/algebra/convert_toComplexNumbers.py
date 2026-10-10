"""convert_toComplexNumbers returns the complex conjugates of their real counterparts in a list"""

from __future__ import annotations

def convert_toComplexNumbers(tangential_circles):
    temp = []
    for i in range(0,len(tangential_circles)):
        temp.append([complex(tangential_circles[i][0],tangential_circles[i][1]),tangential_circles[i][2]])
    return temp