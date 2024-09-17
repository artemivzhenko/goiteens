students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 81, 85]],
    ["Charlie", [92, 87, 85]],
    ["Diana", [89, 92, 94]],
    ["Edward", [76, 80, 79]]
]
user= input("Введіть ім'я учня:")

if user == students[0][0]or students[1][0]or students[2][0]or students[3][0]or students[4][0]:
    print("Ім'я успішне")
else:
    print("Ім'я неправильне")
great= input("Введіть оцінку яку хочете добавити:")