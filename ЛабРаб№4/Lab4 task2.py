import json

def calculate_sum_of_products(json_file_path: str) -> float:
    # Открываем JSON файл
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений
    total_sum = sum(item['score'] * item['weight'] for item in data)

    # Округляем результат до 3 знаков после запятой
    rounded_sum = round(total_sum, 3)

    return rounded_sum

# Пример использования
json_file_path = 'example.json'  # Укажите путь к вашему JSON файлу
result = calculate_sum_of_products(json_file_path)
print(f"Сумма произведений: {result}")
