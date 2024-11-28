import json

def csv_to_json(csv_file_path: str, delimiter: str = ',', line_terminator: str = '\n') -> str:
    # Открываем CSV файл для чтения
    with open(csv_file_path, 'r') as file:
        # Читаем все строки из файла
        lines = file.readlines()

    # Разбиваем первую строку на заголовки
    headers = lines[0].strip().split(delimiter)

    # Инициализируем список для хранения данных
    data = []

    # Проходим по оставшимся строкам
    for line in lines[1:]:
        # Разбиваем строку на значения
        values = line.strip().split(delimiter)
        # Создаем словарь для текущей строки
        row_dict = {headers[i]: values[i] for i in range(len(headers))}
        # Добавляем словарь в список данных
        data.append(row_dict)

    # Преобразуем список словарей в JSON строку с отступами равными 4
    json_str = json.dumps(data, indent=4)

    return json_str

# Пример использования
csv_file_path = 'example.csv'  # Укажите путь к вашему CSV файлу
json_output = csv_to_json(csv_file_path)
print(json_output)
