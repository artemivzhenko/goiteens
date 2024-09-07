#
#
# my_list.append(88)
#
# print(my_list[-1])
#
# print(len(my_list))
#
# print(f"Index of 76 is {my_list.index(76)}")
#
# my_list.insert(4, 234)
#
# print(my_list[4])
#
# my_list.remove(234)
#
# print(my_list[4])

# my_list = [81, 52, 23, 54, 65, 76, 17, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#
# my_new_list = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#     [88, 243, 1235, 76, 15, 87, 80],
#     my_list
# ]
#
# # print(my_new_list[2][3], my_list[3])
#
# for inside_list in my_new_list:
#     for item in inside_list:
#         print(item, end=" | ")
#     print()

my_list = [2, 2, 2, 2, 2, 76, 17, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
my_range_list = [number * -1 for number in my_list]
print(my_range_list)

# my_tuple = (2, 2, 2, 2)
#
# my_set = {2, 2, 2, 8, 1}
# print(my_set)
#
my_list.sort()
