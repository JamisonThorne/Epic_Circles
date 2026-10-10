"""Write processed data back to disk."""

from __future__ import annotations



def complex_descartes_theorem(current_circle):
    kissing_circle = []
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy    
    z1, z2, z3 = current_circle[0][0], current_circle[1][0], current_circle[2][0]
    k1, k2, k3 = current_circle[0][1], current_circle[1][1], current_circle[2][1]
    k4a, k4b = descartes_theorem(k1,k2,k3)
    for k4 in [k4a, k4b]:
        r4 = 1/k4
        #########
        #   Calculate the first portion of Descartes Complex Theorem
        z1k1 = getComplexNumberMultipliedConstant(z1,k1)  #   Multiply complex number by curvature k (1/r)
        z2k2 = getComplexNumberMultipliedConstant(z2,k2)  #   Multiply complex number by curvature k (1/r)
        z3k3 = getComplexNumberMultipliedConstant(z3,k3)  #   Multiply complex number by curvature k (1/r)
        first_portion = getComplexNumberSum(getComplexNumberSum(z1k1,z2k2),z3k3)
        ###### 
        #   Calculate the second portion of Descartes Complex Theorem
        z1k1_z2k2_prod = getComplexNumberMultiplication(z1k1,z2k2)    #   Multiple two complex numbers together
        z2k2_z3k3_prod = getComplexNumberMultiplication(z2k2,z3k3)    #   Multiple two complex numbers together
        z1k1_z3k3_prod = getComplexNumberMultiplication(z1k1,z3k3)    #   Multiple two complex numbers together
        complex_number_sum = getComplexNumberSum(getComplexNumberSum(z1k1_z2k2_prod,z2k2_z3k3_prod),z1k1_z3k3_prod)   #   Add together above resulting multiples
        sqrt_second_portion = getComplexNumberSquareRoot(complex_number_sum)  # Calculate the root of the complex number
        z4 = getComplexNumberMultipliedConstant(getComplexNumberSum(first_portion,(getComplexNumberMultipliedConstant(sqrt_second_portion,2))),1/k4)    #   Calculate Final Complex Number
        kissing_circle.append([z4.real,z4.imag,r4]) #   center, radius
        z4 = getComplexNumberMultipliedConstant(getComplexNumberSubtraction(first_portion,(getComplexNumberMultipliedConstant(sqrt_second_portion,2))),1/k4)    #   Calculate Final Complex Number        
        kissing_circle.append([z4.real,z4.imag,r4]) #   center, radius
        return kissing_circle