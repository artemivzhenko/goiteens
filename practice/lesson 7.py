def check_number_in_range(number):
    result = "Число кратне 5 і більше 100" if number**5 >= 100 else "Число не кратне 5 і меньше 100”."
    return result

input_number = int(input("Введіть ціле число: "))
print(check_number_in_range(input_number))