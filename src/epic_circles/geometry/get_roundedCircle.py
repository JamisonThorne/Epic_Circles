"""Train a trivial baseline model (mean predictor), as a stand-in for a real one."""

from __future__ import annotations

import numpy as np

def round_my_circle(circle):
    for i in range(0,np.shape(circle)[0]):
        for j in range(0,np.shape(circle)[1]):
            # circle[i][j] = round(circle[i][j], 3)
            if circle[i][j] == -0.0:
                circle[i][j] = 0.0
    return circle