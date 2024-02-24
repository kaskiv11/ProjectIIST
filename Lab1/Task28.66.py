#66. Напишіть програму на Python для розсилки індекса маси тіла

def calculate_bmi(weight, height):
    # Формула для розрахунку індексу маси тіла (BMI): вага / (зріст в метрах)^2
    bmi = weight / (height ** 2)
    return bmi

if __name__ == "__main__":
    # Введення ваги та зросту від користувача
    weight = float(input("Введіть вагу (кг): "))
    height = float(input("Введіть зріст (м): "))

    # Виклик функції для розрахунку індексу маси тіла
    bmi_result = calculate_bmi(weight, height)

    # Виведення результату
    print(f"Ваш індекс маси тіла (BMI): {bmi_result:.2f}")
