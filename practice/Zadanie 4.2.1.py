num = int(input("Введите целое число: "))

resultat = "Число кратное 5 и больше 100" if num % 5 == 0 and num >= 100 else "Число не кратно 5 и меньше 100"

print(resultat)