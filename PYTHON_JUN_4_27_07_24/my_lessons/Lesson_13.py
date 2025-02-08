# my_list = [18, 17, 17, 12, 12, 10, 11, 18, 11, 14]
# my_list_2 = [1, 1, 0, 3, 4, 3, 4, 5, 3, 1]
# my_list_3 = [15, 18, 18, 18, 18, 18, 16, 15, 19, 15]
# my_list.reverse()
# my_list_2.reverse() ,
# my_list_3.reverse()
# print(my_list)
# print(my_list_2)
# print(my_list_3)
def count_positives_sum_negatives(numbers):
    if not numbers:
        return []

    count_positives = 0
    sum_negatives = 0

    for num in numbers:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num

    return [count_positives, sum_negatives]


input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
result = count_positives_sum_negatives(input_numbers)
print(result)
