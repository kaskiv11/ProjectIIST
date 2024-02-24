# 40. Напишіть програму на Python для обчислення відстані між точками (x1, y1) і (x2, y2).
import math


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


if __name__ == "__main__":
    # Введення координат точок від користувача
    x1 = float(input("Введіть координату x1: "))
    y1 = float(input("Введіть координату y1: "))
    x2 = float(input("Введіть координату x2: "))
    y2 = float(input("Введіть координату y2: "))

    # Виклик функції для обчислення відстані
    distance = calculate_distance(x1, y1, x2, y2)

    # Виведення результату
    print(f"Відстань між точками ({x1}, {y1}) і ({x2}, {y2}): {distance}")
