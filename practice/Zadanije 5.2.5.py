def print_pyramid(n):
    current_number = 1
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')

        for j in range(1, i + 1):
            print(current_number, end=' ')
            current_number += 1

        print()


n = int(input("Введите значенние n: "))
print_pyramid(n)
