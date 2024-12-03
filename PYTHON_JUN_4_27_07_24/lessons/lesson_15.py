import random


def double_numbers(number1, number2=10, number3=5, number4=8, *args):
    """
    make some calculations
    :param number1: any number
    :param number2: any number (default 10)
    :param number3: any number (default 5)
    :param number4: any number (default 8)
    :return: ((number1/number2) * (number3/number4)) * 2
    """
    global x
    print(args)
    result = (number1/number2) * (number3/number4)
    result *= 2
    x = x + 10
    return result


x = 3
y = 4
z = 6
double_x_y = double_numbers(x, z, 1, 2, 3, 4, 5)
print(double_x_y)
print(x)


def get_min_get_max_from_list(my_list):
    list_min = min(my_list)
    list_max = max(my_list)
    return list_min, list_max



list_1 = []
for i in range(10):
    list_1.append(random.randint(15, 20))

print(get_min_get_max_from_list(list_1))