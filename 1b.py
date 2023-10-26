from scipy.optimize import fsolve
import numpy as np

# Define the function
def f(x):
    return np.exp(x) - 5*x

# Use fsolve to find the roots, with initial guesses based on the plot
root1 = fsolve(f, -2)  # initial guess of 0
root2 = fsolve(f, 3)  # initial guess of -1

print("Root 1:", root1)
print("Root 2:", root2)

