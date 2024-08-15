#PRACTICE 15.8

number = int(input("Введіть ціле число: "))
result = "Число кратне 5 і більше 100" if number % 5 == 0 and number > 100 else "Число не кратне 5 і менше 100"
print(result)