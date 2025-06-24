Descartes Kissing Circles + Apollonian Gasket's

Descartes' kissing circles, also known as the Descartes Circle Theorem, describes the relationship between four mutually tangent circles. This elegant mathematical concept, formulated by René Descartes in 1643, provides a formula to calculate the curvature of a fourth circle when three mutually tangent circles are known.

The Descartes Circle Theorem
Given three circles touching tangentially, the inner circle that fits inbetween all three has a curvature k4 such that:
(k₁ + k₂ + k₃ + k₄)² = 2(k₁² + k₂² + k₃² + k₄²) => k4 = k1+k2+k3+/-2*sqrt(k1*k2+k2*k3+k1*k3)

Complex Decartes Circle Theorem
Used to find the center of the fourth circles radius

Calculates the center of the tangential circle:
z4 = z1*k1+z2*k2+z3*k3+/-2(root(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
z is the complex number of x,y (center coordinates or circle) where z = x + iy  

Papers: https://arxiv.org/pdf/math/0101066

Key Properties

Mutual Tangency: Each circle touches exactly three others at single points
Curvature Relationship: The curvatures follow a precise quadratic relationship
Soddy Circles: Named after Frederick Soddy, who rediscovered the theorem in 1936

Applications
Mathematics

Fractal Geometry: Apollonian gaskets and circle packings
Number Theory: Connections to continued fractions and Diophantine equations
Complex Analysis: Möbius transformations and inversion geometry

The code in this repository illustrates this theorem to near perfection
