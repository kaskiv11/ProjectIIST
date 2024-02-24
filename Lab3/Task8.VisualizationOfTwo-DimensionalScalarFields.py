import matplotlib.pyplot as plt
import numpy as np

# Створення двовимірного скалярного поля (приклад)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Створення контурного графіка з підписами та вибіркою кольорів
contour = plt.contourf(X, Y, Z, cmap='viridis', levels=20, extend='both')

# Додавання колірної смуги
cbar = plt.colorbar(contour)
cbar.set_label('Значення')

# Додавання підписів вісей та заголовка
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Контурний графік двовимірного скалярного поля')

# Додавання сітки
plt.grid(True, linestyle='--', alpha=0.7)

# Додавання легенди
plt.colorbar(contour, label='Значення')

# Виведення графіка
plt.show()
