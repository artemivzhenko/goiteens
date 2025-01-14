def reverse(n):
    if n <= 0:
        return ""
    delim = 10
    while n // delim > 10:
        delim *= 10
    if (n % 10) < 10:
        return f"{n}"
    print(n)
    return f"{n // delim}{reverse(n % delim)}"


print(reverse(1234))

# for i in range(10):
#     x = i ** 2
#     print(x)
#
#
# x = 10
# while x > 0:
#     print(x)
#     x = x - 1
#
#
# def my_loop(n, m):
#     if n != m:
#         print(n)
#         my_loop(n + 1, m)
#     return
#
#
# my_loop(0, 10)
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)  # factorial(5) factorial(4) factorial(3) factorial(2) factorial(1)
#         # 5 * 4 * 3 * 2 * 1
#
#
# print(factorial(5))

#
# # 5 * 4 * 3 * 2 * 1 = 5!
#
#
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
# # 1  2  3  4  5  6  7   8   9  10  11  12  13   14   15    16  17    18    19    20
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(2000))
