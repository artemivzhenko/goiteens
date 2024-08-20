list_1 = [-2, -4, -6, 2, 5]
list_2 = [3, 4, 6, 7, 6, -4, 1, -6, 5, -7]

list_3 = [list_1, list_2]
x = 0
y = 0
for my_list in list_3:
    for my_item in my_list:
        if my_item > 0:
            x += my_item
        elif my_item < 0:
            y += my_item

print(f"The sum of positive numbers: {x}")
print(f"Difference of negative numbers: {y}")
