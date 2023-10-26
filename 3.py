import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Given values
g = 9.81  # m/s^2
r = 0.15
v0 = 10
theta = np.radians(60)  # Convert to radians

# Initial conditions
x0 = 0
y0 = 0
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)

# Define the system of ODEs
def projectile(Y, t):
    x, vx, y, vy = Y
    dxdt = vx
    dydt = vy
    dvxdt = -r * vx * np.sqrt(vx**2 + vy**2)
    dvydt = -g - r * vy * np.sqrt(vx**2 + vy**2)
    return [dxdt, dvxdt, dydt, dvydt]

# Time span (arbitrarily chosen, might need adjustment)
t = np.linspace(0, 20, 1000)

# Solve the system of ODEs
solution = odeint(projectile, [x0, vx0, y0, vy0], t)

# Extract x and y values from the solution
x_vals = solution[:, 0]
y_vals = solution[:, 2]

# Plot y as a function of x
plt.plot(x_vals, y_vals)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.xlim(0,4.5)
plt.ylim(-1, 4)
plt.title('Projectile motion with quadratic air resistance')
plt.grid(True)
plt.show()

