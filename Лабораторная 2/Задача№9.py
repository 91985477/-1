heights_list = [132, 176, 154, 182, 168]

max_height = heights_list[0]  # пусть рост первого человека будет самым высоким

for current_height in heights_list:  # перебираем каждый рост
    if current_height > max_height:  # если текущий рост больше того, который встречали ранее
        max_height = current_height  # то перезаписываем максимальный рост

print("Рост самого высокого челокека:", max_height)