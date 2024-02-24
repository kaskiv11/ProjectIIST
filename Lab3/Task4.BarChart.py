import matplotlib.pyplot as plt

# Дані для стовпчикової діаграми
categories = ['Витрати на їжу', 'Оплата житла', 'Розваги', 'Одяг', 'Збереження']
percentages = [30, 20, 15, 10, 25]  # Відсотки розподілу грошей

# Яскраві кольори для кожної категорії
colors = ['#FF5757', '#5799FF', '#FFB957', '#FF7C57', '#C7A2FF']

# Створення стовпчикової діаграми
plt.bar(categories, percentages, color=colors, edgecolor='black', linewidth=1.2)

# Додавання підписів до стовпчиків
for i, value in enumerate(percentages):
    plt.text(i, value + 1, f'{value}%', ha='center', va='bottom', color='#333333', fontweight='bold')

# Додавання заголовка
plt.title('Розподіл грошей на різні категорії', fontsize=14, fontweight='bold', color='#333333')

# Задання стилізації
plt.style.use('seaborn-darkgrid')
plt.rcParams['axes.facecolor'] = '#f9f9f9'

# Виведення діаграми
plt.show()
