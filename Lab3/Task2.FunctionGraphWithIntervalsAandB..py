import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def your_function(x):
    # Замініть цю функцію на свою
    return np.sin(x)  # Приклад: функція sin(x)

# Визначення інтервалу та кількості точок
a, b = 0, 2*np.pi  # Приклад: інтервал для функції sin(x)
num_points = 100

# Генерація значень x та y
x_values = np.linspace(a, b, num_points)
y_values = your_function(x_values)

# Налаштування стилів seaborn
sns.set(style="whitegrid")
sns.set_palette("husl")

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='sin(x)', linewidth=2, color='darkorange')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Графік функції sin(x) на інтервалі [0, 2π]')
plt.legend()

# Підписати інтервал на графіку
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(a, color='red', linestyle='--', label=f'a = {a}')
plt.axvline(b, color='blue', linestyle='--', label=f'b = {b}')

# Додавання легенди для інтервалів
plt.legend()

# Додавання сітки
plt.grid(True, linestyle='--', alpha=0.7)

# Відображення графіку
plt.show()
