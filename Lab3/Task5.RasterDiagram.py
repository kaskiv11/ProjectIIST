#5.	Нарисувати діаграму растрову


import matplotlib.pyplot as plt
import numpy as np

# Генеруємо випадкові дані для діаграми
data = np.random.rand(1000, 1000)

# Створюємо растрову діаграму
plt.figure(figsize=(12, 10))
plt.imshow(data, cmap='plasma', interpolation='gaussian')
plt.colorbar(label='Color Intensity')
plt.title('Large Raster Diagram', fontsize=20, color='blue')
plt.axis('off')


plt.show()
