"""Load raw data from disk."""

from __future__ import annotations

from math import sqrt

def descartes_theorem(k1,k2,k3):
    #   k4 = k1+k2+k3+/-2*sqrt(k1*k2+k2*k3+k1*k3)
    #   k4 has two possible values
    k_sum = k1+k2+k3
    k_multiple = max((k1*k2) + (k2*k3) + (k1*k3),0)
    # print(k_multiple)
    k4_a = k_sum + 2*sqrt(k_multiple)
    k4_b = k_sum - 2*sqrt(k_multiple)
    return k4_a, k4_b