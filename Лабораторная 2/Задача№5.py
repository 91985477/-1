hour = 7

bad_condition = (6 <= hour) and (hour < 12)  # Плохая запись условия
good_condition = 6 <= hour < 12  # цепочки операторов всегда соединяются через AND

if good_condition:
    print("Утро!!!")