def find_two_largest(nums):

    unique_nums = list(set(nums))

    unique_nums.sort(reverse=True)

    return unique_nums[:2]


user_input = input("Введите числа через пробел: ")

nums = list(map(int, user_input.split()))

result = find_two_largest(nums)
print("Два найбольших значенния:", result)
