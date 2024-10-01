def negative_numbers():
    number = -10
    for i in range(1,11):
        print(number)
        number+=1


def Practice5():
    a = 1
    while a <= 15:
        print(a)
        a += 1

def Practice6(names):
    for name in names:
        greeting = "Hello " + name
        print(greeting)

names = ["Dima", "Yaroslav", "Zhenya", "Sasha", "Andrii", "Max"]


def Practice10(n):
    for i in range(1, n + 1):
        cube = i ** 3
        print(f"Куб числа {i} дорівнює {cube}")

n = int(input("Введіть число: "))