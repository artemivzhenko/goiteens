
number_str = input("Введите число в диапазоне от 1 до 999: ")

length = len(number_str)

number = int(number_str)

parity = "парное" if number % 2 == 0 else "непарное"



if length == 1:
    digits = "однозначное"
elif length == 2:
    digits = "двухзначное"
elif length == 3:
    digits = "трёхзначное"

print(f"{parity} {digits} число")