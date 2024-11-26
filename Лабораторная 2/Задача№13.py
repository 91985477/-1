list_students = ["Маша", "Петя", "Саша", "Кирилл", "Оля"]
heights_list = [132, 176, 154, 182, 168]

max_index = 0
max_height = heights_list[max_index]

for i, current_height in enumerate(heights_list):  # перебераем пары индекс - значение
    max_height = heights_list[max_index]
    if current_height > max_height:  # если текущий рост больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального роста
        max_height = heights_list[max_index]  # и перезаписываем рост

print("Самый высокий человек -", list_students[max_index])
print("Его рост =", max_height)