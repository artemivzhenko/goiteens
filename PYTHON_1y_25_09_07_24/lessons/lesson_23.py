import random as rn

my_new_dictionary: dict = {
    True: "hello world",
    5.5: "5 and dot 5",
    "key1": "my key value",
    10: "number 10"
}

print(my_new_dictionary[True])
print(my_new_dictionary[5.5])
print(my_new_dictionary["key"])
print(my_new_dictionary[10])


def my_function(x):
    return x * 10


my_new_dictionary["function"] = my_function
my_new_dictionary["lib"] = rn

print(my_new_dictionary["function"](2))
print(my_new_dictionary["function"](38))

my_keys = ["key1", "key2", "key3", "key4", "key5"]

value = 10

my_dict_from_keys: dict = dict.fromkeys(my_keys, value)
print(my_dict_from_keys)


for value in my_dict_from_keys.values():
    print(value)


for key in my_dict_from_keys.keys():
    print(key)


for key, value in my_dict_from_keys.items():
    print(key, value)


my_dict_from_keys.update(my_new_dictionary)
print(my_dict_from_keys)
#
#
# def naughty_or_nice(data):
#     naughty_count = 0
#     nice_count = 0
#     for mounth, mounth_data in data.items():
#         print(mounth_data)
#         naughty_count += list(mounth_data.values()).count("Naughty")
#         nice_count += list(mounth_data.values()).count("Nice")
#     print(naughty_count, nice_count)
#     return "Naughty!" if naughty_count > nice_count else "Nice!"
#
# a = 12
#
#
# with open("test.txt", "r") as f:
#     code = ""
#     for line in f:
#         code += line
#     exec(code)

#
# dot = lambda n, m: "".join(["+---" * n + "+\n" + "| o " * n + "|\n" for i in range(m)]) + "+---" * n + "+"
#
# def dot(n, m):
#     return "".join(["+---" * n + "+\n" + "| o " * n + "|\n" for i in range(m)]) + "+---" * n + "+"
#
#
# print(dot(1, 1))

build_pyramid = lambda s, n: "".join([" " * int((len(s)/2)*(n-i)) + "".join([sym*i for sym in s]) + "\n" for i in range(1, n+1)])[:-1]


print(build_pyramid("00-00..00-00",3))