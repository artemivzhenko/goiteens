# Статичний масив чисел
numbers = [1, -4, 7, 12]

# Знаходження суми всіх додатних чисел
positive_sum = sum(num for num in numbers if num > 0)

# Виведення результату
print(f"The sum of all positive numbers is: {positive_sum}")