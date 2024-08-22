n = int(input("Введіть число n -> \n "))

number = 1

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    for t in range(i):
        print(number, end=' ')
        number += 1
    print()