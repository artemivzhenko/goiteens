name = input("Введите фамилию студента: ")
points = int(input("Введите количество балов: "))
messege = f"Студент {name} сдал тест." if points > 80 else f"Студент {name} не сдал тест."

print(messege)
