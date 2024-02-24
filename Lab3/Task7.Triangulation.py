import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri

# Генеруємо випадкові дані
np.random.seed(0)
x = np.random.rand(30)
y = np.random.rand(30)
z = np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y)

# Створюємо триангуляцію Делоне
triang = tri.Triangulation(x, y)

# Відображаємо триангуляцію з кольоровими трикутниками
plt.figure(figsize=(8, 6))
plt.tripcolor(triang, z, cmap='coolwarm', edgecolors='k')
plt.colorbar(label='Z')
plt.plot(x, y, 'ko', markersize=3)
plt.title('Триангуляція Делоне з кольоровими трикутниками')
plt.show()

