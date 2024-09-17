num= int(input("введіть число"))
result= num % 5 == 0
result_1= num > 100

if result and result_1:
    print("Число кратне 5 і більше 100")
else:
    print("Число не кратне 5 і меньше 100")