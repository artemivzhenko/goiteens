numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]


def user_max(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num>max_num:
            max_num = num
    return max_num


def user_mim(numbers):
     min_num = numbers[0]
     for num in numbers[1:]:
         if num<min_num:
             min_num = num
     return min_num

min_number = user_mim(numbers)
max_number = user_max(numbers)
print("min number is "+str(min_number))
print("max number is "+str(max_number))