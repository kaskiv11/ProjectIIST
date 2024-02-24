#130. Напишіть програму на Python для перевірки правильності IP-адреси.
import re

def check_ip_address(ip_address):
    # Задайте шаблон для правильної IP-адреси
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

    # Перевірка збігу із шаблоном
    if re.match(ip_pattern, ip_address):
        print(f"{ip_address} - правильний IP-адреса.")
    else:
        print(f"{ip_address} - неправильний IP-адреса.")

if __name__ == "__main__":
    # Введення IP-адреси від користувача
    user_input = input("Введіть IP-адресу: ")

    # Виклик функції перевірки
    check_ip_address(user_input)
