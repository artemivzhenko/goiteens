import math
# map


def mu_function(number):
    return (number * 2) / 3


my_list = [15, 16, 17, 18, 19, 20, 21, 22, 23]

my_map_list = map(mu_function, my_list)

# print(my_map_list)
#
# for i in my_map_list:
#     print("number from list:", i)


my_c_list = [(i*2)/3 for i in my_list]

# print(my_c_list)


def my_filter_function(number):
    return number % 3 == 0


my_list = [15, 16, 17, 18, 19, 20, 21, 22, 23]
my_filter_list = filter(my_filter_function, my_list)

for i in my_filter_list:
    print("number from list:", i)

# MAX
print("max from list:", max(my_list))
print("min from list:", min(my_list))
print("sum from list:", sum(my_list))
print("my list length:", len(my_list))


my_list_for_all = ["1", 2, True]

print('"" in boolean = ', bool(""))
print('0 in boolean = ', bool(0))
print('None in boolean = ', bool(None))

print(all(my_list_for_all))


ages_list = [12, 13, 14]
names_list = ["Ivan", "Andriy", "Artur"]

my_zip_list = zip(ages_list, names_list)

for i in my_zip_list:
    print(i)


my_lambda_function = lambda x, y: x * y

print("map and lambda function for my list", my_lambda_function(10, 20))


print("Pi number", math.pi)
print("Sinus function", math.sin(90))
print("Cosinus function", math.cos(180))
print("Tangens function", math.tan(180))
print("Factorial for 6", math.factorial(6))
print("SQRT", math.sqrt(64))
