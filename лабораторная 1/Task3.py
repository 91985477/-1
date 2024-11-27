# Параметры книги
pages = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

# Рассчитаем объем данных одной книги в байтах
book_size_bytes = pages * lines_per_page * characters_per_line * bytes_per_character

# Объем дискеты в мегабайтах
diskette_size_mb = 1.44

# Переведем объем дискеты в байты
diskette_size_bytes = diskette_size_mb * 1024 * 1024

# Рассчитаем, сколько книг можно поместить на дискету
number_of_books = diskette_size_bytes // book_size_bytes

# Выведем результат
print(f"На дискету можно поместить {number_of_books} книг.")
