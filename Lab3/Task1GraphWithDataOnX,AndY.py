import matplotlib.pyplot as plt
import seaborn as sns

# Дані на x та y
x_data = [1, 2, 3, 4, 5]
y_data = [10, 12, 5, 8, 15]

# Встановлюємо стиль seaborn для більшої краси
sns.set(style="whitegrid")

# Створюємо графік
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, marker='o', color='#1f78b4', linestyle='-', linewidth=2, markersize=10, label='Мої дані')

# Додаємо назви вісей та заголовок графіка
plt.xlabel('Вісь X', fontsize=14, fontweight='bold', color='#333333')
plt.ylabel('Вісь Y', fontsize=14, fontweight='bold', color='#333333')
plt.title('Графік з даними', fontsize=16, fontweight='bold', color='#333333')

# Додаємо легенду
plt.legend(fontsize=12)

# Змінюємо колір фону графіка
plt.gca().set_facecolor('#f0f0f0')

# Змінюємо колір обрамлення графіка
for spine in plt.gca().spines.values():
    spine.set_edgecolor('#333333')

# Виводимо графік
plt.show()
