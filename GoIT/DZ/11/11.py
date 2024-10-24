input_string = input("Введите строку: ")

result_string = ''.join(char for char in input_string if not char.isdigit())

print(f"Строка без цифр: {result_string}")
