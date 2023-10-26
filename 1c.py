import numpy as np
from scipy.optimize import fsolve

# Define the function
def lambert_W(W):
    return W * np.exp(W) - 1

# Use fsolve to find the value of W(1), with an initial guess based on typical values of the Lambert W function
W_value = fsolve(lambert_W, 0)  # initial guess of 0

print("W(1):", W_value)

