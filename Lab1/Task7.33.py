#90. Напишіть програму на Python
# для створення копій власного вихідного коду.
import shutil
import os

# Отримуємо шлях до власного вихідного коду
current_script_path = os.path.realpath(__file__)

# Введіть шлях для копіювання (може бути тим же, або іншим)
copy_destination_path = input("Введіть шлях для створення копії: ")

try:
    # Копіюємо вихідний код
    shutil.copy2(current_script_path, copy_destination_path)
    print(f"Копію вихідного коду створено успішно. Шлях: {copy_destination_path}")
except FileNotFoundError:
    print(f"Файл '{current_script_path}' не знайдено.")
except PermissionError:
    print(f"Немає доступу до файлу '{current_script_path}'. Перевірте права доступу.")
except Exception as e:
    print(f"Виникла помилка: {e}")
