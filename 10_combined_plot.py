import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='Line')
ax.scatter(x, y, color='red', s=10, label='Points')
ax.set_title("Combined Line + Scatter Plot")
ax.legend()
plt.show()
