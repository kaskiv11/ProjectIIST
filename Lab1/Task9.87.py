#74. Напишіть програму на Python для хеширования слова.
import os

# Введіть шлях до файлу
file_path = input("Введіть шлях до файлу: ")

try:
    # Отримати розмір файлу
    file_size = os.path.getsize(file_path)

    # Вивести розмір файлу
    print(f"Розмір файлу '{file_path}': {file_size} байт")
except FileNotFoundError:
    print(f"Файл '{file_path}' не знайдено.")
except PermissionError:
    print(f"Немає доступу до файлу '{file_path}'. Перевірте права доступу.")
except Exception as e:
    print(f"Виникла помилка: {e}")
