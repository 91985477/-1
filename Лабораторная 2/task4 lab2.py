import random
import string

def generate_password(n: int = 8) -> str:
    # Определяем алфавит
    alphabet = string.ascii_letters + string.digits

    # Генерируем случайный пароль
    password = ''.join(random.sample(alphabet, n))

    return password

# Пример использования
password_length = 12
generated_password = generate_password(password_length)
print(f"Сгенерированный пароль: {generated_password}")
