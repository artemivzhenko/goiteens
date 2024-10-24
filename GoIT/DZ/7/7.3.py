my_string = "hello World"

for index, letter in enumerate(my_string):
    if letter.isupper():
        print(f"Индекс первой заглавной буквы: {index}")
        break
