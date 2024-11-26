cart = {
    "Яблоко": 23,
    "Апельсин": 47,
    "Банан": 10
}

for fruit, count in cart.items():  # перебираем пары ключ-значение
    print(fruit)
    print("Количество:", count)
    print()

total_count = sum(cart.values())  # суммируем только значения
print("Общее количество фруктов:", total_count)