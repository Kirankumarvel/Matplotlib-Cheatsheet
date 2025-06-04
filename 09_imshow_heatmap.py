import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.title("Imshow - Random Heatmap")
plt.colorbar()
plt.show()
