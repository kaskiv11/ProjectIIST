#81. Напишіть програму на Python для об'єднань N строк

def concatenate_strings(strings):
    # Використовуємо метод join для об'єднання строк
    result = ''.join(strings)
    return result

# Введення кількості строк
n = int(input("Введіть кількість строк: "))

# Введення строк в список
input_strings = []
for i in range(n):
    string = input(f"Введіть строку {i + 1}: ")
    input_strings.append(string)

# Об'єднання строк
concatenated_result = concatenate_strings(input_strings)

# Виведення результату
print("Результат об'єднання строк:")
print(concatenated_result)
