"""Write processed data back to disk."""

from __future__ import annotations

from epic_circles.theorems.descartesTheorem import descartesTheorem
from epic_circles.algebra.get_complexAdd import get_complexAdd
from epic_circles.algebra.get_complexSubtract import get_complexSubtract
from epic_circles.algebra.get_complexRoot import get_complexRoot
from epic_circles.algebra.get_complexMultiply import get_complexMultiply
from epic_circles.algebra.get_realMultiply import get_realMultiply

def complex_descartesTheorem(current_circle):
    kissing_circle = []
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy    
    z1, z2, z3 = current_circle[0][0], current_circle[1][0], current_circle[2][0]
    k1, k2, k3 = current_circle[0][1], current_circle[1][1], current_circle[2][1]
    k4a, k4b = descartesTheorem(k1,k2,k3)
    for k4 in [k4a, k4b]:
        r4 = 1/k4
        #########
        #   Calculate the first portion of Descartes Complex Theorem
        z1k1 = get_realMultiply(z1,k1)  #   Multiply complex number by curvature k (1/r)
        z2k2 = get_realMultiply(z2,k2)  #   Multiply complex number by curvature k (1/r)
        z3k3 = get_realMultiply(z3,k3)  #   Multiply complex number by curvature k (1/r)
        first_portion = get_complexAdd(get_complexAdd(z1k1,z2k2),z3k3)
        ###### 
        #   Calculate the second portion of Descartes Complex Theorem
        z1k1_z2k2_prod = get_complexMultiply(z1k1,z2k2)    #   Multiple two complex numbers together
        z2k2_z3k3_prod = get_complexMultiply(z2k2,z3k3)    #   Multiple two complex numbers together
        z1k1_z3k3_prod = get_complexMultiply(z1k1,z3k3)    #   Multiple two complex numbers together
        complex_number_sum = get_complexAdd(get_complexAdd(z1k1_z2k2_prod,z2k2_z3k3_prod),z1k1_z3k3_prod)   #   Add together above resulting multiples
        sqrt_second_portion = get_complexRoot(complex_number_sum)  # Calculate the root of the complex number
        z4 = get_realMultiply(get_complexAdd(first_portion,(get_realMultiply(sqrt_second_portion,2))),1/k4)    #   Calculate Final Complex Number
        kissing_circle.append([z4.real,z4.imag,r4]) #   center, radius
        z4 = get_realMultiply(get_complexSubtract(first_portion,(get_realMultiply(sqrt_second_portion,2))),1/k4)    #   Calculate Final Complex Number        
        kissing_circle.append([z4.real,z4.imag,r4]) #   center, radius
        return kissing_circle