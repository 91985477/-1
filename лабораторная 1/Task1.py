# Исходный список с пропущенным элементом
numbers = [2, -93, -2, 8, -15.65, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25, None]

# Найдем индекс пропущенного элемента
missing_index = numbers.index(None)

# Удалим пропущенный элемент для расчета среднего арифметического
numbers_without_missing = [num for num in numbers if num is not None]

# Рассчитаем среднее арифметическое
average = sum(numbers_without_missing) / len(numbers)

# Заменим пропущенный элемент средним арифметическим
numbers[missing_index] = average

# Выведем исправленный список
print("Исправленный список:", numbers)