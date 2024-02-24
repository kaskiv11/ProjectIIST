#74. Напишіть програму на Python для хеширования слова.
import hashlib

def hash_word(word):
    # Створюємо об'єкт хешування за допомогою SHA-256
    sha256_hash = hashlib.sha256()

    # Оновлюємо хеш зі словом (потрібно передавати байтовий об'єкт, тому слово перетворюємо в байти)
    sha256_hash.update(word.encode('utf-8'))

    # Отримуємо закодований хеш у вигляді шістнадцяткового числа
    hashed_word = sha256_hash.hexdigest()

    return hashed_word

# Приклад використання
word_to_hash = input("Введіть слово для хешування: ")
hashed_result = hash_word(word_to_hash)

print(f"Хеш слова '{word_to_hash}': {hashed_result}")
