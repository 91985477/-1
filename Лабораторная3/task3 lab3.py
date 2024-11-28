def to_csv_file(filename: str, headers: list, rows: list, delimiter: str = ',', new_line: str = '\n') -> None:
    # Открываем файл для записи
    with open(filename, 'w') as file:
        # Записываем заголовки
        file.write(delimiter.join(headers) + new_line)

        # Записываем строки данных
        for row in rows:
            # Преобразуем каждый элемент строки в строку и объединяем их с помощью разделителя
            row_str = delimiter.join(map(str, row))
            file.write(row_str + new_line)
            yield row_str  # Возвращаем строку для генератора

# Пример использования
headers_list = ['Name', 'Age', 'City']
data = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Записываем данные в файл output.csv
generator = to_csv_file('output.csv', headers_list, data)

# Проходим по генератору, чтобы записать все данные
for _ in generator:
    pass
