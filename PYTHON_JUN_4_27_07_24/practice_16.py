# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def math_operators(operator, number_x, number_y):
    plus_function = lambda x, y: x + y
    minus_function = lambda x, y: x - y
    multiply_function = lambda x, y: x * y
    divide_function = lambda x, y: x / y
    match operator:
        case "+":
            return plus_function(number_x, number_y)
        case "-":
            return minus_function(number_x, number_y)
        case '*':
            return multiply_function(number_x, number_y)
        case '/':
            return divide_function(number_x, number_y)
        case _:
            return 0


print(math_operators("+", 10, 57))
print(math_operators("-", 10, 57))
print(math_operators("*", 10, 57))
print(math_operators("/", 10, 57))
print(math_operators("bla bla", 10, 57))




