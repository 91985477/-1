import csv
import json

def csv_to_json(csv_file_path: str, delimiter: str = ',', line_terminator: str = '\n') -> str:
    # Открываем CSV файл
    with open(csv_file_path, newline='') as csvfile:
        # Создаем CSV reader с указанными разделителями
        csvreader = csv.DictReader(csvfile, delimiter=delimiter, lineterminator=line_terminator)

        # Преобразуем данные в список словарей
        data = [row for row in csvreader]

    # Преобразуем список словарей в JSON строку с отступами равными 4
    json_str = json.dumps(data, indent=4)

    return json_str

# Пример использования
csv_file_path = 'example.csv'  # Укажите путь к вашему CSV файлу
json_output = csv_to_json(csv_file_path)
print(json_output)
