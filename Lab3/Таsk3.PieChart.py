# 3 Нарисувати кругову діаграму і підписати частини


import matplotlib.pyplot as plt

# Дані для кругової діаграми
categories = ['Витрати на їжу', 'Оплата житла', 'Розваги', 'Одяг', 'Збереження']
percentages = [30, 20, 15, 10, 25]  # Відсотки розподілу грошей

# Кольори для кожної категорії
colors = ['#FF9999', '#66B3FF', '#FFCC99', '#FFA07A', '#C2C2F0']

# Фон графіку
fig, ax = plt.subplots()
fig.patch.set_facecolor('#f9f9f9')

# Встановлення вибірки "explode" для виділення частини діаграми (наприклад, для виділення "Витрати на їжу")
explode = (0.1, 0, 0.2, 0, 0)  # Додано виділення для категорії 'Розваги'

# Стилізація
wedgeprops = {'linewidth': 2, 'edgecolor': 'w'}

# Додавання коли, щоб виглядало як круг
ax.axis('equal')

# Кругова діаграма під кутом
wedges, texts, autotexts = ax.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=45, colors=colors,
                                  explode=explode, wedgeprops=wedgeprops)

# Зміна кольору тексту
for text, autotext in zip(texts, autotexts):
    text.set_color('#333333')
    autotext.set_color('#333333')

# Підписати діаграму
plt.title('Розподіл грошей на різні категорії', fontsize=14, fontweight='bold', color='#333333')

# Вивести діаграму
plt.show()
