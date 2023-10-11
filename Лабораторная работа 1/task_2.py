storage = 1.44 * 1024 * 1024
pages = 100
rows_per_page = 50
symbols_per_row = 25
byte_per_symbol = 4

byte_per_book = pages * rows_per_page * symbols_per_row * byte_per_symbol
num_of_books = int(storage // byte_per_book)

print("Количество книг, помещающихся на дискету:", num_of_books)
