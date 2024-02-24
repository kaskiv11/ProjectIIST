#134. Напишіть програму на Python, щоб визначити, працює оболочка python у 32-бітному або 64-бітному режимі в операційній системі
import platform

def check_python_bit_mode():
    # Отримання інформації про платформу
    platform_info = platform.architecture()

    # Перевірка бітового режиму
    if platform_info[0] == '32bit':
        print("Python працює у 32-бітному режимі.")
    elif platform_info[0] == '64bit':
        print("Python працює у 64-бітному режимі.")
    else:
        print("Не вдалося визначити бітовий режим Python.")

if __name__ == "__main__":
    # Виклик функції для перевірки бітового режиму Python
    check_python_bit_mode()
