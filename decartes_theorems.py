def descartes_theorem(k1,k2,k3):
    #   k4 = k1+k2+k3+/-2*sqrt(k1*k2+k2*k3+k1*k3)
    #   k4 has two possible values
    k_sum = k1+k2+k3
    k_multiple = max((k1*k2) + (k2*k3) + (k1*k3),0)
    # print(k_multiple)
    k4_a = k_sum + 2*sqrt(k_multiple)
    k4_b = k_sum - 2*sqrt(k_multiple)
    return k4_a, k4_b

def complex_descartes_theorem(current_circle):
    kissing_circle = []
    #   Calculates the center of the tangential circle:
    #       z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    #   z is the complex number of x,y (center coordinates or circle) where z = x + iy    
    z1 = current_circle[0][0]
    z2 = current_circle[1][0]
    z3 = current_circle[2][0]
    k1 = current_circle[0][1]
    k2 = current_circle[1][1]
    k3 = current_circle[2][1]
    k4a, k4b = Descartes_Theorem(k1,k2,k3)
    for k4 in [k4a, k4b]:
        r4 = 1/k4
        #########
        #   Calculate the first portion of Descartes Complex Theorem
        z1k1 = Complex_Real_Multiply(z1,k1)  #   Multiply complex number by curvature k (1/r)
        z2k2 = Complex_Real_Multiply(z2,k2)  #   Multiply complex number by curvature k (1/r)
        z3k3 = Complex_Real_Multiply(z3,k3)  #   Multiply complex number by curvature k (1/r)
        first_portion = Complex_Add(Complex_Add(z1k1,z2k2),z3k3)
        ###### 
        #   Calculate the second portion of Descartes Complex Theorem
        z1k1_z2k2_prod = Complex_Multiply(z1k1,z2k2)    #   Multiple two complex numbers together
        z2k2_z3k3_prod = Complex_Multiply(z2k2,z3k3)    #   Multiple two complex numbers together
        z1k1_z3k3_prod = Complex_Multiply(z1k1,z3k3)    #   Multiple two complex numbers together
        complex_number_sum = Complex_Add(Complex_Add(z1k1_z2k2_prod,z2k2_z3k3_prod),z1k1_z3k3_prod)   #   Add together above resulting multiples
        sqrt_second_portion = Complex_Root(complex_number_sum)  # Calculate the root of the complex number
        z4 = Complex_Real_Multiply(Complex_Add(first_portion,(Complex_Real_Multiply(sqrt_second_portion,2))),1/k4)    #   Calculate Final Complex Number
        kissing_circle.append([z4.real,z4.imag,r4]) #   center, radius
        z4 = Complex_Real_Multiply(Complex_Sub(first_portion,(Complex_Real_Multiply(sqrt_second_portion,2))),1/k4)    #   Calculate Final Complex Number        
        kissing_circle.append([z4.real,z4.imag,r4]) #   center, radius
        return kissing_circle
    
def find_descartes_circles(current_circle,tracker,R):
    circle_results = []
    final_circles = []
    for i in range(0,len(current_circle)):
        for j in range(0,len(current_circle)):
            for k in range(0,len(current_circle)):
                if i != j and i != k and j != k:  # Ensure we are not comparing the same circle
                    if tracker[i][j][k] == 1:
                        tangential_circles = copy.deepcopy(current_circle)
                        tangential_circles = [tangential_circles[i], tangential_circles[j], tangential_circles[k]]
                        if tangential_circles[0][2] == R:
                            tangential_circles[0][2] = -1 * tangential_circles[0][2]
                        tangential_circles = convert_from_r_to_k(tangential_circles)
                        tangential_circles = convert_toComplexNumbers(tangential_circles)
                        kissing_circles = complexDescartesTheorem(tangential_circles)
                        tangential_circles[:3] = convert_toRealNumbers(tangential_circles[:3])
                        tangential_circles[:3] = convert_from_k_to_r(tangential_circles[:3])
                        if tangential_circles[0][2] == -1*(R/1):
                            tangential_circles[0][2] = -1 * tangential_circles[0][2]
                        kissing_circles = round_my_circle(kissing_circles)
                        tangential_circles = round_my_circle(tangential_circles)
                        tangential_circles = find_my_tangent_circle(tangential_circles,kissing_circles)
                        circle_results.append(tangential_circles)
    for items in circle_results:
        for item in items: 
            final_circles.append(item)
    return get_unique_array(final_circles)