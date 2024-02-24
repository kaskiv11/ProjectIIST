import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Дані для 3D-діаграми
categories = ['Витрати на їжу', 'Оплата житла', 'Розваги', 'Одяг', 'Збереження']
percentages = [30, 20, 15, 10, 25]

# Кольори для кожної категорії
colors = ['#FF5757', '#5799FF', '#FFB957', '#FF7C57', '#C7A2FF']

# Створення фігури та вісей 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Задання позицій стовпців
x_pos = np.arange(len(categories))

# Розміри стовпців
dx = np.ones(len(categories))
dy = np.ones(len(categories))
dz = percentages

# Малювання 3D-пірамідальних стовпців
bars = ax.bar3d(x_pos, dy, np.zeros_like(dz), dx, dy, dz, color=colors, shade=True, alpha=0.8)

# Додавання підписів до вісей
ax.set_xticks(x_pos + 0.5)
ax.set_xticklabels(categories)
ax.set_xlabel('Категорії')
ax.set_ylabel('Відсотки')
ax.set_zlabel('Значення')

# Додавання заголовка
plt.title('3D-пірамідальна діаграма розподілу грошей', fontsize=16, fontweight='bold', color='#333333')

# Додавання підписів до стовпців
for i, label in enumerate(percentages):
    ax.text(x_pos[i] + 0.5, 1.5, label, f'{label}%', ha='center', va='center', color='#333333', fontweight='bold')

# Відображення графіку
plt.show()

