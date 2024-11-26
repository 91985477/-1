list_students = ["Маша", "Петя", "Саша", "Кирилл", "Оля"]
heights_list = [132, 176, 154, 182, 168]

max_index = 0
for i in range(len(heights_list)):  # перебераем все индексы
    max_height = heights_list[max_index]
    current_height = heights_list[i]
    if current_height > max_height:  # если текущий рост больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального роста

print("Самый высокий человек -", list_students[max_index])
print("Его рост =", heights_list[max_index])