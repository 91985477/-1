mount = 12

# символ \ позволяет визуально разбить команду, для интерпретатора это одна строка
bad_condition = \
    mount == 12 or \
    mount == 1 or \
    mount == 2  # Очень плохая запись условия

good_condition = mount in [12, 1, 2]  # При множественном сравнении лучше использовать in

if good_condition:
    print("Зима!!!")