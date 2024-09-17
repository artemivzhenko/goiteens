n = int(input("введіть число:"))
number = 1
for item in range(1, n+1):
    for num in range(1,item+1):
        print(number, end=" ")
        number += 1
    print()


