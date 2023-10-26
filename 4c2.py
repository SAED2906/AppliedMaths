import numpy as np
import matplotlib.pyplot as plt

# Given parameters
F0 = 1
omega = 3
gamma = 3.2
t = np.linspace(0, 100, 1000)

# Solution x(t)
x = (F0 / (omega**2 - gamma**2)) * (np.cos(gamma * t) - np.cos(omega * t))
x_dot = (F0 / (omega**2 - gamma**2)) * (-gamma * np.sin(gamma * t) + omega * np.sin(omega * t))

# Corrected envelope
envelope = np.abs(F0 / (omega**2 - gamma**2)) * np.sqrt(2 - 2 * np.cos((gamma - omega) * t))

# Plot x(t) vs. t with corrected envelope
plt.figure(figsize=(10,6))
plt.plot(t, x, label='x(t)')
plt.plot(t, envelope, 'r--', label='Envelope')
plt.plot(t, -envelope, 'r--')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.title('Time vs. Displacement with Envelope')
plt.legend()
plt.grid(True)

# Plot x'(t) vs. x(t)
plt.figure(figsize=(10,6))
plt.plot(x, x_dot)
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (x\')')
plt.title('Displacement vs. Velocity')
plt.grid(True)

plt.show()

