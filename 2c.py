import numpy as np
from scipy.optimize import fsolve

# Given parameters
g = 9.81  # m/s^2
r = 0.15
v0 = 10
theta = np.radians(60)  # Convert degrees to radians

# Define the function f(R)
def f(R):
    return (g/r + v0 * np.sin(theta)) * (R / (v0 * np.cos(theta))) + g/r**2 * np.log(1 - r*R/(v0 * np.cos(theta)))

# Use fsolve to find the root, with an initial guess of 10
R_solution = fsolve(f, 10)[0]

print("The value of R is approximately:", R_solution, "meters")

