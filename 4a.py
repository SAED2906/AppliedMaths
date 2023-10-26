import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of first-order ODEs
def spring_mass_system(U, t):
    u1, u2 = U
    du1dt = u2
    du2dt = -9 * u1
    return [du1dt, du2dt]

# Initial conditions
u1_0 = 1
u2_0 = 3

# Time span
t = np.linspace(0, 10, 1000)

# Solve the system of ODEs
solution = odeint(spring_mass_system, [u1_0, u2_0], t)

# Extract u1 (x) and u2 (x') values from the solution
u1_vals = solution[:, 0]
u2_vals = solution[:, 1]

# Plot u1 (x) vs. t
plt.figure()
plt.plot(t, u1_vals)
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.title('Time vs. Displacement')
plt.grid(True)

# Plot u2 (x') vs. u1 (x)
plt.figure()
plt.plot(u1_vals, u2_vals)
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (x\')')
plt.title('Displacement vs. Velocity')
plt.grid(True)

plt.show()

