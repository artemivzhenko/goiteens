# def waller(init_balance, currency_p):
#     balance = init_balance
#     currency = currency_p
#
#     def add_balance(money):
#         nonlocal balance
#         balance += money
#         return balance
#
#     def minus_balance(money):
#         nonlocal balance
#         balance -= money
#         return balance
#
#     return add_balance, minus_balance
#
#
# add_wallet_balance, minus_wallet_balance = waller(1000)
#
# balance_now = add_wallet_balance(200)
# print(balance_now)
# balance_now = add_wallet_balance(200)
# print(balance_now)
# balance_now = add_wallet_balance(200)
# print(balance_now)
# balance_now = minus_wallet_balance(100)
# print(balance_now)

#
# def multiply_x(x):
#     number_x = x
#
#     def double_x():
#         nonlocal number_x
#         number_x *= 2
#         return number_x
#
#     def triple_x():
#         nonlocal number_x
#         number_x *= 3
#         return number_x
#
#     return double_x, triple_x
#
#
# my_def = multiply_x
# double, triple = my_def(5)
# print(double())
# print(triple())
#
#
# def pryamokutnic(x, y):
#     side_x = x
#     side_y = y
#
#     def is_square():
#         nonlocal side_x
#         nonlocal side_y
#         return side_x == side_y
#
#     def square():
#         nonlocal side_x
#         nonlocal side_y
#         return side_x * side_y
#
#


# import pretty_errors


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик фукнції {func.__name__}")
        result = []
        for arg in args:
            package_list = arg
            result.append(func(package_list[0], package_list[1]))
        for key, kwarg in kwargs.items():
            print(key)
            package_list = kwarg
            result.append(func(package_list[0], package_list[1]))
        print(f"Функція відпрацюівала без помилок")
        print(F"Відбувся виклик функції {func.__name__} з параметрами \nargs={args} \nkwargs={kwargs}")
        return result
    return wrapper
#
#
# @my_decorator
# def add_numbers(x, y):
#     return x + y
#
#
# print(add_numbers([5, 9], [5, 10], [50, 9], q=[50, 90], w=[0, 9]))
# #
#
#
# x: str = "4"
# x_int: int = int(x)
#
# print(x)
#
#
# def add_numbers(x: list[int], y: dict[int:str]) -> dict[int:str]:
#     return x + y


# def my_function(x, y, *args, **kwargs):
#     result = 0
#     for arg in args:                     # args = arguments
#         result += arg
#     for keyword, arg in kwargs.items():  # kwargs = keyword arguments
#         print("Get keyword %s" % keyword)
#         result += arg
#     print(f"\nargs={args} \nkwargs={kwargs}")
#     return x + y + result
#
#
# print(my_function(1, 2, 89, 2345, 234, 13, 62, n=89, v=88, a=54))
#
#
# class Car:
#
#     def __init__(self, mark, price, color, horse_power):
#         self.mark = mark
#         self.price = price
#         self.color = color
#         self.horse_power = horse_power
#
#     def difference_cars(self, other_car):
#         return self.horse_power > other_car.horse_power
#
#     @staticmethod
#     def difference_cars_s(first_car, second_car):
#         return first_car.horse_power > second_car.horse_power
#
#
# bmw = Car("BMW", "10000", "Black", 800)
#
# print(f"BMW color is {bmw.color}")
#
# volkswagen = Car("Volkswagen", "5000", "Blue", 400)
#
# is_bmw_more_power = bmw.difference_cars_s(bmw, volkswagen)
# print(f"Is BMW more power {is_bmw_more_power}")
#

def get_min(lst):
    min_v = min([abs(x) for x in lst])
    return min_v*(-1 if min_v not in lst else 1) if -min_v not in lst or min_v == 0 or (lst.count(min_v) == 0) else None


print(get_min([2, 4, -1, 3]))
print(get_min([2, 0, -1, 3]))
print(get_min([5, 2, -2]))
