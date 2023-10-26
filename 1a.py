import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3, 400)
y = np.exp(x) - 5*x

plt.plot(x, y, label="f(x) = e^x - 5x")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Graph of f(x) = e^x - 5x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

