from typing import List, Any

def remove_last_occurrence(lst: List[Any], value: Any) -> List[Any]:
    # Проходим по списку с конца
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            # Удаляем элемент и возвращаем список
            lst.pop(i)
            return lst
    # Если элемент не найден, вызываем исключение
    raise ValueError(f"Значение {value} не найдено в списке")

# Пример использования
example_list = [1, 2, 3, 4, 2, 5, 2]
value_to_remove = 2

try:
    modified_list = remove_last_occurrence(example_list, value_to_remove)
    print("Измененный список:", modified_list)
except ValueError as e:
    print(e)
