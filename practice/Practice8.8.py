word = input("Put your word -> \n")
my_litter = input("Put your letter -> \n")
my_litter_count = 0
for litter in word:
    if litter == my_litter:
        my_litter_count += 1
        break
else:
    print("My loop end successful")
print(my_litter_count)