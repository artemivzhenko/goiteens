names = input("Введите имена через пробел: ").split()

unique_names = list(filter(lambda name: names.count(name) == 1, names))

full_names = list(map(lambda name: f"{name} Smith", unique_names))

print("Уникальные имена с добавленной фамилией:", full_names)
