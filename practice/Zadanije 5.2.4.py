def Tablicka_umnozenija_gy_gy(n):
    max_length = len(str(n * n))
    for i in range(1 , n + 1):
        for j in range(1 , n + 1):
            number = i * j
            number_str = str(number) + " " * (max_length - len(str(number)))
            print(number_str, end=' ')
        print()

n = int(input("Введите размер таблицы умноження: "))
Tablicka_umnozenija_gy_gy(n)