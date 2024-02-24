# Вправа 13. Розмістити на полі 8×8 нулі та одиниці в шахматному порядку, використовуючи функцію повторення (*).
# In [2] task_13()
# значень n×m і обчислити мінімальне, максимальне значення, середнє та Out [2] [[0 1 0 1 0 1 0 1]
# середньо квадратичне відхилення, округлене до 3 знаків після коми. [1 0 1 0 1 0 1 0]
# [0 1 0 1 0 1 0 1]
# In [2] task_10() [1 0 1 0 1 0 1 0]
# 4 5 [0 1 0 1 0 1 0 1]
# Out [2] мінімум: 0.038 [1 0 1 0 1 0 1 0]
# максимум: 0.946 [0 1 0 1 0 1 0 1]
# середнє: 0.593 [1 0 1 0 1 0 1 0]]
# дисперсія: 0.302

import numpy as np

def task_13():
    # Створення шахматної дошки
    chessboard = np.zeros((8, 8), dtype=int)
    chessboard[1::2, ::2] = 1
    chessboard[::2, 1::2] = 1

    # Виведення шахматної дошки
    print(chessboard)

    # Обчислення мінімального, максимального, середнього та середньо квадратичного відхилення
    minimum_value = np.min(chessboard)
    maximum_value = np.max(chessboard)
    mean_value = np.mean(chessboard)
    std_deviation = np.std(chessboard)

    # Виведення результатів
    print(f"\nМінімум: {minimum_value:.3f}")
    print(f"Максимум: {maximum_value:.3f}")
    print(f"Середнє: {mean_value:.3f}")
    print(f"Середньо квадратичне відхилення: {std_deviation:.3f}")

# Виклик функції для вправи 13
task_13()

