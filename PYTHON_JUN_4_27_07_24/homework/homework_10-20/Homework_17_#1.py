def square_numbers(*args, factor=1):

    result = []
    for num in args:
        result.append((num ** 2) * factor)
    return result


print(square_numbers(1, 2, 3))
print(square_numbers(4, 5, 6, factor=2))
print(square_numbers(7, 8, factor=3))
