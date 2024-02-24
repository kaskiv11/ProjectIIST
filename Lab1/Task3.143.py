#143.Користувач вводить число з діапазону 1-1000.
# Має видрукуватися чи це число є просте

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Введення числа від користувача
user_input = int(input("Введіть число з діапазону 1-1000: "))

# Перевірка чи число просте та виведення результату
if 1 <= user_input <= 1000:
    if is_prime(user_input):
        print(f"{user_input} - просте число.")
    else:
        print(f"{user_input} - не є простим числом.")
else:
    print("Введене число не входить у діапазон від 1 до 1000.")
