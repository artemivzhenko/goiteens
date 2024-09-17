even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for index, number in enumerate(even_numbers):
    if index % 2 == 0:
        print(f"Индекс: {index}, Номер: {number}")
