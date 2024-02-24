#100. Напишіть програму на Python, щоб отримати ім’я хоста, під час якої виконується підпрограма.

import socket

def get_hostname():
    # Отримання ім'я хоста
    hostname = socket.gethostname()
    return hostname

if __name__ == "__main__":
    # Виклик функції для отримання і виведення ім'я хоста
    host_name = get_hostname()
    print(f"Ім'я хоста: {host_name}")
