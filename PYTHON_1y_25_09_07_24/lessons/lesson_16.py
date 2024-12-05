import math
#
#
# def multiply_2(values):
#     a, b = values
#     c_2 = a**2 + b**2
#     return math.sqrt(c_2)
#
#
# my_list = [(3, 6), (2, 4), (5, 6), (9, 10), (3, 8)]
# my_multiply_2_list = map(multiply_2, my_list)
#
#
# for i in my_multiply_2_list:
#     print(i)
#
#
# # list comprehension
#
# my_multiply_2_list = [x[0]+x[1] * 2 for x in my_list]
#
# print(my_multiply_2_list)
#
#
# my_not_filter_list = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
#
#
# def filter_divide_by_3(value):
#     return value % 3 == 0
#
#
# my_filtered_list = filter(filter_divide_by_3, my_not_filter_list)
#
# for i in my_filtered_list:
#     print(i)
#
#
# my_list = [45, 46, 47, 48, 49, 50]
#
# my_lambda_map_list = map(lambda x: x * 10, my_list)
#
# for i in my_lambda_map_list:
#     print(i)
#
#
# my_not_filter_list = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
#
# my_filtered_list = filter(lambda x: x % 4 == 0, my_not_filter_list)
#
# print(list(my_filtered_list))

my_list = [1, 2, 3, 4, 5, 6]

convert_to_farengait = map(lambda x: (x * (9 / 5)) + 32, my_list)
print(list(convert_to_farengait))
