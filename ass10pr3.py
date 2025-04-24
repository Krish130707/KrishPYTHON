'''Take N (N >= 10) random 2-dimensional points
represented in cartesian coordinate space. Store them in a
numpy array. Convert them to polar coordinates.'''

import numpy as np

N = 10

cartesian_points = np.random.uniform(-10, 10, (N, 2))

def cartesian_to_polar(points):
    x, y = points[:, 0], points[:, 1]
    r = np.sqrt(x**2 + y**2)  # Fix: Use **2 for squaring
    theta = np.arctan2(y, x)  
    return np.column_stack((r, theta))

polar_points = cartesian_to_polar(cartesian_points)

print(f"Cartesian Points:\n{cartesian_points}\n")
print(f"Polar Coordinates:\n{polar_points}")
