# Descartes Kissing Circles + Apollonian Gasket's

Descartes' kissing circles, also known as the Descartes Circle Theorem, describes the relationship between four mutually tangent circles. This elegant mathematical concept, formulated by René Descartes in 1643, provides a formula to calculate the ***curvature*** of a fourth circle when three mutually tangent circles are known.

### The Descartes Circle Theorem
Given three circles touching tangentially, the inner circle that fits between all three circles has curvature k4 such that:

###### $$(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)$$ $\\Rightarrow$ $$k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1 k_2 + k_2 k_3 + k_1 k_3}$$

### Complex Decartes Circle Theorem
Finds the ***center*** of the fourth circles radius

Calculates the center of the tangential circle:

###### z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4

z is the complex number of x,y (center coordinates or circle) where z = x + iy  

***Papers***: https://arxiv.org/pdf/math/0101066

***Key Properties***

Mutual Tangency: Each circle touches exactly three others at single points
Curvature Relationship: The curvatures follow a precise quadratic relationship
Soddy Circles: Named after Frederick Soddy, who rediscovered the theorem in 1936

***Applications***

Fractal Geometry: Apollonian gaskets and circle packings
Number Theory: Connections to continued fractions and Diophantine equations
Complex Analysis: Möbius transformations and inversion geometry