number = int(input("Enter your number -> \n"))

result = "Число кратне 5 та більше 100" if number % 5 == 0 and number > 100 else "Число не кратне 5 та менше 100"

print(result)