import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of first-order ODEs
def forced_spring_mass_system(U, t):
    u1, u2 = U
    du1dt = u2
    du2dt = -9 * u1 + np.cos(3.002*t)
    return [du1dt, du2dt]

# Initial conditions
u1_0 = 0
u2_0 = 0

# Time span with increased step count
t = np.linspace(0, 100, 10000)

# Solve the system of ODEs
solution = odeint(forced_spring_mass_system, [u1_0, u2_0], t)

# Extract u1 (x) and u2 (x') values from the solution
u1_vals = solution[:, 0]
u2_vals = solution[:, 1]

# Calculate the envelope
omega = 3
F0 = 1
envelope = (F0 / (2 * omega)) * t

# Plot u1 (x) vs. t with envelope
plt.figure()
plt.plot(t, u1_vals, label="x(t)")
plt.plot(t, envelope, 'r--', label="Envelope")
plt.plot(t, -envelope, 'r--')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.title('Time vs. Displacement with Envelope')
plt.legend()
plt.grid(True)

# Plot u2 (x') vs. u1 (x) with increased smoothness
plt.figure()
plt.plot(u1_vals, u2_vals)
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (x\')')
plt.title('Displacement vs. Velocity')
plt.grid(True)

plt.show()

