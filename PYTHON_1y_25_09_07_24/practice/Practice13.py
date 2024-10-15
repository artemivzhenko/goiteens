def numbers_string(s):
    return s.isdigit()

my_string1 = input("введення -> \n ")

if numbers_string(my_string1):
    print("в рядку тільки цифри")
else:
    print("в рядку не тільки цифри")

def space_remove(input_string):
    return input_string.replace(" ", "")

my_string2 = input("введення -> \n ")
ready = space_remove(my_string2)
print("з видаленими пробілами", ready)

def character_without(string):
    for letter in string:
        if string.count(letter)==1:
            return letter

my_string3 = input("Введення -> \n")
function_result = character_without(my_string3)
print(function_result)