def find_max_min(sequence):
    if not sequence:
        return None, None  # Повертаємо None, None для пустої послідовності

    # Використовуємо функції min() та max() для знаходження мінімального та максимального значень
    minimum = min(sequence)
    maximum = max(sequence)

    return minimum, maximum

if __name__ == "__main__":
    # Приклад використання функції зі списком чисел
    numbers = [5, 2, 8, 1, 9, 3]

    # Виклик функції та виведення результату
    min_value, max_value = find_max_min(numbers)
    print(f"Мінімальне значення: {min_value}")
    print(f"Максимальне значення: {max_value}")
