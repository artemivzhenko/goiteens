my_list = [10, 20, 30, 40, 50]

for index, value in enumerate(reversed(my_list)):
    print(f"Индекс {len(my_list) - 1 - index}: Значение {value}")
