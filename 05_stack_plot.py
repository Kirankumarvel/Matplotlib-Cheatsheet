import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]
y2 = [0.5, 1, 1.5, 2, 2.5]
y3 = [5, 3, 2, 1, 0]

plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'], colors=['r', 'g', 'b'])
plt.title("Stack Plot")
plt.legend(loc='upper left')
plt.show()
