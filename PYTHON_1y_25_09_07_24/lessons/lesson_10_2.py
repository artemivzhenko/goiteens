num_input = int(input("введіть число:"))
for num in range(1, num_input+1):
    for num_2 in range(1, num_input + 1):
        print(num * num_2,end=" ")
    print()