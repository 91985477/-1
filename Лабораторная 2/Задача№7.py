number = 12

condition_1 = number % 2 == 0  # число кратно 2
condition_2 = number % 3 == 0  # число кратно 3

if condition_1 or condition_2:
    print('Число кратно 2 или 3')
else:
    print('Число не (кратно 2 или 3)')

    number = 12

    condition_1 = number % 2 == 0  # число кратно 2
    condition_2 = number % 3 == 0  # число кратно 3

    if condition_1 and condition_2:
        print('Число кратно 2 и 3')
    elif condition_1:
        print('Число кратно 2')
    elif condition_2:
        print('Число кратно 3')
    else:
        print('Число не кратно 2 и не кратно 3)')