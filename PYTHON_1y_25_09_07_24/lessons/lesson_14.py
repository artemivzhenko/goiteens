import random


def multiply_two_numbers(number_1: int, number_2: int=4, number_3: int=3) -> int:
    multiply_result = 1
    args = [number_1, number_2, number_3]
    for arg in args:
        multiply_result *= arg
    return multiply_result


my_number_1 = 6
#my_number_2 = 2
my_number_3 = 5


m_result = multiply_two_numbers(my_number_1, number_3=my_number_3)
print(m_result)



my_string = 'abcde'

print(my_string.find("a"))


import numpy as np

def add_large_numbers(num1_str, num2_str):
    num1_array = np.array(list(map(int, num1_str[::-1])))
    num2_array = np.array(list(map(int, num2_str[::-1])))
    max_len = max(len(num1_array), len(num2_array))
    num1_array = np.pad(num1_array, (0, max_len - len(num1_array)), 'constant')
    num2_array = np.pad(num2_array, (0, max_len - len(num2_array)), 'constant')
    carry = 0
    result = []
    for digit1, digit2 in zip(num1_array, num2_array):
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(total % 10)
    if carry:
        result.append(carry)
    result_str = ''.join(map(str, result[::-1]))

    return result_str