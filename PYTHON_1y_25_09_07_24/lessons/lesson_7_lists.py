my_list = [2, 2, 2, 2, 2, 76, 17, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

my_list.append(88)

print(my_list[-1])

print(len(my_list))

print(f"Index of 76 is {my_list.index(76)}")

my_list.insert(4, 234)

print(my_list[4])

my_list.remove(234)

print(my_list[4])


my_new_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    [88, 243, 1235, 76, 15, 87, 80],
    my_list
]

print(my_new_list[2][3], my_list[3])

for inside_list in my_new_list:
    for item in inside_list:
        print(item, end=" | ")
    print()

my_range_list = [number * -1 for number in my_list]
print(my_range_list)

my_tuple = (2, 2, 2, 2)

my_set = {2, 2, 2, 8, 1}
print(my_set)

my_list.sort()

my_set_list = set(my_list)

my_list = [88, 243, 1235, 76, 15, 87, 80, 12, 75, 87]
my_list.sort()
# print(my_list)

my_new_list = my_list[::-1]
my_list.reverse()
# print(f"My reverse list {my_list}")

my_second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13, 13, 13, 13, 13]

my_list.extend(my_second_list)
my_summary_list = my_list + my_second_list
print(my_summary_list)

print(my_summary_list.count(13))

my_copy_list = my_summary_list.copy()
print(my_copy_list)


if 13 not in my_copy_list:
    print("yes")
else:
    print("no")

my_list = [2, 76, 17, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

for item_index, item in enumerate(my_list):
    print(f"Item index:{item_index} | item value: {item}")
