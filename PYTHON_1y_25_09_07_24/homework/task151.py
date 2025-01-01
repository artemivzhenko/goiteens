def squares(*args, **kwargs):

    result = []
    for num in args:
        result.append(num**2)
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            result.append(value**2)
    return result

numbers = (1, 2, 3, 4)
result1 = squares(*numbers)
print(result1)

result2 = squares(a=5, b=6, c=7)
print(result2)

result3 = squares(1, 2, x=3, y=4)
print(result3)