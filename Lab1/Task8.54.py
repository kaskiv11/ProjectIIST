#54. Напишіть програму на Python,
# щоб отримати поточне ім'я користувача.
import getpass

# Отримати поточне ім'я користувача
current_username = getpass.getuser()

print(f"Поточне ім'я користувача: {current_username}")