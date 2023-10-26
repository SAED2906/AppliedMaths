import numpy as np
from scipy.optimize import fsolve

# Given parameters
g = 9.81  # m/s^2
r = 0.15
v0 = 10
theta = np.radians(60)  # Convert degrees to radians

# Define the function f(R)
def f(R):
    return (g/r + v0*np.sin(theta))*(R/(v0*np.cos(theta))) + (g/r**2)*np.log(1 - r*R/(v0*np.cos(theta)))

# Use fsolve to find the root
R_initial_guess = 10  # Initial guess for the range
R_solution = fsolve(f, R_initial_guess)

print(f"The solution for R when f(R) = 0 is approximately {R_solution[0]:.2f} meters.")

