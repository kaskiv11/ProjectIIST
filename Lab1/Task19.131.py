#131. Напишіть програму на Python для перетворення цілих чисел у двоякові, сохранюючі провідні нулі.
#Приклад даних: 50
#Ожиданий результат: 00001100, 0000001100

def to_binary_with_padding(number, padding):
    binary_representation = bin(number)[2:]  # Отримання двійкового представлення без префіксу '0b'
    padded_binary = binary_representation.zfill(padding)  # Додавання провідних нулів
    return padded_binary

if __name__ == "__main__":
    # Введення цілого числа від користувача
    user_input = int(input("Введіть ціле число: "))

    # Визначення кількості бітів для забезпечення потрібного розміру виведення
    bit_size = 10

    # Виклик функції перетворення в двійковий вигляд зі збереженням провідних нулів
    binary_result = to_binary_with_padding(user_input, bit_size)

    # Виведення результату
    print(f"Двійкове представлення з провідними нулями: {binary_result}")
