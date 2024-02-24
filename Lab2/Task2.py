# Обчислення рівняння матриці 4x4
import numpy as np

# Задання матриці коефіцієнтів та вектора правих частин
coefficients = np.array([
    [1, 1, 1, -1],
    [0, 1, 2, -1],
    [1, -1, 0, -1],
    [-1, 3, -2, 0]
])

right_hand_side = np.array([0, 2, -1, 0])

# Розв'язок системи рівнянь
solution = np.linalg.solve(coefficients, right_hand_side)

# Виведення результату
print("Розв'язок системи рівнянь:")
print(solution)