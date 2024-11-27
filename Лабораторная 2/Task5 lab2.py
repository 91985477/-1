import random

def generate_three_digit_number() -> int:
    # Генерируем три случайные цифры
    digit1 = random.randint(0, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)

    # Формируем трехзначное число
    three_digit_number = digit1 * 100 + digit2 * 10 + digit3

    return three_digit_number

# Пример использования
generated_number = generate_three_digit_number()
print(f"Сгенерированное трехзначное число: {generated_number}")
