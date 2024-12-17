number = float(input("Введіть число: "))
square = number ** 2
print("Квадрат числа:", square)


number = float(input("Введіть число: "))
square = number ** 2
squared_list = list(str(square))
joined_string = " ".join(squared_list)
print("Квадрат числа зі списку об'єднаних назад у рядок:", joined_string)


favorite_color = "синій"
favorite_animal = "кіт"
combined_string = f"Моя улюблена тварина - {favorite_animal}, а улюблений колір - {favorite_color}"
print(combined_string)


favorite_food = "піца"
favorite_drink = "сік"
combined_string = f"Моя улюблена їжа - {favorite_food}, а улюблений напій - {favorite_drink}"
print(combined_string)


first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
difference = first_number - second_number
print(f"Різниця між {first_number} та {second_number} дорівнює {difference}")


first_name = "Іван"
last_name = "Петренко"
full_name = f"{first_name}-{last_name}".lower()
print(full_name)


favorite_quote = "Завжди прагни бути найкращим, але не забувай залишатись людиною."
author = "Конфуцій"
combined_quote = f"«{favorite_quote}» - {author}"
print(combined_quote)
