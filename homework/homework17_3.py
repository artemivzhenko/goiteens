#Маючи список імен, використайте спочатку filter, щоб відібрати тільки
# унікальні імена, а потім map для перетворення кожного імені у формат "Ім'я Прізвище",
# додавши фіктивне прізвище "Smith" до кожного імені.

name = ["Anna", "Mike", "Anna", "Sofia", "Mike","Anton"]
name_2 = list(filter(lambda x: name.count(x) == 1, name))
names = list(map(lambda x: f"{x} Smith", name_2))
print(names)