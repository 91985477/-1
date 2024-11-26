students_dict = {
    'Саша': 27,
    'Кирилл': 52,
    'Маша': 14,
    'Петя': 36,
    'Оля': 43,
}
min_age = 18  # минимальный возраст

students_list = []
for student in students_dict:
    if students_dict[student] > min_age:
        students_list.append(student)

print("Исходный список:", students_list)

students_list.sort()
print("Отсортированный список:", students_list)