n = int(input("Введіть число -> \n "))

print(f"Таблиця множення для числа {n}:")
for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")
