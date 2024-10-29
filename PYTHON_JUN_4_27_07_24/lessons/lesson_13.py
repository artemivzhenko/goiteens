# Type list
my_list = ['Artem', 'Nazar', 'Maryan', 'Svitlana', 'Andriy', 'Artur', "111"]
#             0        1         2          3          4         5     6   7   8    9     10     11     12
#           -13       -12       -11        -10         -9       -8    -7  -6  -5   -4     -3     -2     -1
import random

last_index = len(my_list) - 1

random_index = random.randint(0, last_index)

print(my_list[random_index])

print(my_list[1:6:2])

print(f"Повертає розмірність списку {len(my_list)}")
# print(my_list.index('Maryan'))
# my_list.sort()
# print(my_list)
#
# my_list_2 = my_list[::-1]
# print(my_list_2)
#
#
# my_list.reverse()
# print(my_list)
#
#
# for item in my_list:
#     print(f"Item in my list {item}")

my_list.append("Ivan")
print(my_list)
my_list.insert(3, "Dmitriy")
print(my_list)

my_list.remove("Ivan")
print(my_list)


my_value = "Egor"
my_list.append(my_value)
print(my_list)
my_value = "Kiril"
print(my_list)

my_list[2] = "Kiril"
print(my_list)

#Type tuple

my_tuple = ('Artem', 'Nazar', 'Maryan')
print(my_tuple[2])
for item in my_tuple:
    print(item)
my_tuple = tuple(my_list)
print(my_tuple)

# Type set
my_list = ['Artem', 'Nazar', 'Nazar', 'Nazar', 'Nazar', 'Artem', 'Artem', 'Artem']
my_set = set(my_list)
print(my_set)


# Type dictionary

my_dictionary = {
    "key": "value",
    "name": "Ivan",
    "age": 10,
    "surname": "Jhonatan",
    "username": "ijhon",
    "password": "fhbsadbcahsdbc",
    "books": ["Shevchenko", "Skovoroda"],
    "is_a_man": True,
    "is_marry": False,
}
print(my_dictionary["age"])
print(my_dictionary["is_marry"])
print(my_dictionary["password"])
print(my_dictionary["name"])
print(my_dictionary["books"])

for key in my_dictionary.keys():
    print(key)
for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(key, value)

