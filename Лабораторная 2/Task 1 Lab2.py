import random

def generate_unique_random_list(size, start, end):
    if end - start + 1 < size:
        raise ValueError("Диапазон чисел слишком мал для создания списка указанного размера с уникальными числами.")

    # Создаем список всех возможных чисел в заданном диапазоне
    possible_numbers = list(range(start, end + 1))

    # Перемешиваем список
    random.shuffle(possible_numbers)

    # Возвращаем первые `size` элементов из перемешанного списка
    return possible_numbers[:size]

# Параметры
size = 15
start = -10
end = 10

# Генерация списка
unique_random_list = generate_unique_random_list(size, start, end)
print(unique_random_list)