import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.axis('tight')
ax.axis('off')

cols = ['A', 'B', 'C']
vals = [[1, 4, 7], [2, 5, 8]]

ax.table(cellText=vals, colLabels=cols, loc='center')
plt.title("Table Example")
plt.show()
