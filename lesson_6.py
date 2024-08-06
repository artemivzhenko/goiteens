my_first_list: list = ["Artem", 183475920, True, 0.2312312]

for item in my_first_list:
    print(item)

first_star: str = ""

for number in range(1, 6):
    first_star = "*" * number
    print(first_star)

print("Star = " + first_star)


number: int = 1

while number <= 5:
    print("Number = " + str(number))
    number += 1


# Написати программу яка запитує у користувача число і якщо це число меньше 100 то просить ввести його ще раз