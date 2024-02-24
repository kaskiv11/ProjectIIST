# Обчислення A( A^2 − B) − 2( B + A) B  для матриць A та B    3*3
import numpy as np

# Задання матриць A та B
A = np.array([
    [2, 3, 1],
    [-1, 2, 4],
    [5, 3, 0]
])

B = np.array([
    [2, 7, 13],
    [-1, 0, 5],
    [5, 13, 21]
])

# Обчислення виразу A(A^2 - B) - 2(B + A)B
result = np.dot(A, np.dot(np.power(A, 2) - B, A)) - 2 * np.dot(B + A, B)

# Виведення результату
print("Результат обчислення виразу для матриць A та B:")
print(result)
