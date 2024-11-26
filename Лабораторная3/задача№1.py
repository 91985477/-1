def is_polyndrom(src_str):
    src_str = "".join(src_str.split())  # избавляемся от пробелов
    src_str = src_str.lower()  # приводим строку к нижнему регистру

    return src_str == src_str[::-1]

s = "Кит на море не романтик"
print("Строка", repr(s), "полиндром?", is_polyndrom(s))