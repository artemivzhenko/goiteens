def find_first_uppercase(s):
    for index, char in enumerate(s):
        if char.isupper():
            return index
    return -1


string = "hello World"
result = find_first_uppercase(string)
print(f"Индекс первой заглавной буквы: {result}")


