def print_inverted_triangle(n):
    for i in range(n, 0, -1)
        for j in range(1, 1+1):
                print(j, end= " , ")
print()



n = int(input("Enter the size of the multiplication table (n): "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=' ')
    print()




n = int(input("Введіть значення n: "))

current_number = 1
for i in range(1, n + 1):

    print(' ' * (n - i), end='')

    for j in range(i):
        print(current_number, end=' ')
        current_number += 1

    print()
