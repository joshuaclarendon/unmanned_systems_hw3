import numpy as np
from numpy.typing import NDArray

def rotation_matrix(theta: float, x_pos: float = 0.0, y_pos: float = 0) -> NDArray[np.float64]:
    # Added position to matrix so it is full SE2 matrix and not just rotation matrix. This
    # negates the need to add reference frame displcement at the end.
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, x_pos], [s, c, y_pos], [0, 0, 1]])
