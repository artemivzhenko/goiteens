def triangle(n):
    for i in range(n, 0, -1):
        for t in range(1, i + 1):
            print(t, end=' ')
        print()

n = 4

triangle(n)

