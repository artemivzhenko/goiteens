my_first_list: list = ["Artem", 183475920, True, 0.2312312]

print("Artem" in my_first_list)
print("Ivan" in my_first_list)

for i in "Artem":
    print(i)

names = "Artem,Ivan,Vlad,Arina"

names_list = names.split(",")
print(names_list)


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


# Функція повинна приймати три аргументи: операція (строка/символ), значення1 (число), значення2 (число).
# Функція повинна повертати результат чисел після застосування обраної операції.
# 
# Приклади (Оператор, значення1, значення2) –> результат
# +,4,7 –> 11
# -,15,18) –> -3
# *,5,5) –> 25
# /,49,7) –> 7
