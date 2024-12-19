#Виконайте перевод списка температур в градусах Фаренгейта, але
# з використанням map та filter

temp_c = []
user= int(input("Введіть температуру в цельсія:"))
temp_c.append(user)
temp_f = list(map(lambda c: c * 9 / 5 + 32, temp_c))
print(f"Температура в градусах Фаренгейта:{temp_f}")