import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
data = rng.standard_normal(1000)

plt.hist(data, bins=10, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
