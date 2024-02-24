#12. Напишіть програму на Python для друку календаря з вказаним місяцем і роком.
#Примітка. Використовуйте модуль «календар».

import calendar

def print_calendar(year, month):
    # Виведення календаря за вказаний місяць і рік
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")  # Виведення порожнього місця для днів перед першим та після останнього
            else:
                print(f"{day:2} ", end=" ")
        print()

if __name__ == "__main__":
    # Введення року та місяця від користувача
    year = int(input("Введіть рік: "))
    month = int(input("Введіть місяць (1-12): "))

    # Перевірка правильності введених даних
    if 1 <= month <= 12:
        # Виклик функції для виведення календаря
        print_calendar(year, month)
    else:
        print("Неправильно введений місяць. Введіть число від 1 до 12.")
