#Напишіть програму, яка виведе таблицю множення розміру n x n, де n - число, введене користувачем.

n = int(input("Введіть число n -> \n "))

for i in range(1, n+1):
    for t in range(1, n+1):
        print(i * t , end=" ")
    print()
