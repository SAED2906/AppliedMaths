import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of first-order ODEs
def forced_oscillator(U, t):
    x, v = U
    dxdt = v
    dvdt = np.cos(3.2*t) - 9*x
    return [dxdt, dvdt]

# Initial conditions
x0 = 0
v0 = 0

# Time span
t = np.linspace(0, 100, 1000)

# Solve the system of ODEs
solution = odeint(forced_oscillator, [x0, v0], t)

# Extract x and v values from the solution
x_vals = solution[:, 0]
v_vals = solution[:, 1]

# Plot x(t) vs. t
plt.figure()
plt.plot(t, x_vals, label='x(t)')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.title('Time vs. Displacement')
plt.grid(True)

# Plot v(t) vs. x(t)
plt.figure()
plt.plot(x_vals, v_vals, label="x'(t) vs x(t)")
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (x\')')
plt.title('Displacement vs. Velocity')
plt.grid(True)

plt.show()

