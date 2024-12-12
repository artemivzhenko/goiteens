
input_string = input("Введите строку: ")
words = input_string.split()
result = {word[0]: word for word in words}
print(result)
