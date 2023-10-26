import numpy as np
import matplotlib.pyplot as plt

# Define the time array
t = np.linspace(0, 10, 1000)

# Define the solution x(t) and its derivative x'(t)
x = np.exp(-t/2) * (np.cos(np.sqrt(35)/2 * t) + (7/np.sqrt(35)) * np.sin(np.sqrt(35)/2 * t))
x_prime = -0.5 * np.exp(-t/2) * (np.cos(np.sqrt(35)/2 * t) + (7/np.sqrt(35)) * np.sin(np.sqrt(35)/2 * t)) - np.exp(-t/2) * (np.sqrt(35)/2 * (7/np.sqrt(35)) * np.cos(np.sqrt(35)/2 * t) - np.sqrt(35)/2 * np.sin(np.sqrt(35)/2 * t))

# Pseudo-amplitude
pseudo_amplitude = (7/np.sqrt(35)) * np.exp(-t/2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='x(t)')
plt.plot(x, x_prime, label="x'(t)")
plt.plot(t, pseudo_amplitude, 'r--', label='Pseudo-Amplitude')
plt.plot(t, -pseudo_amplitude, 'r--')  # Negative pseudo-amplitude
plt.xlabel('Time (t) / Displacement (x)')
plt.ylabel('Displacement (x) / Velocity (x\')')
plt.title('Damped Harmonic Oscillator')
plt.legend()
plt.grid(True)
plt.show()

