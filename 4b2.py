import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of first-order ODEs for part (a)
def spring_mass_system_a(U, t):
    u1, u2 = U
    du1dt = u2
    du2dt = -9 * u1
    return [du1dt, du2dt]

# Define the system of first-order ODEs for part (b)
def spring_mass_system_b(U, t):
    u1, u2 = U
    du1dt = u2
    du2dt = -9 * u1 - u2
    return [du1dt, du2dt]

# Initial conditions
u1_0 = 1
u2_0 = 3

# Time span
t = np.linspace(0, 10, 1000)

# Solve the system of ODEs for part (a)
solution_a = odeint(spring_mass_system_a, [u1_0, u2_0], t)
u1_vals_a = solution_a[:, 0]
u2_vals_a = solution_a[:, 1]

# Solve the system of ODEs for part (b)
solution_b = odeint(spring_mass_system_b, [u1_0, u2_0], t)
u1_vals_b = solution_b[:, 0]
u2_vals_b = solution_b[:, 1]

# Calculate the pseudo-amplitude for part (b)
A0 = np.sqrt(1**2 + (7/np.sqrt(35))**2)
pseudo_amplitude = A0 * np.exp(-0.5 * t)

# Plot u1 (x) vs. t for both (a) and (b)
plt.figure()
plt.plot(t, u1_vals_a, label='Part (a)')
plt.plot(t, u1_vals_b, 'r', label='Part (b)')
plt.plot(t, pseudo_amplitude, 'g-.', label='Pseudo-Amplitude')
plt.plot(t, -pseudo_amplitude, 'g-.')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.title('Time vs. Displacement')
plt.legend()
plt.grid(True)

# Plot u2 (x') vs. u1 (x) for both (a) and (b)
plt.figure()
plt.plot(u1_vals_a, u2_vals_a, label="Part (a)")
plt.plot(u1_vals_b, u2_vals_b, 'r--', label="Part (b)")
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (x\')')
plt.title('Displacement vs. Velocity')
plt.legend()
plt.grid(True)

plt.show()

