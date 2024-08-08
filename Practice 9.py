#Напишіть функцію для перетворення імені на ініціали.
# Це завдання суворо приймає два слова з одним пробілом між ними.
def convert_to_letters(name):
    first_name, last_name = name.split()

    letters = first_name[0].upper() + '.' + last_name[0].upper()

    return letters

name = input("Введіть ім'я та прізвище: ")

print(convert_to_letters(name))